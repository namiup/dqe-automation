import pandas as pd

class ParquetReader:
    """
    A class for reading and processing Parquet files from the file system.
    """

    def __init__(self, file_path):
        """
        Initialize with the path to the Parquet file.
        """
        self.file_path = file_path

    def read(self, columns=None):
        """
        Read the Parquet file into a pandas DataFrame.
        :param columns: List of columns to read (optional).
        :return: pandas.DataFrame
        """
        return pd.read_parquet(self.file_path, columns=columns)

    def get_row_count(self):
        """
        Return the number of rows in the Parquet file.
        """
        df = self.read()
        return len(df)

    def get_columns(self):
        """
        Return the list of columns in the Parquet file.
        """
        df = self.read()
        return df.columns.tolist()

    def filter_rows(self, filter_func):
        """
        Return rows that match a filter function.
        :param filter_func: A function that takes a DataFrame and returns a filtered DataFrame.
        :return: pandas.DataFrame
        """
        df = self.read()
        return filter_func(df)
