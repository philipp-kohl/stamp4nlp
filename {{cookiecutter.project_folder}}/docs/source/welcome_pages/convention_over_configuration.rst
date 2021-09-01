.. _convention_over_configuration:

Convention over Configuration
=============================

Convention over Configuration is a software design paradigm to keep configurations as simple as possible and support the user to stay focused in his goal without forcing the user to make many decisions in the beginning.
Standard configurations serve as the conventions the user can alter on demand. Staying with conventions and standards helps to communicate and collaborate with colleagues.

Conventions used by STAMP 4 NLP:

* Folder Structure: See :ref:`folder_structure`
* Development Environment: based on spaCy, Scikit-learn and jupyter notebook
* Documentation: for the process model and project

Alter Configuration
-------------------
Altering configuration can confuse colleagues but can be a benefit. Thus, inform your colleagues and document why you do not stick with the standard under ``docs/source/instance_specific_content/convention_changes.rst``.

* Folder Structure: Change the folder structure as desired. Keep in mind that code has to be changed as well (save/load location). To minimize the changes you can use the variables in ``{project_code}/configuration.py``.
* Development Environment: The user can add other dependencies in ``pyproject.toml`` or switch the data science stack to `Pytorch <https://pytorch.org/>`_ or `AllenNLP <https://allennlp.org/>`_.
* Documentation: Change the documentation as desired.
