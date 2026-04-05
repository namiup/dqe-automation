import pytest
import csv

file_path = "./PyTest Introduction/src/data/data.csv"
actual_schema = [["id", "name", "age", "email", "is_active"]]

@pytest.fixture
def read_file():
    """Returns a list of all rows (dicts) for repeated use in tests."""
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
    return rows

@pytest.fixture
def csv_reader():
    """Returns a fresh DictReader (iterator) for tests that need it."""
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        yield reader  # Use yield so the file stays open during the test

# Fixture to validate the schema of the file
@pytest.fixture(scope="session", params=actual_schema)
def validate_schema(read_file):
    actual_schema = request.param
    expected_schema = read_file.fieldnames
    assert actual_schema == expected_schema, f"Schema mismatch: {actual_schema} != {expected_schema}"

# Pytest hook to mark unmarked tests with a custom mark
