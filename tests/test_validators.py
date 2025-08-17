import pandas as pd
from lib import validators


def test_validate_headers_missing():
    df = pd.DataFrame({"a": [1]})
    missing = validators.validate_headers(df, ["a", "b"])
    assert missing == ["b"]


def test_validate_sentiment():
    assert validators.validate_sentiment("Positive") == "Positive"
    assert validators.validate_sentiment("bad") is None
