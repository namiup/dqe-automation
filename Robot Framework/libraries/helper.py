import pandas as pd
from io import StringIO

def read_html_file(file_path):
    """Reads an HTML file or literal HTML content and returns the first table as a DataFrame."""
    # Check if the input is literal HTML content
    if file_path.strip().startswith("<"):
        # Wrap the literal HTML content in a StringIO object
        file_path = StringIO(file_path)
    
    # Read all tables from the HTML
    dataframes = pd.read_html(file_path)
    
    # Check if there are any tables
    if len(dataframes) == 0:
        raise ValueError("No tables found in the HTML file.")
    
    # Return the first table as a DataFrame
    return dataframes[0]

def read_parquet_file(dataset_path, date_column, start_date, end_date):
    """Reads a Parquet file and filters data based on date range."""
    filters = []
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    if start_date:
        filters.append((date_column, '>=', start_date))
    if end_date:
        filters.append((date_column, '<=', end_date))

    df = pd.read_parquet(
        dataset_path, 
        engine='pyarrow', 
        filters=filters if filters else None
    )

    return df

def compare_dataframes(df1, df2):
    """Compares two DataFrames and returns a dictionary with differences."""
    # Ensure same column order
    df1 = df1[df2.columns]
    
    # Check for exact match
    if df1.equals(df2):
        return {"match": True, "differences": None}
    
    # Find differences
    diff = {}
    # Rows only in df1
    only_in_df1 = pd.concat([df1, df2, df2]).drop_duplicates(keep=False)
    # Rows only in df2
    only_in_df2 = pd.concat([df2, df1, df1]).drop_duplicates(keep=False)
    # Rows with same index but different values
    diff_rows = df1.compare(df2, align_axis=0) if df1.shape == df2.shape else None

    diff["match"] = False
    diff["only_in_df1"] = only_in_df1 if not only_in_df1.empty else None
    diff["only_in_df2"] = only_in_df2 if not only_in_df2.empty else None
    diff["different_rows"] = diff_rows if diff_rows is not None and not diff_rows.empty else None

    return diff
