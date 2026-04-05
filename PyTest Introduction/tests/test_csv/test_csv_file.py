import pytest
import re

def test_file_not_empty(read_file):
    assert len(read_file) > 0, f"File is empty: {file_path}"

@pytest.mark.validate_csv
def test_validate_schema(csv_reader):
    expected_columns = ['id', 'name', 'age', 'email', 'is_active']
    actual_columns = csv_reader.fieldnames
    assert actual_columns == expected_columns, f"Schema mismatch: {actual_columns} != {expected_columns}"

@pytest.mark.validate_csv
@pytest.mark.skip
def test_age_column_valid(read_file):
    for row in read_file:
        try:
            age = int(row['age'])
        except (ValueError, KeyError):
            assert False, f"Invalid or missing age value in row {row_num}: {row.get('age')}"
        assert 0 <= age <= 100, f"Age out of range in row {row_num}: {age}"

@pytest.mark.validate_csv
def test_email_column_valid(read_file):
    email_pattern = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
    for row in read_file
        email = row.get('email', '')
        assert email_pattern.match(email), f"Invalid email format in row {row_num}: {email}"

@pytest.mark.validate_csv
@pytest.mark.xfail
def test_duplicates(read_file):
    rows = list(read_file)
    header, *data_rows = rows  # Unpack header and data rows
    unique_rows = set(tuple(row) for row in data_rows)
    assert len(unique_rows) == len(data_rows), "Duplicate rows found in the CSV file"
    
@pytest.mark.parametrize("id, is_active", [
    ("1", "False"),
    ("2", "True")
])
def test_active_players(id, is_active, read_file):
    found_id = False
    for row in read_file:
        if row.get('id') == id:
            found_id = True
            assert row.get('is_active') == is_active, f"is_active should be {is_active} for id={id}, got {row.get('is_active')}"
    assert found_id, f"Row with id={id} not found"


def test_active_player(read_file):
    id = "2"
    is_active = "True"
    found_id = False
    for row in read_file:
        if row.get('id') == id:
            found_id = True
            assert row.get('is_active') == is_active, f"is_active should be {is_active} for id={id}, got {row.get('is_active')}"
    assert found_id, f"Row with id={id} not found"
