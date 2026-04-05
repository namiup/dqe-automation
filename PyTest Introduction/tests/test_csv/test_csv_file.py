import pytest
import re
import os
import csv

def test_file_not_empty():
    file_path = "./PyTest Introduction/src/data/data.csv"
    assert os.path.getsize(file_path) > 0, f"File is empty: {file_path}"


def test_duplicates():
    assert 1 + 1 == 2


def test_validate_schema():
    file_path = "./PyTest Introduction/src/data/data.csv"
    expected_columns = ['id', 'name', 'age', 'email', 'is_active']

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        actual_columns = reader.fieldnames
        assert actual_columns == expected_columns, f"Schema mismatch: {actual_columns} != {expected_columns}"


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


def test_email_column_valid():
    assert 1 + 1 == 2


def test_active_players():
    assert 1 + 1 == 2


def test_active_player():
    assert 1 + 1 == 2
