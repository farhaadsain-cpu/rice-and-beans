import pandas as pd
from sklearn.linear_model import LogisticRegression


def train_risk_model(df: pd.DataFrame) -> LogisticRegression:
    X = df.drop(columns=["risk_flag"])
    y = df["risk_flag"]
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    return model


def predict_risk(model: LogisticRegression, X: pd.DataFrame) -> pd.Series:
    return pd.Series(model.predict_proba(X)[:, 1], index=X.index)
