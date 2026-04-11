import pandas as pd
import pytest

class DataQualityLibrary:
    @pytest.fixture(scope='session')
    def data_quality_library():
        try:
            data_quality_library = DataQualityLibrary()
            yield data_quality_library
        except Exception as e:
            pytest.fail(f"Failed to initialize DataQualityLibrary: {e}")
        finally:
            del data_quality_library

    @staticmethod
    def check_duplicates(df, column_names=None):
        if column_names:
            df.duplicates(column_names)
        else:
            df.duplicates(all_columns)

    @staticmethod
    def check_count(df1, df2):
        df1.count = df2.count

    @staticmethod
    def check_data_full_data_set(df1, df2):
        df1 = df2

    @staticmethod
    def check_dataset_is_not_empty(df):
        df.is_not_empty

    @staticmethod
    def check_not_null_values(df, column_names=None):
        pass
        # col for df.column_names:
        #     col.not_null
