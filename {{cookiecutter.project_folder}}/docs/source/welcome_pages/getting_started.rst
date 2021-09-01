.. _getting_started:

Getting Started
===============

STAMP 4 NLP is an instantiable and iterative-incremental process model facilitating the development of NLP Applications:

* Uses concepts and best practices of Software Engineering: Agile (Scrum), Continuous Integration and Delivery, Testing
* Supports the collaborative development with business partners
* Focus on business goal
* Standardization facilitates lower settling-in periods
* Provides transparency:
    * Enables project stakeholder not familiar with NLP to follow the development process
    * Defined responsibilities for every task, which minimizes points of conflicts
    * Metrics indicate the application's quality


Prerequisites
-------------

1. Install `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/installation.html>`__ for instantiating the process model and the framework.
2. Install `poetry <https://python-poetry.org/docs/#installation>`__ as dependency manangement and packaging tool for Python projects.

Instantiating STAMP 4 NLP
-------------------------

Run ``cookiecutter .`` in the root directory of the repository to create an instance of STAMP 4 NLP. You will be prompted to provide information about the project:

* Project Name: Name of the project, that will be used for folder names and documentation.
* Short Description: Description of the project, that will be copied in different places in the documentation. It can be changed at any time.
* Project Language: One of spacy's supported language abbreviation (https://spacy.io/usage/models) for downloading and installing the language model.
* Application Type: If already known at project creation time, this helps to generate example code for a first prototype.
* Author: The author, who serves as the project leader or as contact person for the project. At the moment only one author can be added initially. If you want to have several authors mentioned, you have to add them manually in ``pyproject.toml`` (see :ref:`folder_structure`).
* Author E-Mail: Corresponding E-Mail address of the author.

The created instance provides:

* Folder structure: A standardized folder structure. Read more at :ref:`folder_structure`
* Code: Prototypical application fitting matching the application type and a basic REST interface.
* Documentation: For the project content, the process model STAMP 4 NLP and for the code.

Prepare Development Environment
-------------------------------

To use the predefined development environment, run ``poetry install`` in the project folder. All dependencies and scripts described in ``pyproject.toml`` are installed.
Now you are ready for documentation or development: inspect data with jupyter notebooks, create a first baseline or document the results of the :ref:`Goal Specification`.

.. _generate_doc:

Generate Documentation
----------------------

The documentation uses `Sphinx <https://www.sphinx-doc.org/en/master/>`_ with `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ or  `Markdown <https://www.markdownguide.org/>`_.
Thus the documentation has to be converted to html. For this purpose run ``poetry run gen_doc``. The generated documentation can be found at ``docs/build/html/index.html``.
Read :ref:`write_documentation` for how to add your content to this documentation.

.. _start_rest_server:

Start REST Server
-----------------

.. Hint:: You have to implement the endpoint in the api-folder at first!

Run ``poetry run server`` to start a `uvicorn <https://www.uvicorn.org/>`_ server with `fastapi <https://fastapi.tiangolo.com/tutorial/first-steps/>`_.
You can always check the REST-Documentation by starting the server and checking `localhost:8000/docs` in your browser.

