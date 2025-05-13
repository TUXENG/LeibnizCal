# src/defined/router.py
from fastapi import APIRouter, HTTPException
from .schemas import DefinedRequest, IntegralResponse
from .service import solve_defined

router = APIRouter(prefix="/defined", tags=["defined"])

@router.post("/", response_model=IntegralResponse)
async def compute_defined(req: DefinedRequest):
    try:
        res = solve_defined(
            req.expression, 
            req.variable, 
            req.lower_limit, 
            req.upper_limit
            )
        return {
            "input": req.model_dump(), 
            "result": res
            }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
