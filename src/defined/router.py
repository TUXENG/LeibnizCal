from fastapi import APIRouter, Request, HTTPException
from fastapi.templating import Jinja2Templates
from src.config import settings
from .schemas import DefinedIntegralRequest
from .service import resolver_integral_definida

router = APIRouter()
templates = Jinja2Templates(directory="src/templates")

@router.get("/defined", name="defined.compute_defined")
async def defined_form(request: Request):
    # Simplemente muestra el formulario vacío
    return templates.TemplateResponse(
        "defined.html",
        {
            "request": request,
            "settings": settings,
            "active_tab": "defined",
            "result": None
        }
    )

@router.post("/defined", name="defined.compute_defined")
async def compute_defined(request: Request, form: DefinedIntegralRequest):
    try:
        res = resolver_integral_definida(
            form.expression, 
            form.variable, 
            form.lower_limit, 
            form.upper_limit
            )
    except ValueError as e:
        raise HTTPException(400, detail=str(e))

    return templates.TemplateResponse(
        "defined.html",
        {
            "request": request,
            "settings": settings,
            "active_tab": "defined",
            "result": res
        }
    )
