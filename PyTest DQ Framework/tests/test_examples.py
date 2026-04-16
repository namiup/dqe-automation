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
