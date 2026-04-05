import pytest
import csv

# Fixture to read the CSV file
@pytest.fixture(scope="session")
def read_file():
    file_path = "./PyTest Introduction/src/data/data.csv"
    csvfile = open(file_path, newline='')
    reader = csv.DictReader(csvfile)
    yield reader
    csvfile.close()

# Fixture to validate the schema of the file
@pytest.fixture(scope="session")
def validate_schema(actual_schema, expected_schema):

# Pytest hook to mark unmarked tests with a custom mark
