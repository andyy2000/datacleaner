import pandas as pd
from datacleaner.clean import DataCleaner

def test_handle_missing_values():
    df = pd.DataFrame({"A": [1, 2, None], "B": [4, None, 6]})
    cleaner = DataCleaner(df)
    df_cleaned = cleaner.handle_missing_values(strategy="mean")
    assert df_cleaned.isnull().sum().sum() == 0
