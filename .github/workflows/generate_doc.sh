#!/bin/bash
startPath="$PWD"
# Install cookiecutter and export path
pip install --user cookiecutter
export PATH=$HOME/.local/bin:$PATH
source ~/.profile
# Cookiecutter installation end
poetry config virtualenvs.create false
source /opt/poetry/env
cd "$startPath"
cookiecutter --no-input . project_name="NLP Process Model" project_author="Philipp Kohl" project_author_email="p.kohl@fh-aachen.de"
cd nlp-process-model
poetry install --no-root
poetry run gen_doc
cd "$startPath"