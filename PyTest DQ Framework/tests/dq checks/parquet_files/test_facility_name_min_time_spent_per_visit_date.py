"""
Description: Data Quality checks ...
Requirement(s): TICKET-1234
Author(s): Name Surname
"""

import pytest

@pytest.mark.parquet_data
def test_check_dataset_is_not_empty(test_facility_data, data_quality_library):
    data_quality_library.check_dataset_is_not_empty(test_facility_data)
