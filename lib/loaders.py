import pandas as pd
from typing import IO


def load_csv(path: str) -> pd.DataFrame:
    """Load CSV from path."""
    return pd.read_csv(path)


def load_uploaded_csv(uploaded: IO) -> pd.DataFrame:
    """Load a CSV uploaded via Streamlit."""
    return pd.read_csv(uploaded)
