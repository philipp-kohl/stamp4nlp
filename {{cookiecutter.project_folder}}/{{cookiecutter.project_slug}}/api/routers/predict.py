from fastapi import APIRouter, HTTPException, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Dict

from io import StringIO
import pandas as pd

router = APIRouter()


class ModelPredictionData(BaseModel):
    name: str  # Name is required
    description: str = None  # Default is None, NOT required
    """
    Data can have a fixed random number of columns and each column has a list of string data 
    (Which can be empty strings).
    Data is required 
    """
    data: Dict[str, List[str]]


@router.post("/data")
async def predict_json(data: ModelPredictionData):
    """
    This function does a model prediction based on json-contents

    Args:
        data: json content of the rest post
    """
    try:
        df: pd.DataFrame = pd.DataFrame.from_dict(data.data)
    except ValueError as e:
        if str(e) != "arrays must all be same length":  # pandas couldn't convert due to different lengths
            raise e
        content = {"description": "arrays must all be same length"}
        return JSONResponse(status_code=422, content=content)

    return predict_dataframe(df)


@router.post("/file")
async def predict_file(file: UploadFile = File(...), sep=";"):
    """
    EXAMPLE on how to predict with csv files
    This function does a model prediction based on a csv-file

    Args:
        file: a csv file send with REST
        sep: separator of the csv file, default argument is a semicolon
    """
    # TODO: change this to allow other file types
    if file.content_type != "text/csv":
        raise HTTPException(status_code=400, detail="Invalid content type")

    # read the content
    contents = str(await file.read(), 'utf-8')

    # TODO change this to your usecase, this converts the content of a csv file to a dataframe
    df = pd.read_csv(StringIO(contents), sep=sep, dtype=str, na_values="")

    return predict_dataframe(df)


def predict_dataframe(df: pd.DataFrame):
    # TODO change this to your wrapped model
    # res = my_model.predict(df)
    # placeholder:
    res = df.to_dict()
    return res
