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
        reader = ParquetReader(None)
        yield reader
    except Exception as e:
        pytest.fail(f"Failed to initialize ParquetReader: {e}")
    finally:
        del reader

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


@pytest.fixture(scope='module')
def target_data_factory(parquet_reader):
    def _factory(target_path, include_subfolders=True):
        return parquet_reader.process(target_path, include_subfolders=include_subfolders)
    return _factory
