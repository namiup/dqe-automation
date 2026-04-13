"""
Description: Data Quality checks ...
Requirement(s): TICKET-1234
Author(s): Name Surname
"""

import pytest

@pytest.fixture(scope='module')
def test_facility_data(target_data_factory):
    path = '/parquet_data/facility_name_min_time_spent_per_visit_date'
    target_data = target_data_factory(path)
    return target_data


@pytest.mark.parquet_data
def test_check_dataset_is_not_empty(test_facility_data, data_quality_library):
    data_quality_library.check_dataset_is_not_empty(test_facility_data)


# @pytest.mark.parquet_data
# def test_check_count(source_data, test_facility_data, data_quality_library):
#     data_quality_library.check_count(source_data, test_facility_data)
