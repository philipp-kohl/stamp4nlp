import pytest

from hooks.pre_gen_project import check_author, check_email


def test_pre_gen_project_hook():
    check_email("test@pytest.test")
    check_author("pytest")


def test_pre_gen_project_author_not_working():
    does_not_work = ["A"]
    for author in does_not_work:
        with pytest.raises(SystemExit) as pytest_exit:
            check_author(author)
            assert pytest_exit.value.code == 1


def test_pre_gen_project_email_should_work():
    works = ["py.test@pytest.de",
             "pytest@pytest.de",
             "py.test@fh-aachen.de",
             "py.test@p.y.t.e.s.t",
             "p@y.t",
             "p.y.t.e.s.t@p.y.t.e.s.t"]
    for email in works:
        check_email(email)


def test_pre_gen_project_email_not_working():
    does_not_work = ["pytest@pytestde",
                     "@pytest.de",
                     "py.test@de",
                     "pytest@pytest@pytest.de",
                     "pytest@pytest.@de",
                     "pytest@pytest.de pytest@pytestde"]
    for email in does_not_work:
        with pytest.raises(SystemExit) as pytest_exit:
            check_email(email)
            assert pytest_exit.value.code == 1


