.. _folder_structure:

Folder Structure
================

A standardized folder structure supports the users to know where data, code, documentation, reports and much more are located and where elements should be saved to.
The predefined STAMP 4 NLP folder structure looks as follows:

::

   root                     <- Will be named as your project name with hyphens
   |--data
      |--raw
      |--interim
      |--processed
   |--docs
      |--build
      |--source
   |--models
   |--notebooks
      |--exploratory
      |--reports
   |--{project_code}        <- Will be named as your project name with underscores
      |--api
      |--preprocessing
      |--scripts
      |--configuration.py
      |--main.py
   |--test
      |--test_files
         |--test_data
         |--test_models
   |--pypoetry.toml
   |--README.md
   |--.dvcignore
   |--.gitignore
   |--.gitlab-ci.yml

Short description for the folders and files:

* data
    * raw: Unprocessed and unchanged data.
    * interim: Processed data but not ready for training.
    * processed: Processed data, that is ready for training.
* docs
    * build: Generated documentation. See :ref:`generate_doc`
    * source: Source files for the documentation. See :ref:`write_documentation`
* models: Trained or loaded models are placed here.
* notebooks
    * exploratory: Notebooks for analysis of data or models.
    * reports: Notebooks for showcases, communication with stakeholders.
* {project_code}:
    * api: Predefined REST Server. See :ref:`start_rest_server`
    * preprocessing: Preprocessing to transform the raw data to interim and processed format.
    * scripts: Scripts for ``poetry run`` usage. Predefined are ``gen_doc`` and ``server`` (:ref:`getting_started`). To add and create own scripts see https://python-poetry.org/docs/pyproject/#scripts.
    * configuration.py: See :ref:`convention_over_configuration`
    * main.py
* test: Tests for your project code.
* pypoetry.toml: Configuration file for `poetry <https://python-poetry.org/>`_. Add dependencies, scripts and authors here.
* README.md: :ref:`getting_started` in short.
* .dvcignore: Files and directories ignored by `DVC <https://dvc.org/>`_. DVC is for data versioning.
* .gitignore: Files and directories ignored by `git <https://git-scm.com/>`_. Git is for code versioning.
* .gitlab-ci.yml: Build pipeline for GitLab.

