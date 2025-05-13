from fastapi import APIRouter, HTTPException
from typing import List
from .schemas import HistoryEntry
from .service import add_entry, get_all, delete_entry, clear_all

router = APIRouter(prefix="/history", tags=["history"])

@router.get("/", response_model=List[HistoryEntry])
async def list_history():
    return get_all()

@router.post("/", response_model=HistoryEntry)
async def create_history(entry: HistoryEntry):
    # Este endpoint es más de prueba; en la práctica se añadirá desde defined/undefined
    new = add_entry(entry.expression, entry.result, entry.type)
    return new

@router.delete("/{entry_id}", status_code=204)
async def delete_history(entry_id: int):
    deleted = delete_entry(entry_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="History entry not found")
    return

@router.delete("/", status_code=204)
async def clear_history():
    clear_all()
    return
