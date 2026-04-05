import pytest
import re
import os
import csv
import re

def test_file_not_empty():
    file_path = "./PyTest Introduction/src/data/data.csv"
    assert os.path.getsize(file_path) > 0, f"File is empty: {file_path}"

@pytest.mark.validate_csv
def test_validate_schema():
    file_path = "./PyTest Introduction/src/data/data.csv"
    expected_columns = ['id', 'name', 'age', 'email', 'is_active']

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        actual_columns = reader.fieldnames
        assert actual_columns == expected_columns, f"Schema mismatch: {actual_columns} != {expected_columns}"

@pytest.mark.validate_csv
@pytest.mark.skip
def test_age_column_valid():
    file_path = "./PyTest Introduction/src/data/data.csv"  # Update path as needed

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row_num, row in enumerate(reader, start=2):  # start=2 to account for header row
            try:
                age = int(row['age'])
            except (ValueError, KeyError):
                assert False, f"Invalid or missing age value in row {row_num}: {row.get('age')}"
            assert 0 <= age <= 100, f"Age out of range in row {row_num}: {age}"

@pytest.mark.validate_csv
def test_email_column_valid():
    file_path = "./PyTest Introduction/src/data/data.csv"
    email_pattern = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row_num, row in enumerate(reader, start=2):  # start=2 to account for header
            email = row.get('email', '')
            assert email_pattern.match(email), f"Invalid email format in row {row_num}: {email}"

@pytest.mark.validate_csv
@pytest.mark.xfail
def test_duplicates():
    file_path = "./PyTest Introduction/src/data/data.csv"

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    header, *data_rows = rows  # Unpack header and data rows

    unique_rows = set(tuple(row) for row in data_rows)
    assert len(unique_rows) == len(data_rows), "Duplicate rows found in the CSV file"
    
@pytest.mark.parametrize("id, is_active", [
    ("1", "False"),
    ("2", "True")
])
def test_active_players(id, is_active):
    file_path = "./PyTest Introduction/src/data/data.csv"
    found_id = False
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row.get('id') == id:
                found_id = True
                # Accept both boolean and string representations
                assert row.get('is_active') == is_active, f"is_active should be {is_active} for id={id}, got {row.get('is_active')}"
    assert found_id, f"Row with id={id} not found"


def test_active_player():
    id = "1"
    is_active = "True"
    file_path = "./PyTest Introduction/src/data/data.csv"
    found_id = False
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row.get('id') == id:
                found_id = True
                # Accept both boolean and string representations
                assert row.get('is_active') == is_active, f"is_active should be {is_active} for id={id}, got {row.get('is_active')}"
    assert found_id, f"Row with id={id} not found"
