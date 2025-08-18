import streamlit as st
import pandas as pd
from lib import loaders, models

st.title("Risk Summary")

alerts = loaders.load_csv("data_templates/alerts_events.csv")
cluster_counts = alerts["cluster"].value_counts()
cols = st.columns(len(cluster_counts))
for col, (cluster, count) in zip(cols, cluster_counts.items()):
    col.metric(label=cluster, value=int(count))

st.subheader("Model")
sample = pd.DataFrame({"metric1":[1,2,3,4],"metric2":[0,1,0,1],"risk_flag":[0,0,1,1]})
model = models.train_risk_model(sample)
preds = models.predict_risk(model, sample[["metric1","metric2"]])
st.write(preds)
