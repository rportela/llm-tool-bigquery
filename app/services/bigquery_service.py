from typing import List
from ..domain.models import DatasetDTO, TableDTO
from ..infrastructure.bigquery_client import BigQueryClient


class BigQueryService:
    """High-cohesion façade: every BQ read operation lives here."""

    def __init__(self, client: BigQueryClient):
        self.client = client

    def list_datasets(self) -> List[DatasetDTO]:
        return [DatasetDTO(name=d.dataset_id) for d in self.client.list_datasets()]

    def list_tables(self, dataset: str) -> List[TableDTO]:
        return [
            TableDTO(fqid=f"{t.project}.{t.dataset_id}.{t.table_id}")
            for t in self.client.list_tables(dataset)
        ]

    def get_table_schema(self, table: str) -> TableDTO:
        tbl = self.client.get_table(table)
        return TableDTO(
            fqid=table,
            description=tbl.description,
            columns=[
                dict(name=f.name, field_type=f.field_type, description=f.description)
                for f in tbl.schema
            ],
        )
