# Dagster ETL Pipeline

A robust and modular ETL pipeline built using Dagster, orchestrating data workflows with asset-based design. It uses:

Dagster for orchestration

DuckDB as the analytical database

Parquet files for raw data storage

# Project Structure:

```
dagster_etl_pipeline/
├── dagster_essentials/        # Dagster assets and jobs
├── data/
│   ├── raw/                   # Contains raw Parquet files (not tracked in repo)
│   └── staging/               # DuckDB file storage (not tracked in repo)
├── .gitignore
├── README.md
└── ...
```

# Missing Files (Not in Repo):

Due to GitHub’s file size limits, the following files are not included in the repository:

data/raw/taxi_trips_2023-03.parquet (~53 MB)

data/staging/data.duckdb (~111 MB)

You will need to download or generate these files manually and place them in the respective folders to run the pipeline locally.

# Getting Started:

Clone the repository:
git clone https://github.com/saksham1525/dagster-etl-pipeline.git
cd dagster-etl-pipeline

Set up a virtual environment:
python -m venv .venv
source .venv/bin/activate (On Windows: .venv\Scripts\activate)
pip install -r requirements.txt

Add the required data files:
Place the .parquet and .duckdb files in the appropriate folders as mentioned above.

Start the Dagster development UI:
dagster dev

Then go to: http://localhost:3000

Deployment:

This project can be deployed to Dagster Cloud. Follow their official documentation for setup and CI/CD pipelines.

# Credits:

Originally based on the Dagster University “Dagster Essentials” tutorial, but customized for broader ETL use cases.

# License:

MIT License
