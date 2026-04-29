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


def read_partitioned_parquet_with_date_filter(
    dataset_path, 
    date_column, 
    start_date=None, 
    end_date=None
):
    """
    Reads a partitioned Parquet dataset and filters by date.

    Args:
        dataset_path (str): Path to the root of the partitioned Parquet dataset.
        date_column (str): Name of the date column to filter on.
        start_date (str or None): Start date (inclusive) in 'YYYY-MM-DD' format.
        end_date (str or None): End date (inclusive) in 'YYYY-MM-DD' format.

    Returns:
        list: List of records (dicts) after filtering.
    """
    filters = []
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
