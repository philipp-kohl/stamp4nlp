import subprocess
import {{cookiecutter.project_slug}}.configuration as conf
from pathlib import Path
import sys


def main():
    source_path = Path(conf.docs_source).resolve()
    build_path = Path(conf.docs_build).resolve()

    print('source: ', source_path)
    print('build: ', build_path)

    try:
        subprocess.run("sphinx-build -M clean {} {}".format(source_path, build_path), shell=True, check=True)
        subprocess.run("sphinx-build -M html {} {}".format(source_path, build_path), shell=True, check=True)
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)


if __name__ == "__main__":
    main()
