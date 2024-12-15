from datacleaner.utils import validate_dataframe
import pandas as pd

def test_validate_dataframe():
    df = pd.DataFrame({"A": [1, 2, 3]})
    assert validate_dataframe(df)
