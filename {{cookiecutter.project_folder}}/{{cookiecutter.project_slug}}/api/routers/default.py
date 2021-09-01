from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def service_is_alive():
    return {"Hello": "World"}


@router.get("/info")
async def service_info():
    return get_service_description()


@router.get("/description")
async def service_description():
    return get_service_description()


def get_service_description():
    return {
        "project_name": "{{cookiecutter.project_name}}",
        "project_slug": "{{cookiecutter.project_slug}}",
        "project_short_description": "{{cookiecutter.project_short_description}}",
        "project_language": "{{cookiecutter.project_language}}",
        "application_type": "{{cookiecutter.application_type}}",
        "project_author": "{{cookiecutter.project_author}}",
        "project_author_email": "{{cookiecutter.project_author_email}}",
    }



