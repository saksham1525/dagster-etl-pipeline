# Dagster ETL Pipeline

An ETL pipeline built with Dagster for processing NYC taxi trip data with automated data ingestion, transformations, and analytics.

## Architecture

- **Orchestration**: Dagster with asset-based design
- **Database**: DuckDB for analytical processing  
- **Storage**: Parquet files for raw data
- **Visualization**: GeoPandas + Matplotlib
- **Scheduling**: Time-based and event-driven execution

## Data Sources

The pipeline automatically downloads:

- **NYC Taxi Trips** (2023-01 to 2023-03): `https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{YYYY-MM}.parquet`
- **NYC Taxi Zones**: `https://community-engineering-artifacts.s3.us-west-2.amazonaws.com/dagster-university/data/taxi_zones.csv`

## Quick Start

### Prerequisites
- Python 3.9-3.12
- Git

### Recommended Setup

```bash
git clone <your-repo-url>
cd dagster-etl-pipeline

# Automated setup (creates venv + installs dependencies)
python3 setup.py

# Activate environment and start
source venv/bin/activate
dagster dev
```

### Manual Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start Dagster UI
dagster dev
```

Access the Dagster UI at: http://localhost:3000

## Project Structure

```
src/dagster_essentials/
├── definitions.py           # Main entry point
└── defs/
    ├── assets/              # Data transformation logic
    ├── jobs.py              # Execution workflows
    ├── schedules.py         # Automated scheduling
    ├── sensors.py           # Event-driven execution
    ├── resources.py         # Database connections
    └── partitions.py        # Time-based partitioning
```

## Features

### Automated Workflows
- **Monthly Updates**: Downloads new taxi data (5th of each month)
- **Weekly Analytics**: Generates trip statistics (every Monday)  
- **On-Demand Analysis**: Custom borough reports via JSON requests

### Data Processing Flow
1. Downloads raw Parquet and CSV files
2. Loads into DuckDB with cleaned schema
3. Aggregates trips by time periods and geography
4. Generates maps and analytical charts

### Custom Analysis
Create JSON files in `data/requests/` directory:

```json
{
    "start_date": "2023-01-10",
    "end_date": "2023-01-25", 
    "borough": "Manhattan"
}
```

Results saved to `data/outputs/`.

## Configuration

**Time Range**: 2023-01-01 to 2023-04-01  
**Database**: `data/staging/data.duckdb`  
**Boroughs**: Manhattan, Brooklyn, Queens, Bronx, Staten Island

**Schedules**:
- Trip Updates: `0 0 5 * *` (Monthly)
- Weekly Analytics: `0 0 * * 1` (Monday)