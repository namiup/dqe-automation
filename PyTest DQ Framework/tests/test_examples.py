"""
Description: Data Quality checks ...
Requirement(s): TICKET-1234
Author(s): Name Surname
"""

import pytest


@pytest.mark.parquet_data
def test_connect(db_connection):
    df = db_connection.get_data_sql("select * from patients")
    assert len(df) == 30


@pytest.fixture(scope='module')
def source_data(db_connection):
    source_query = """
    select * from patients
    """
    source_data = db_connection.get_data_sql(source_query)
    return source_data



