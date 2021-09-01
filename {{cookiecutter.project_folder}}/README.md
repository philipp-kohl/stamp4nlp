# {{cookiecutter.project_name}}

## Description
{{cookiecutter.project_short_description}}

## Installation
1. This software runs with [poetry](https://python-poetry.org/docs/#system-requirements), so make sure to install it.
2. Install all dependencies with `poetry install`

## Data Management
[Data Version Control, or DVC](https://dvc.org/doc), is a data and ML experiments management tool.
It works with git, so make sure to create a git repository before using DVC.

### Init Data
- Move your (original-/raw-)data to the `data/raw` directory
- track them with `dvc add data/raw`
- add the created `*.dvc` and `.gitignore` files to git
- push the data to the DVC-Remote with `dvc push`

For more information about your dvc remote use `dvc remote list` or visit the [DVC-SSH-Server-Project](https://git.fh-aachen.de/LaborBusinessProgramming/other-projects/dvc-ssh-server)

### Load Data
You cloned this repository and you're missing data?
```
dvc pull
```

## Scripts
You can run the following scripts:
- Start the server with `poetry run server`
- Run tests with `poetry run pytest`
- Generate documentation with `poetry run gen_doc`

Note: you may need to run `poetry install` after **installing** or **updating** the scripts

## REST-Service

The REST-Service is build with [uvicorn](https://www.uvicorn.org/) and [fastapi](https://fastapi.tiangolo.com/tutorial/first-steps/).
You can always check the REST-Documentation by starting the server and checking `localhost:8000/docs` in your browser
