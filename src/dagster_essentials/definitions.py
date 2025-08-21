from pathlib import Path
from dotenv import load_dotenv

from dagster import definitions, load_from_defs_folder

# Load environment variables from .env file
load_dotenv()


@definitions
def defs():
    return load_from_defs_folder(project_root=Path(__file__).parent.parent.parent)
