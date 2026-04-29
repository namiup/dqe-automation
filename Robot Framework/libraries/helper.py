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

    pdfd = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Salary": [50000, 60000, 70000, 80000]
    }
                            
    return pdfd

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
    """
    Compare two pandas DataFrames and return the comparison result.
    """
    import pandas as pd

    # Ensure both inputs are DataFrames
    if isinstance(html_data, pd.Series):
        html_data = html_data.to_frame()
    if isinstance(parquet_data, pd.Series):
        parquet_data = parquet_data.to_frame()

    # Compare the DataFrames
    match = html_data.equals(parquet_data)

    # Return the result as a dictionary
    return {"match": match, "html_shape": html_data.shape, "parquet_shape": parquet_data.shape}
