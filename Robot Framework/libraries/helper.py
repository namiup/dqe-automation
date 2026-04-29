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
                            
    return df

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

def compare_html_and_parquet(html_data, parquet_data):
    # Ensure both inputs are DataFrames
    if isinstance(html_data, pd.Series):
        html_data = html_data.to_frame()
    if isinstance(parquet_data, pd.Series):
        parquet_data = parquet_data.to_frame()

    # Reset row index for both DataFrames
    html_data = html_data.reset_index(drop=True)
    parquet_data = parquet_data.reset_index(drop=True)

    # Flatten MultiIndex columns if present
    if isinstance(html_data.columns, pd.MultiIndex):
        html_data.columns = ['_'.join(map(str, col)).strip() for col in html_data.columns.values]
    if isinstance(parquet_data.columns, pd.MultiIndex):
        parquet_data.columns = ['_'.join(map(str, col)).strip() for col in parquet_data.columns.values]

    # Compare the DataFrames
    match = html_data.equals(parquet_data)

    # Find unmatched rows using all columns
    unmatched_html = html_data[~html_data.apply(tuple, 1).isin(parquet_data.apply(tuple, 1))]
    unmatched_parquet = parquet_data[~parquet_data.apply(tuple, 1).isin(html_data.apply(tuple, 1))]

    return {
        "match": match,
        "html_shape": html_data.shape,
        "parquet_shape": parquet_data.shape,
        "unmatched_html": unmatched_html,
        "unmatched_parquet": unmatched_parquet
    }
