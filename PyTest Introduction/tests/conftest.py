import pytest
import pandas as pd

# Fixture to read the CSV file
@pytest.fixture.get_file():
  file_path = "./PyTest Introduction/src/data/data.csv"
  return file_path

# Fixture to validate the schema of the file


# Pytest hook to mark unmarked tests with a custom mark
