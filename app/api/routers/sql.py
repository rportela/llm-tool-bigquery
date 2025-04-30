from fastapi import APIRouter, Depends
from ..deps import sql_generator_dep
from ...domain.models import SQLRequestDTO

router = APIRouter(prefix="/openai-tools", tags=["sql"])


@router.post("/generate_sql")
async def generate_sql(req: SQLRequestDTO, svc=Depends(sql_generator_dep)):
    return {"sql": await svc.generate_sql(req)}
