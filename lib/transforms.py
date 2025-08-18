import pandas as pd
from . import validators, constants

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


def compute_alert_score(alerts: pd.DataFrame, thresholds: dict | None = None) -> tuple[float, str]:
    """Return percentage of high severity alerts and tier based on thresholds."""
    alerts = alerts.copy()
    total = len(alerts)
    high = alerts[alerts["severity"].str.title() == "High"].shape[0]
    score = (high / total * 100) if total else 0.0
    thresholds = thresholds or constants.ALERT_THRESHOLDS
    tier = "Low"
    if score >= thresholds.get("high", 0):
        tier = "High"
    elif score >= thresholds.get("medium", 0):
        tier = "Medium"
    return score, tier


def taxi_association_sentiment(minutes: pd.DataFrame) -> float:
    """Calculate sentiment score for taxi association themes."""
    mapping = {"Positive": 1, "Neutral": 0, "Negative": -1}
    ta = minutes[minutes["theme"].str.title() == "Taxi Association"]
    if ta.empty:
        return 0.0
    return ta["sentiment"].map(mapping).mean()
