from hooks.post_gen_project import *


def test_extract_version():
    inputs = ["refs/tags/de_core_news_lg-2.3.0", "refs/tags/de_core_news_lg-3.0.0a0", "refs/tags/de_core_news_md-3.1.0"]
    results = ["2.3.0", "3.0.0a0", "3.1.0"]

    for input, result in zip(inputs, results):
        version = extract_version({"ref": input})
        assert version == result


def test_matching_suffix():
    inputs = [("lg", "refs/tags/de_core_news_lg-2.3.0"), ("trf", "refs/tags/zh_core_web_trf-3.0.0a0"),
              ("md", "refs/tags/de_core_news_md-3.1.0")]

    for input in inputs:
        assert matching_suffix({"ref": input[1]}, input[0]) is True


def test_not_matching_suffix():
    inputs = [("md", "refs/tags/de_core_news_lg-2.3.0"), ("lg", "refs/tags/zh_core_web_trf-3.0.0a0"),
              ("trf", "refs/tags/de_core_news_md-3.1.0")]

    for input in inputs:
        assert matching_suffix({"ref": input[1]}, input[0]) is False


def test_extract_project_spacy_version():
    pyproject_content = """# Documentation
    sphinx = "^4.0.3"
    "sphinxcontrib.datatemplates" = "^0.8.1"
    pyyaml = "^5.3.1"
    sphinx-rtd-theme = "^0.5.2"
    myst-parser = "^0.15.1"

    #Spacy
    spacy = "^3.0.6"
    "spacy-lookups-data" = "^1.0.2"

    #Misc
    pathlib2 = "^2.3.5"
    aiofiles = "^0.6.0"
    dvc = {extras = ["ssh"], version = "^2.5.0"}"""
    major, minor = extract_project_spacy_major_version(pyproject_content)

    assert major == "3" and minor == "0"


def test_extract_project_spacy_major_version_complex_defintion():
    pyproject_content = """# Documentation
    sphinx = "^4.0.3"
    "sphinxcontrib.datatemplates" = "^0.8.1"
    pyyaml = "^5.3.1"
    sphinx-rtd-theme = "^0.5.2"
    myst-parser = "^0.15.1"

    #Spacy
    spacy = {extras = [some-extra], version = "^3.0.6"}
    "spacy-lookups-data" = "^1.0.2"

    #Misc
    pathlib2 = "^2.3.5"
    aiofiles = "^0.6.0"
    dvc = {extras = ["ssh"], version = "^2.5.0"}"""
    major, minor = extract_project_spacy_major_version(pyproject_content)
    assert major == "3" and minor == "0"

    pyproject_content = """# Documentation
        sphinx = "^4.0.3"
        "sphinxcontrib.datatemplates" = "^0.8.1"
        pyyaml = "^5.3.1"
        sphinx-rtd-theme = "^0.5.2"
        myst-parser = "^0.15.1"

        #Spacy
        spacy = {version = "^3.0.6", extras = [some-extra]}
        "spacy-lookups-data" = "^1.0.2"

        #Misc
        pathlib2 = "^2.3.5"
        aiofiles = "^0.6.0"
        dvc = {extras = ["ssh"], version = "^2.5.0"}"""
    major, minor = extract_project_spacy_major_version(pyproject_content)
    assert major == "3" and minor == "0"


def read_spacy_tags():
    try:
        with open("tests/data/spacy_tags.json", "r") as file:
            return json.load(file)
    except:
        with open("data/spacy_tags.json", "r") as file:
            return json.load(file)


def test_find_matching_model():
    models = read_spacy_tags()
    assert find_matching_model("de", "3", "1", models, "sm") == "de_core_news_sm-3.1.0"


def test_find_matching_model_en():
    models = read_spacy_tags()
    assert find_matching_model("en", "3", "1", models, "sm") == "en_core_web_sm-3.1.0"


def test_scrap_spacy_model():
    pyproject_content = """# Documentation
       sphinx = "^4.0.3"
       "sphinxcontrib.datatemplates" = "^0.8.1"
       pyyaml = "^5.3.1"
       sphinx-rtd-theme = "^0.5.2"
       myst-parser = "^0.15.1"

       #Spacy
       spacy = {extras = [some-extra], version = "^3.0.6"}
       "spacy-lookups-data" = "^1.0.2"

       #Misc
       pathlib2 = "^2.3.5"
       aiofiles = "^0.6.0"
       dvc = {extras = ["ssh"], version = "^2.5.0"}"""
    models = read_spacy_tags()
    name, url, version = scrap_spacy_model(models, "de", pyproject_content, suffix="sm")

    expected_name = "de-core-news-sm"
    expected_url = "https://github.com/explosion/spacy-models/releases/download/de_core_news_sm-3.0.0/de_core_news_sm-3.0.0.tar.gz"
    expected_version = "3.0.0"
    assert name == expected_name and url == expected_url and version == expected_version
