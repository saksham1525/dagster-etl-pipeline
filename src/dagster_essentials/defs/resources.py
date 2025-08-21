import os
from dagster_duckdb import DuckDBResource
import dagster as dg

database_resource = DuckDBResource(
    database=os.getenv("DUCKDB_DATABASE", "data/staging/data.duckdb")
)

@dg.definitions
def resources():
    return dg.Definitions(resources={"database": database_resource})