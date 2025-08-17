import pandas as pd
from typing import List

VALID_SENTIMENTS = {"Positive", "Neutral", "Negative"}


def validate_headers(df: pd.DataFrame, required: List[str]) -> List[str]:
    """Return missing headers from DataFrame."""
    return [h for h in required if h not in df.columns]


def validate_date(value: str) -> bool:
    try:
        pd.to_datetime(value)
        return True
    except Exception:
        return False


def validate_sentiment(value: str) -> str | None:
    value = str(value).title()
    if value in VALID_SENTIMENTS:
        return value
    return None
