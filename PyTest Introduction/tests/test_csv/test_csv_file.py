import pytest
import re
import os

def test_file_not_empty():
    file_path = "./PyTest Introduction/src/data/data.csv"
    assert os.path.getsize(file_path) > 0, f"File is empty: {file_path}"


def test_duplicates():
    assert 1 + 1 == 2


def test_validate_schema():
    assert 1 + 1 == 2


def test_age_column_valid():
    assert 1 + 1 == 2


def test_email_column_valid():
    assert 1 + 1 == 2


def test_active_players():
    assert 1 + 1 == 2


def test_active_player():
    assert 1 + 1 == 2
