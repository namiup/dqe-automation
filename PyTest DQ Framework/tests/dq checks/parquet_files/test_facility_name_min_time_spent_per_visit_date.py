"""
Description: Data Quality checks ...
Requirement(s): TICKET-1234
Author(s): Name Surname
"""

import pytest

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
    """
    source_data = db_connection.get_data_sql(source_query)
    return source_data

@pytest.fixture(scope='module')
def test_facility_data(target_data_factory):
    path = '/parquet_data/facility_name_min_time_spent_per_visit_date'
    target_data = target_data_factory(path)
    return target_data


@pytest.mark.parquet_data
def test_check_dataset_is_not_empty(test_facility_data, data_quality_library):
    data_quality_library.check_dataset_is_not_empty(test_facility_data)


@pytest.mark.parquet_data
def test_check_duplicates(test_facility_data, data_quality_library):
    data_quality_library.check_duplicates(test_facility_data)

@pytest.mark.parquet_data
def test_check_count(source_data, test_facility_data, data_quality_library):
    data_quality_library.check_count(source_data, test_facility_data)

@pytest.mark.parquet_data
def test_check_not_null_values(target_data, data_quality_library):
    data_quality_library.check_not_null_values(target_data, ['facility_name','visit_date','min_time_spent'])
