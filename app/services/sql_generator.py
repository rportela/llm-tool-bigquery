from ..domain.models import SQLRequestDTO
from ..infrastructure.openai_client import OpenAIClient


class SQLGeneratorService:
    def __init__(self, openai_client: OpenAIClient):
        self.ai = openai_client

    async def generate_sql(self, req: SQLRequestDTO) -> str:
        prompt = self._build_prompt(req)
        return await self.ai.chat(prompt)

    @staticmethod
    def _build_prompt(req: SQLRequestDTO) -> str:
        # pure logic — no IO
        tbl_hint = "\n".join(f"-- {t}" for t in req.tables or [])
        return f"""-- BigQuery StandardSQL
