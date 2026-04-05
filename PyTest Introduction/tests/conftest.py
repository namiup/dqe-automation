import pytest
import pandas as pd

# Fixture to read the CSV file
@pytest.fixture
def read_file():
    file_path = "./PyTest Introduction/src/data/data.csv"
    csvfile = open(file_path, newline='')
    reader = csv.DictReader(csvfile)
    yield reader
    csvfile.close()

# Fixture to validate the schema of the file


# Pytest hook to mark unmarked tests with a custom mark
