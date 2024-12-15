def validate_dataframe(df):
    """Validate if the input is a pandas DataFrame."""
    import pandas as pd
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    return True
