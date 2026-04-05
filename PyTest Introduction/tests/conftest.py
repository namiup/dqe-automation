import pytest
import csv

file_path = "./PyTest Introduction/src/data/data.csv"
actual_schema = ["id", "name", "age", "email", "is_active"]

@pytest.fixture(scope="session")
def read_file():
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
    return rows

@pytest.fixture(scope="session")
def csv_reader():
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        yield reader

# Fixture to validate the schema of the file
@pytest.fixture(scope="session")
def validate_schema(csv_reader):
    expected_schema = csv_reader.fieldnames
    assert actual_schema == expected_schema, f"Schema mismatch: {actual_schema} != {expected_schema}"

# Pytest hook to mark unmarked tests with a custom mark
