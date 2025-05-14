from fastapi import APIRouter
from .schemas import IntegralRequest, IntegralResponse
from .service import solve_undefined_integral

router = APIRouter(prefix="/undefined", tags=["undefined"])

@router.post("/", response_model=IntegralResponse)
def integrate(data: IntegralRequest):
    return solve_undefined_integral(data)
