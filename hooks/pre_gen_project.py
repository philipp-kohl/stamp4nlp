# cookiecutter do not support local imports at the moment: https://github.com/cookiecutter/cookiecutter/issues/824
# checks.py
import sys
import re


def error_exit(error: str):
    print(error)
    sys.exit(1)


def check_author(pro_author: str):
    if not pro_author or len(pro_author) < 2:
        error_exit("ERROR: Please enter a valid Author")


def check_email(pro_auth_email: str):
    email_regex = r'[^@]+@[^@]+\.[^@]+'

    if not re.match(email_regex, pro_auth_email) or ' ' in pro_auth_email:
        error_exit(f"ERROR: {pro_auth_email} is not a valid email address")


if __name__ == '__main__':
    project_author = '{{cookiecutter.project_author}}'
    project_auth_email = '{{cookiecutter.project_author_email}}'

    check_author(project_author)
    check_email(project_auth_email)
