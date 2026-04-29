import pandas as pd
from io import StringIO

def read_html_file(file_path):
    """Reads an HTML file or literal HTML content and returns the first table as a string."""
    # Check if the input is literal HTML content
    if file_path.strip().startswith("<"):
        # Wrap the literal HTML content in a StringIO object
        file_path = StringIO(file_path)
    
    # Read all tables from the HTML
    dataframes = pd.read_html(file_path)
    
    # Check if there are any tables
    if len(dataframes) == 0:
        return "No tables found in the HTML file."
    
    # Get the first table and convert it to a string
    df = dataframes[0]
    return df.to_string(index=False)


def read_parquet_file(dataset_path, date_column='date', start_date=None, end_date=None):
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
    return df.to_dict(orient='records')
