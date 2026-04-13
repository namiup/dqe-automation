"""
Description: Data Quality checks ...
Requirement(s): TICKET-1234
Author(s): Name Surname
"""

import pytest
from src.connectors.file_system.parquet_reader import ParquetReader

@pytest.fixture(scope='session')
def parquet_reader(request):
    try:
        reader = ParquetReader('/parquet_data/facility_name_min_time_spent_per_visit_date')
        yield reader
    except Exception as e:
        pytest.fail(f"Failed to initialize ParquetReader: {e}")
    finally:
        del reader

@pytest.mark.parquet_data
def test_connect(db_connection):
    df = db_connection.get_data_sql("select count(*) from patients")
    assert df.iloc[0, 0] == 30


@pytest.fixture(scope='module')
def source_data(db_connection):
    source_query = """
    select count(*) from patients
    """
    source_data = db_connection.get_data_sql(source_query)
    return source_data


@pytest.fixture(scope='module')
def target_data(parquet_reader):
    target_path = '/parquet_data/facility_name_min_time_spent_per_visit_date'
    target_data = parquet_reader.process(target_path, include_subfolders=True)
    return target_data


@pytest.mark.parquet_data
def test_check_dataset_is_not_empty(target_data, data_quality_library):
    data_quality_library.check_dataset_is_not_empty(target_data)


@pytest.mark.parquet_data
def test_check_count(source_data, target_data, data_quality_library):
    data_quality_library.check_count(source_data, target_data)
