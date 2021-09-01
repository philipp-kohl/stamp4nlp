.. _write_documentation:

Write Your Documentation
========================

The documentation is written with `Sphinx <https://www.sphinx-doc.org/en/master/>`_. You can use `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ or `Markdown <https://www.markdownguide.org/>`_.
You can also switch between reStructuredText and Markdown from file to file but cannot use both in one file. For Markdown support read :ref:`inlcude_markdown` and https://myst-parser.readthedocs.io/en/latest/sphinx/intro.html.

To change or add documentation go to the ``docs/source`` folder (:ref:`folder_structure`). Here are different files and folders:

* _data: YAML files for describing different elements (artifacts, roles, subprocesses, tasks and role assignment). In combination with _datatemplates pages are rendered in a standard way. See `sphinx-contrib/datatemplates <https://github.com/sphinx-contrib/datatemplates>`_. In this way it is possible to automatically extract specific information.
* _datatemplates: reStructuredText templates with `jinja <https://jinja.palletsprojects.com/en/3.0.x/templates/>`_ logic to model pages for artifacts, roles, subprocesses, taks and role assignment. Change these files for other appearance. Add new files for new pages, which should behave in the same way.
* _static: Images, graphs, static HTML, CSS or JavaScript goes here.
* _templates: Templates for Sphinx. See https://www.sphinx-doc.org/en/master/templating.html.
* code: Documentation for the project code. At the moment `autosummary <https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html>`_ is used, but can changed as desired.
* instance_specific_content: Project related information should be documented here.
* process_model: The documentation of STAMP 4 NLP as process model is delivered with every project instance. Results of specific tasks can be documented in the corresponding artifacts pages (see :ref:`add_info_to_artifacts`). Thus, artifacts are shared between general process model description and project specific content.
* welcome_pages: The Getting Started for STAMP 4 NLP. Do not use these pages for your own project related Getting Started. Use ``instance_specific_content/project_getting_started`` for this purpose.
* conf.py: Configuration file for Sphinx.
* index.rst: Root document. Use this to include new pages to the main toctree.

The most important parts for adding documentation are:

* ``_data/artifacts`` or ``process_model/artifacts`` to persist results accordingly to the process model.
* ``instance_specific_content/`` for adding own pages (see :ref:`create_own_pages`)
* ``index.rst`` to add own pages to the toctree


Generate Documentation
----------------------

See :ref:`generate_doc`.

.. _create_own_pages:

Create Own Pages
----------------
Creating a new page to address a specific project-related topic supports clarity and comprehensibility. You can use reStructuredText or Markdown for your pages.
You can reference these pages from artifacts or other subpages to prevent cluttering content.

Include reStructuredText
^^^^^^^^^^^^^^^^^^^^^^^^

Including reStructuredText (.rst) files to the doctree. For example in ``index.rst``:

.. parsed-literal::

   .. toctree::
      :maxdepth: 2
      :caption: Project documentation

      instance_specific_content/instance_specific_content.rst
      instance_specific_content/project_getting_started.rst
      instance_specific_content/role_assignment.rst
      instance_specific_content/dependencies.rst
      process_model/artifacts.rst
      instance_specific_content/your_new_page.rst               <- Your new page added to the doctree


.. _inlcude_markdown:

Include Markdown
^^^^^^^^^^^^^^^^

Including Markdown pages is as easy as including reStructuredText (.rst) files. Add your Markdown file to the doctree.
For example in ``index.rst``:

.. parsed-literal::

   .. toctree::
      :maxdepth: 2
      :caption: Project documentation

      instance_specific_content/instance_specific_content.rst
      instance_specific_content/project_getting_started.md      <-- E.g. use your README.md as project getting started
      instance_specific_content/role_assignment.rst
      instance_specific_content/dependencies.rst
      process_model/artifacts.rst

To reference markdown files from rst you have to use the ``eval-rst`` environment in your markdown file:

.. code-block::

    ```{eval-rst}
    .. _<your-target>:
    ```

Reference Pages
^^^^^^^^^^^^^^^

Sphinx uses the following Syntax to create an anchor (see `Doc <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#ref-role>`_):

.. parsed-literal::

   .. _<YOUR_REF_LABEL>:
   Section to Reference
   --------------------

To reference this section:

.. parsed-literal::

   lorem ipsum `:ref:`YOUR_REF_LABEL``

.. _add_info_to_artifacts:

Add Information to Artifacts
----------------------------

Artifacts represent results from tasks. Thus, they offer the opportunity to document the results directly into the process model's artifacts (:ref:`artifacts`). In this way artifacts provide information about the general process model and the project-specific results.
There are 3 types to add information to artifacts:

Add Content Directly to Artifact's Page
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open the corresponding artifact file under ``docs/source/process_model/artifacts/`` to add reStructuredText to it. E.g., the ``Annotation Guidelines`` have the following content:

.. parsed-literal::

   .. datatemplate:yaml:: ../../_data/artifacts/annotation_guidelines.yaml
   :template: artifact.tmpl

See ``_data`` and ``_datatemplates`` under :ref:`folder_structure` for information of these two lines of code.
After these lines you can add your own reStructuredText to document your results.

Create a New Page and Add Reference
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Encapsulating topics to their own pages helps to keep the overview of the results and dig deeper on demand. Therefore you can create your own page and reference it in your artifact's file.
E.g., adding Annotation Guidelines as a new page to the artifact.

``docs/source/process_model/artifacts/annotation_guideleines.rst``:

.. parsed-literal::

   .. datatemplate:yaml:: ../../_data/artifacts/annotation_guidelines.yaml
   :template: artifact.tmpl
   .. include:: <Path to File>                <- 1. Option https://docutils.sourceforge.io/docs/ref/rst/directives.html#include
   See `:ref:`project_annotation_guidelines`` <- 2. Option

``docs/source/instance_specific_content/project_annotation_guideleines.rst``:

.. parsed-literal::

   .. _project_annotation_guidelines:
   Annotation Guidelines
   ---------------------
   Content...

Add Machine Readable Content
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adding machine readable content to artifacts can help to use these values as input for your code. E.g., machine learning metrics can serve as benchmark in this way.
To add machine readable content open the corresponding artifact file under ``docs/source/data/`` (see ``_data`` and ``_datatemplates`` under :ref:`folder_structure` for information about this folder and the underlying concept).
Now add a new `key` ``instance_specific`` at the bottom and add your key and value pairs in YAML format.

.. parsed-literal::

   ---
   name: Machine Learning Requirements
   description: ...
   instance_specific:
     ner-recall: 0.85
     ner-precision: 0.85
     ner-f1: 0.85

These values can be read with ``read_values_from_yaml(file)`` from ``{project_code}/configuration.py``.

