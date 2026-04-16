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
        SELECT
        f.facility_name,
        v.visit_timestamp::date AS visit_date,
        MIN(v.duration_minutes) AS min_time_spent
    FROM
        visits v
    JOIN facilities f 
        ON f.id = v.facility_id
    GROUP BY
        f.facility_name,
        visit_date
    UNION ALL  -- misstake
    SELECT
        f.facility_name,
        v.visit_timestamp::date AS visit_date,
        MIN(v.duration_minutes) AS min_time_spent
    FROM
        visits v
    JOIN facilities f 
        ON f.id = v.facility_id
    WHERE
        f.facility_type = 'Clinic' 
    GROUP BY
        f.facility_name,
        visit_date
    """
    source_data = db_connection.get_data_sql(source_query)
    return source_data



