import pandas as pd

class ParquetReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self, columns=None):
        return pd.read_parquet(self.file_path, columns=columns)

    def process(self, func, columns=None):
        """
        Read the Parquet file and apply a processing function to the DataFrame.
        :param func: A function that takes a DataFrame and returns a processed DataFrame.
        :param columns: Optional list of columns to read.
        :return: Processed DataFrame
        """
        df = self.read(columns=columns)
        return func(df)
