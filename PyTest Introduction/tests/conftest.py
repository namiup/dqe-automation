import pytest
import csv

file_path = ["./PyTest Introduction/src/data/data.csv"]
actual_schema = [["id", "name", "age", "email", "is_active"]]

# Fixture to read the CSV file
@pytest.fixture(scope="session", params=file_path)
def read_file():
    csvfile = open(file_path, newline='')
    reader = csv.DictReader(csvfile)
    yield reader
    csvfile.close()

# Fixture to validate the schema of the file
@pytest.fixture(scope="session", params=actual_schema)
def validate_schema(read_file):
    actual_schema = request.param
    expected_schema = read_file.fieldnames
    assert actual_schema == expected_schema, f"Schema mismatch: {actual_schema} != {expected_schema}"

# Pytest hook to mark unmarked tests with a custom mark
