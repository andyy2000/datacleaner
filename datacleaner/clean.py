import pandas as pd

class DataCleaner:
    def __init__(self, dataframe):
        self.df = dataframe

    def handle_missing_values(self, strategy="mean", columns=None):
        """
        Handle missing values in the DataFrame.
        strategy: 'mean', 'median', 'mode', or 'drop'.
        columns: List of columns to process. If None, applies to all columns.
        """
        if columns is None:
            columns = self.df.columns
        
        for col in columns:
            if strategy == "mean" and self.df[col].dtype in ["float64", "int64"]:
                self.df[col].fillna(self.df[col].mean(), inplace=True)
            elif strategy == "median" and self.df[col].dtype in ["float64", "int64"]:
                self.df[col].fillna(self.df[col].median(), inplace=True)
            elif strategy == "mode":
                self.df[col].fillna(self.df[col].mode()[0], inplace=True)
            elif strategy == "drop":
                self.df.dropna(subset=[col], inplace=True)
        return self.df

    def remove_duplicates(self):
        """Remove duplicate rows from the DataFrame."""
        self.df.drop_duplicates(inplace=True)
        return self.df

    def standardize_column_names(self):
        """Standardize column names to lowercase and replace spaces with underscores."""
        self.df.columns = self.df.columns.str.lower().str.replace(' ', '_')
        return self.df
