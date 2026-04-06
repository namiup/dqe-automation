import pytest
import csv

def pytest_addoption(parser):
    parser.addoption(
        "--file_path", action="store", help="Path to csv file"
    )
    parser.addoption(
        "--actual_schema", action="store", help="Expected actual schema"
    )

@pytest.fixture(scope="session")
def read_file(request):
    file_path = request.config.getoption("--file_path")
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
    return rows

@pytest.fixture(scope="session")
def csv_reader(request):
    file_path = request.config.getoption("--file_path")
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        yield reader

# Fixture to validate the schema of the file
@pytest.fixture(scope="session")
def validate_schema(csv_reader, request):
    schema_str = request.config.getoption("--actual_schema")
    actual_schema = [s.strip() for s in schema_str.split(",")]
    expected_schema = csv_reader.fieldnames
    assert actual_schema == expected_schema, f"Schema mismatch: {actual_schema} != {expected_schema}"

# Pytest hook to mark unmarked tests with a custom mark
def pytest_collection_modifyitems(config, items):
    for item in items:
        if not list(item.iter_markers()):
            item.add_marker("unmarked")
