{{cookiecutter.project_name}} Documentation
=================================================================

{{cookiecutter.project_short_description}}

Documentation Usage
-------------------

This documentation covers several topics:

* For not STAMP 4 NLP familiar users: :ref:`getting-started`
* The general STAMP 4 NLP process: :ref:`stamp4nlp-doc`
* The project specific content: :ref:`project-doc`
* And the project code documentation: :ref:`project-code-doc`

The NLP Process Model facilitates the structured, transparent, instantiable and collaborative development of a NLP application in cooperation with a business partner.
It is based on a metric-driven approach to measure its quality and its progress, that is made over iterations. The process model includes agile components like iterative and incremental methods with opportunity to goal refinement.

.. _getting-started:
.. toctree::
   :maxdepth: 1
   :caption: STAMP 4 NLP Getting Started

   welcome_pages/getting_started.rst
   welcome_pages/folder_structure.rst
   welcome_pages/write_documentation.rst
   welcome_pages/convention_over_configuration.rst

.. raw:: html
   :file: _static/Overview_index.html

.. _stamp4nlp-doc:
.. toctree::
   :maxdepth: 2
   :caption: STAMP 4 NLP Documentation

   process_model/subprocesses.rst
   process_model/roles.rst
   process_model/artifacts.rst
   process_model/tasks.rst

.. _project-doc:
.. toctree::
   :maxdepth: 2
   :caption: {{cookiecutter.project_name}} documentation

   instance_specific_content/instance_specific_content.rst
   instance_specific_content/project_getting_started.rst
   instance_specific_content/convention_changes.rst
   instance_specific_content/role_assignment.rst
   instance_specific_content/dependencies.rst
   process_model/artifacts.rst

.. _project-code-doc:
.. toctree::
   :maxdepth: 2
   :caption: Code Documentation

   code/auto_doc.rst




