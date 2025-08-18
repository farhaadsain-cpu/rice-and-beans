import pandas as pd
from lib import transforms

def test_invalid_sentiment_replaced():
    df = pd.DataFrame({
        "attendees": ["A"],
        "summary": ["The meeting was good"],
        "sentiment": ["Unknown"],
        "theme": ["Community"],
    })
    norm = transforms.normalize_minutes(df)
    assert norm.loc[0, "sentiment"] == "Positive"

def test_minutes_keep_rows_with_empty_attendees():
    df = pd.DataFrame({
        "attendees": [None],
        "summary": ["No attendees"],
        "sentiment": ["Neutral"],
        "theme": ["General"],
    })
    norm = transforms.normalize_minutes(df)
    assert len(norm) == 1
    assert norm.loc[0, "attendees"] == ""


def test_compute_alert_score_threshold():
    alerts = pd.DataFrame({"severity": ["High", "High", "Low"]})
    score, tier = transforms.compute_alert_score(alerts, {"high": 50, "medium": 25})
    assert score > 60
    assert tier == "High"


def test_taxi_association_sentiment():
    mins = pd.DataFrame({
        "sentiment": ["Positive", "Negative"],
        "theme": ["Taxi Association", "Taxi Association"],
    })
    score = transforms.taxi_association_sentiment(mins)
    assert score == 0
