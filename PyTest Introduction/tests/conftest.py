import pytest
import pandas as pd

# Fixture to read the CSV file
@pytest.fixture
def read_file():
  file_path = "./PyTest Introduction/src/data/data.csv"
      with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
  return reader

# Fixture to validate the schema of the file


# Pytest hook to mark unmarked tests with a custom mark
