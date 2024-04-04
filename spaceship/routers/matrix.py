from fastapi import APIRouter
from pydantic import BaseModel
import numpy as np

router = APIRouter()

class Matrix(BaseModel):
    matrix1: list
    matrix2: list
    result: list

@router.get('', response_model=Matrix)
def read_matrix():
    matrix1 = np.random.rand(10, 10)
    matrix2 = np.random.rand(10, 10)

    result = np.dot(matrix1, matrix2)

    return {"matrix1": matrix1.tolist(), "matrix2": matrix2.tolist(), "result": result.tolist()}
