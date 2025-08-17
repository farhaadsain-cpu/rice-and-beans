import streamlit as st
import pandas as pd
from lib import loaders, transforms

st.title("Overview")

projects = loaders.load_csv("data_templates/projects.csv")
contractors = loaders.load_csv("data_templates/contractors.csv")
minutes = loaders.load_csv("data_templates/stakeholder_minutes.csv")
alerts = loaders.load_csv("data_templates/alerts_events.csv")

minutes = transforms.normalize_minutes(minutes)
mean_sent = minutes["sentiment"].map({"Positive":1,"Neutral":0,"Negative":-1}).mean()
avg_bbee = contractors["bbee_level"].mean()
local_vs_target = (
    projects["local_content_pct"].mean() - projects["local_content_target"].mean()
)
avg_payment = projects["avg_payment_days"].mean()
risk_rate = (alerts[alerts["severity"]=="High"].shape[0] / max(len(alerts),1)) * 100

col1,col2,col3,col4,col5 = st.columns(5)
col1.metric("Risk Events (%)", f"{risk_rate:.1f}")
col2.metric("Avg B-BBEE Level", f"{avg_bbee:.1f}")
col3.metric("Local Content vs Target", f"{local_vs_target:.1f}")
col4.metric("Avg Payment Days", f"{avg_payment:.1f}")
col5.metric("Mean Sentiment", f"{mean_sent:.2f}")
