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
    
    df = dataframes[0]
    return df.iloc[:, 1]

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
    return df.iloc[:, 1]

def compare_dataframes(df1, df2):
    """
    Compare two pandas DataFrames or Series and return a dictionary with the comparison result.
    """
    if not isinstance(df1, (pd.DataFrame, pd.Series)) or not isinstance(df2, (pd.DataFrame, pd.Series)):
        raise ValueError("Both inputs must be pandas DataFrames or Series.")

    # Check if the dataframes/series are equal
    match = df1.equals(df2)

    # Return the result as a dictionary
    return {"match": match, "df1_shape": df1.shape, "df2_shape": df2.shape}

def get_columns(df):
    """Returns the column names of a DataFrame as a list."""
    return list(df.columns)
