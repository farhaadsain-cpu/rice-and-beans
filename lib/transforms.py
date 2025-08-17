import pandas as pd
from . import validators

POSITIVE_WORDS = {"good", "excellent", "positive", "great"}
NEGATIVE_WORDS = {"bad", "poor", "negative", "delay"}


def infer_sentiment(text: str) -> str:
    text = str(text).lower()
    if any(word in text for word in POSITIVE_WORDS):
        return "Positive"
    if any(word in text for word in NEGATIVE_WORDS):
        return "Negative"
    return "Neutral"


def normalize_minutes(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["attendees"] = df["attendees"].fillna("")
    df["sentiment"] = df["sentiment"].apply(validators.validate_sentiment)
    mask = df["sentiment"].isna()
    df.loc[mask, "sentiment"] = df.loc[mask, "summary"].apply(infer_sentiment)
    return df
