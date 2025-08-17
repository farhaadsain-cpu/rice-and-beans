import streamlit as st
import pandas as pd
import plotly.express as px
from lib import loaders, models

st.title("Predictive Risk")

alerts = loaders.load_csv("data_templates/alerts_events.csv")
alerts["month"] = pd.to_datetime(alerts["date"]).dt.to_period("M").astype(str)
heatmap = alerts.groupby(["cluster","month"]).size().reset_index(name="count")
fig = px.density_heatmap(heatmap, x="month", y="cluster", z="count", color_continuous_scale="Blues")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Model")
sample = pd.DataFrame({"metric1":[1,2,3,4],"metric2":[0,1,0,1],"risk_flag":[0,0,1,1]})
model = models.train_risk_model(sample)
preds = models.predict_risk(model, sample[["metric1","metric2"]])
st.write(preds)
