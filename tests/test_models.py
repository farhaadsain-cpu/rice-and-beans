import pandas as pd
from lib import models

alerts = pd.DataFrame({
    "date": ["2024-01-01", "2024-01-02", "2024-02-01"],
    "cluster": ["North", "South", "North"],
    "risk_level": ["High", "Emerging", "High"],
    "status": ["Open", "Mitigating", "Open"],
})


def test_summarize_risks():
    summary = models.summarize_risks(alerts)
    assert summary["high"] == 2
    assert summary["emerging"] == 1
    assert summary["mitigations"] == 1


def test_risk_trend():
    trend = models.risk_trend(alerts)
    assert "risk_level" in trend.columns
    assert len(trend) == 2


def test_risk_by_cluster():
    by_cluster = models.risk_by_cluster(alerts)
    assert set(by_cluster.columns) == {"cluster", "risk_score"}
    north_score = by_cluster.loc[by_cluster["cluster"] == "North", "risk_score"].iloc[0]
    assert north_score == 6
