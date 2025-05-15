from typing import List
from .schemas import HistoryEntry
from datetime import datetime, timezone

# Almacenamiento en memoria (reemplazar por DB si se desea)
_history: List[HistoryEntry] = []
_next_id = 1

def add_entry(expression: str, result: str, type_: str) -> HistoryEntry:
    global _next_id, _history
    entry = HistoryEntry(
        id=_next_id,
        expression=expression,
        result=result,
        type=type_,
        timestamp=datetime.now(timezone.utc)
    )
    _history.append(entry)
    _next_id += 1
    return entry

def get_all() -> List[HistoryEntry]:
    # Devolver copia para evitar modificaciones externas
    return list(_history)

def delete_entry(entry_id: int) -> bool:
    global _history
    original_len = len(_history)
    _history = [e for e in _history if e.id != entry_id]
    return len(_history) < original_len

def clear_all() -> None:
    global _history, _next_id
    _history = []
    _next_id = 1
