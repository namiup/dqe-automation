import pandas as pd


class DataQualityLibrary:
    """
    A library of static methods for performing data quality checks on pandas DataFrames.

    This class is intended to be used in a PyTest-based testing framework to validate
    the quality of data in DataFrames. Each method performs a specific data quality
    check and uses assertions to ensure that the data meets the expected conditions.
    """

    @staticmethod
    def check_duplicates(df, column_names=None):
        if column_names:
            df.duplicated(column_names)
        else:
            df.duplicated(all_columns)

    @staticmethod
    def check_count(df1, df2):
        assert len(df1) == len(df2), f"Row counts differ: {len(df1)} != {len(df2)}"

    @staticmethod
    def check_data_full_data_set(df1, df2):
        df1 = df2

    @staticmethod
    def check_dataset_is_not_empty(df):
        assert not df.empty, "Dataset is empty"

    @staticmethod
    def check_not_null_values(df, column_names=None):
        for col in df.column_names:
            col.not_null
