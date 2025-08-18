import pandas as pd

RISK_LEVEL_MAP = {"High": 3, "Emerging": 2, "Low": 1}


def summarize_risks(alerts: pd.DataFrame) -> dict:
    high = (alerts["risk_level"] == "High").sum()
    emerging = (alerts["risk_level"] == "Emerging").sum()
    mitigations = (alerts["status"] == "Mitigating").sum()
    return {
        "high": int(high),
        "emerging": int(emerging),
        "mitigations": int(mitigations),
    }


def risk_trend(alerts: pd.DataFrame) -> pd.DataFrame:
    df = alerts.copy()
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M").dt.to_timestamp()
    df["score"] = df["risk_level"].map(RISK_LEVEL_MAP).fillna(0)
    trend = df.groupby("month")["score"].sum().reset_index(name="risk_level")
    return trend


def risk_by_cluster(alerts: pd.DataFrame) -> pd.DataFrame:
    df = alerts.copy()
    df["score"] = df["risk_level"].map(RISK_LEVEL_MAP).fillna(0)
    cluster = df.groupby("cluster")["score"].sum().reset_index(name="risk_score")
    return cluster
