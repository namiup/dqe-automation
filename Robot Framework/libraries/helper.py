import pandas as pd

def read_html_file(file_path):
    df = pd.read_html(file_path)
    return df.to_string(index=False)
