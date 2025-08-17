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
