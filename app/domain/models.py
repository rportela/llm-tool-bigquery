from typing import List, Optional
from pydantic import BaseModel, Field


class ColumnDTO(BaseModel):
    name: str
    field_type: str
    description: Optional[str] = None


class TableDTO(BaseModel):
    fqid: str = Field(..., description="project.dataset.table")
    description: Optional[str] = None
    columns: List[ColumnDTO] = []


class DatasetDTO(BaseModel):
    name: str
    description: Optional[str] = None
    tables: List[TableDTO] = []


class SQLRequestDTO(BaseModel):
    question: str
    tables: Optional[List[str]] = None  # optional filter
