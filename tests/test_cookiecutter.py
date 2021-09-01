from cookiecutter.main import cookiecutter
from pathlib import Path
import yaml


def _run_cookiecutter(config: dict, tmpdir_factory):
    path = Path.cwd()
    generated = tmpdir_factory.mktemp('generated')
    generated_output = Path(tmpdir_factory.mktemp('generated_output'))

    # this took me way to long to find
    # https://cookiecutter.readthedocs.io/en/1.7.2/advanced/user_config.html
    if 'default_context' not in config:
        cookiecutter_config = {
            'default_context': config
        }
    else:
        cookiecutter_config = config

    config_path = generated.join("generated_config.yaml")
    with open(config_path, 'w', encoding='utf-8') as fp:
        yaml.dump(cookiecutter_config, fp, allow_unicode=True, default_flow_style=False)

    result = cookiecutter(str(path), no_input=True, output_dir=str(generated_output), config_file=config_path)
    return Path(result).exists()


def test_cookiecutter(tmpdir_factory):
    """
    test from root
    """
    config = {
        "project_name": "generated_project",
        "project_author": "pytest",
        "project_author_email": "pytest@fh-aachen.de"
    }
    res = _run_cookiecutter(config, tmpdir_factory)
    assert res
