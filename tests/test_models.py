import pandas as pd
from lib import models

def test_model_train_predict():
    df = pd.DataFrame({
        "metric1": [1, 2, 3, 4],
        "metric2": [0, 1, 0, 1],
        "risk_flag": [0, 0, 1, 1],
    })
    model = models.train_risk_model(df)
    preds = models.predict_risk(model, df[["metric1", "metric2"]])
    assert len(preds) == len(df)
