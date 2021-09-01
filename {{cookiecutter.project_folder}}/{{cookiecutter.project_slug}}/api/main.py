import uvicorn
import click
from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.staticfiles import StaticFiles

#TODO adapt for use case
from {{cookiecutter.project_slug}}.api.routers import predict, default


app = FastAPI()
# add all models from the models directory
app.mount("/static", StaticFiles(directory="models"), name="static")


async def get_token_header(x_token: str = Header(...)):
    if x_token != "default_token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")

app.include_router(
    predict.router,
    prefix="/predict",
    tags=["predict"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}}
)

app.include_router(
    default.router,
    prefix="",
    tags=["default", "info", "description"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}}
)


@click.command()
@click.option("--host", default="127.0.0.1", show_default=True)
@click.option("--port", default=8000, show_default=True, type=int)
def main(host, port):
    """
    Calls a subprocess starting the server in the 'catalog_integration_framework' directory
    """
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()
