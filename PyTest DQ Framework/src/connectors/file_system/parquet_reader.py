class ParquetReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self, columns=None):
        return pd.read_parquet(self.file_path, columns=columns)

    def process(self, target_path=None, include_subfolders=False):
        """
        Process Parquet files at target_path.
        If include_subfolders is True, process files in subfolders as well.
        """
        import os
        import glob

        files = []
        if include_subfolders:
            # Recursively find all .parquet files
            files = glob.glob(os.path.join(target_path, '**', '*.parquet'), recursive=True)
        else:
            # Only files in the target_path directory
            files = glob.glob(os.path.join(target_path, '*.parquet'))

        dfs = [pd.read_parquet(f) for f in files]
        if dfs:
            return pd.concat(dfs, ignore_index=True)
        else:
            return pd.DataFrame()  # Return empty DataFrame if no files found
