"""
Description: Data Quality checks ...
Requirement(s): TICKET-1234
Author(s): Name Surname
"""

import pytest

@pytest.fixture
def target_path():
    return '/parquet_data/facility_name_min_time_spent_per_visit_date'

@pytest.mark.parquet_data
def test_check_dataset_is_not_empty(target_data, data_quality_library):
    data_quality_library.check_dataset_is_not_empty(target_data(target_path))
