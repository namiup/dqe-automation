"""
Description: Data Quality checks ...
Requirement(s): TICKET-1234
Author(s): Name Surname
"""

import pytest

@pytest.mark.parquet_data
def test_check_dataset_is_not_empty(target_data, data_quality_library):
    target_path = '/parquet_data/facility_name_min_time_spent_per_visit_date'
    data_quality_library.check_dataset_is_not_empty(target_data(target_path))
