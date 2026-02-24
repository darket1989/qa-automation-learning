import os
from pathlib import Path
import pytest
from dotenv import load_dotenv
import json

# Load json file for login
@pytest.fixture(scope="session")
def users():
    """
    Loads testData/users.json and returns a dict.
    Accessible in any test as the 'users' fixture.
    """
    root = Path(__file__).parent.parent  # go from /tests to project root
    data_path = root / "testData" / "users.json"
    with data_path.open(encoding="utf-8") as f:
        return json.load(f)

#Environment variables for login
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")
@pytest.fixture(scope="session")
def creds():
    """
    Provides credentials from environment variables.
    Fails early with a clear message if missing.
    """
    user = os.getenv("user")
    pwd = os.getenv("password")
    if not user or not pwd:
        raise RuntimeError("Missing USERNAME/PASSWORD in environment. ")
    return {"valid_user": user, "pwd": pwd}