import os
import yaml
from pathlib import Path
from typing import List
import fnmatch
import data.raw
import data.processed
import data.interim
import models

#Relative to root folder, because they are used in poetry run.
docs_source = "docs/source/"
docs_build = "docs/build/"

interim_data_dir = data.interim.__path__[0]
processed_data_dir = data.processed.__path__[0]
raw_data_dir = data.raw.__path__[0]

models_dir = models.__path__[0]

blacklist = ["*.gitkeep", "*__init__.py", "*__pycache__/*"]

documentation_artifacts_dir = "../docs/source/_data/artifacts"
instance_key = "instance_specific"


def get_all_artifacts() -> List[str]:
    return get_all_files_from_dir(Path(documentation_artifacts_dir))


def get_all_models() -> List[str]:
    return get_all_files_from_dir_filtered(Path(models_dir), blacklist)


def get_all_processed_data() -> List[str]:
    return get_all_files_from_dir_filtered(Path(processed_data_dir), blacklist)


def get_all_interim_data() -> List[str]:
    return get_all_files_from_dir_filtered(Path(interim_data_dir), blacklist)


def get_all_raw_data() -> List[str]:
    return get_all_files_from_dir_filtered(Path(raw_data_dir), blacklist)


def get_all_files_from_dir_filtered(path: Path, blacklist) -> List[str]:
    files = get_all_files_from_dir(path)
    filtered_files = []
    for file in files:
        if any(fnmatch.fnmatch(file, pattern) for pattern in blacklist):
            continue
        filtered_files.append(file)

    return filtered_files


def is_valid_dir_path(path: Path) -> bool:
    return path.exists() and path.is_dir()


def make_save_dir(path: Path, save_path) -> Path:
    save_path = save_path or os.path.join(path, 'generated')
    save_path = Path(save_path)
    os.makedirs(save_path, exist_ok=True)
    return save_path


def get_all_files_from_dir(path: Path) -> List[str]:
    all_files = list()
    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = Path(os.path.join(root, file))
            all_files.append(full_path)
    return all_files


def read_yaml(file):
    with open(file, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
            return data
        except yaml.YAMLError as exc:
            print(exc)


def read_values_from_yaml(file):
    data = read_yaml(file)
    return data[instance_key]


def read_value_from_yaml(file, key):
    data = read_yaml(file)
    return data[instance_key][key]


if __name__ == '__main__':
    print('Raw Data: ', get_all_raw_data())
    print('Interim Data: ', get_all_interim_data())
    print('Processed Data: ', get_all_processed_data())
    print('Models: ', get_all_models())
    print('Artifacts: ', get_all_artifacts())

    print(read_yaml(get_all_artifacts()[0]))

    print(read_value_from_yaml(get_all_artifacts()[0], 'name'))
