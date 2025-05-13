# src/undefined/router.py
from fastapi import APIRouter, HTTPException
from .schemas import UndefinedRequest, IntegralResponse
from .service import solve_undefined

router = APIRouter(prefix="/undefined", tags=["undefined"])

@router.post("/", response_model=IntegralResponse)
async def compute_undefined(req: UndefinedRequest):
    try:
        res = solve_undefined(req.expression, req.variable)
        return {"input": req.model_dump(), "result": res}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
