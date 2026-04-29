import pandas as pd

def read_parquet_file(file_path):
    df = pd.read_parquet(file_path)
    return df.to_dict(orient='records')
