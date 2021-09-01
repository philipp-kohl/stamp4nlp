import json
import os
import pathlib
import re
from urllib.request import urlopen
from distutils.version import StrictVersion

from cookiecutter.main import cookiecutter

SPACY_MODEL_REPO = "https://api.github.com/repos/explosion/spacy-models/git/refs/tags"
PYPROJECT_TOML_PATH = "pyproject.toml"


def extract_version(model: dict):
    tag: str = model["ref"]
    tag = tag.replace("refs/tags/", "")
    version = tag.split("-")[-1]
    return version


def matching_version(model: dict, target_major_version: str, target_minor_version: str):
    version = extract_version(model)
    model_major_version, model_minor_version, _ = version.split(".")
    return model_major_version == target_major_version and model_minor_version == target_minor_version


def matching_suffix(model: dict, suffix: str):
    ref = model["ref"].split("-")[0]
    return ref.endswith(suffix)


def read_project_config():
    with open(PYPROJECT_TOML_PATH, "r") as file:
        pyproject = file.read()

    return pyproject


def load_spacy_model_repo_tags():
    contents = urlopen(SPACY_MODEL_REPO).read()
    spacy_model_tags = json.loads(contents)
    return spacy_model_tags


def extract_project_spacy_major_version(pyproject):
    match = re.search(r"spacy\s?=(.*)", pyproject)

    if match:
        right_hand_side = match.group(1).replace(" ", "")
        if right_hand_side.startswith("{") and right_hand_side.endswith("}"):
            # handle spacy = {extras = ["..."], version = "^2.5.0"}
            match = re.search(r"version=\"(.*)\"", right_hand_side)
            if match:
                right_hand_side = match.group(1)
            else:
                raise Exception("Spacy version cannot be extracted from pyproject.toml")

        spacy_version = right_hand_side.replace("^", "").replace("\"", "")
        major, minor, patch = spacy_version.split(".")
        return major, minor
    else:
        raise Exception("Spacy version cannot be extracted from pyproject.toml")


def find_matching_model(language, major_version, minor_version, spacy_model_tags, suffix):
    language_models = []
    for tag in spacy_model_tags:
        try:
            if tag["ref"].startswith(f"refs/tags/{language}") and "alpha" not in tag["ref"]:
                if matching_version(tag, major_version, minor_version):
                    if matching_suffix(tag, suffix):
                        language_models.append(tag)
        except:
            print(f"{tag['ref']} will be ignored!")

    sorted_models = sorted(language_models, key=lambda model: StrictVersion(extract_version(model)), reverse=True)
    choice = sorted_models[0]
    name = choice["ref"].split("/")[-1].replace("\"", "").replace("'", "")
    return name


def scrap_spacy_model(spacy_model_tags: dict, language: str, pyproject_content: str, suffix="sm"):
    # Extract major and minor version for spacy
    major_version, minor_version = extract_project_spacy_major_version(pyproject_content)

    name_n_version = find_matching_model(language, major_version, minor_version, spacy_model_tags, suffix)
    name = name_n_version.split("-")[0].replace("_", "-")
    url = f"https://github.com/explosion/spacy-models/releases/download/{name_n_version}/{name_n_version}.tar.gz"
    version = name_n_version.split("-")[-1]
    return name, url, version


def generate_template(application_type: str):
    if application_type.strip().lower() == "blank":
        return

    template_type, template_url = application_type.split("=")
    template_type = template_type.strip()
    template_url = template_url.strip()
    code_folder = "{{cookiecutter.project_slug}}"
    project_folder = "{{cookiecutter.project_folder}}"
    config = {"code_dir": code_folder, "root": pathlib.Path("..") / project_folder}

    cookiecutter(template_url,
                 no_input=True,
                 extra_context=config,
                 output_dir="./",
                 overwrite_if_exists=True)


if __name__ == '__main__':
    try:
        name, url, version = scrap_spacy_model(load_spacy_model_repo_tags(),
                                               "{{cookiecutter.project_language}}",
                                               read_project_config())
        os.system(f"poetry add {url} --lock")
    except Exception:
        print("Language model cannot be added automatically. Please add it to pyproject.toml in this format: "
              "<name-of-language-model> = {url = \"https://github.com/explosion/spacy-models/releases/download/<name_and_version"
              ">/<name_and_version>.tar.gz\"}")

    try:
        generate_template("{{cookiecutter.application_type}}")
    except Exception:
        print("Template code could not be incorporated. Please add the files to the generated directory.")
