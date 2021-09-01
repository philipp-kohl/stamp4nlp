import tempfile
from cookiecutter.main import cookiecutter
import os
import click


@click.command()
@click.option("-u", "--update", is_flag=True, default=False)
def main(update: bool):
    # Create project from the cookiecutter-pypackage/ template
    config = {
        "project_name": "STAMP Test Run",
        "project_author": "Philipp Kohl",
        "project_author_email": "p.kohl@fh-aachen.de",
        "project_short_description": "<That is a placeholder for the project specific description for which STAMP 4 NLP was instantiated...>"
    }
    dir = cookiecutter('./', no_input=True, extra_context=config,
                       output_dir="/tmp/stamp4nlp-temp-doc/",
                       overwrite_if_exists=True)  # tempfile.mktemp(prefix="stamp4nlp-temp-"))

    print(dir)
    if update:
        os.system(
            f'cd {dir}; poetry update; poetry install; poetry run gen_doc; google-chrome {dir}/docs/build/html/index.html;')
    else:
        os.system(
            f'cd {dir}; poetry install; poetry run gen_doc; google-chrome {dir}/docs/build/html/index.html;')


if __name__ == "__main__":
    main()
