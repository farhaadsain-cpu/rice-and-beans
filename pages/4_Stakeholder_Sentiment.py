import streamlit as st
import pandas as pd
import altair as alt
from lib import loaders, transforms

st.title("Stakeholder Sentiment")

uploaded = st.file_uploader("Upload stakeholder minutes", type="csv")
if uploaded:
    df = loaders.load_uploaded_csv(uploaded)
else:
    df = loaders.load_csv("data_templates/stakeholder_minutes.csv")

df = transforms.normalize_minutes(df)
df["date"] = pd.to_datetime(df["date"])
if "location" not in df.columns:
    df["location"] = ""

sent_counts = df["sentiment"].value_counts()
recent_alerts = df[df["sentiment"] == "Negative"].sort_values("date", ascending=False).head(5)
high_risk = df[df["summary"].str.contains("risk|concern|delay", case=False, na=False)]

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Positive", int(sent_counts.get("Positive", 0)))
c2.metric("Neutral", int(sent_counts.get("Neutral", 0)))
c3.metric("Negative", int(sent_counts.get("Negative", 0)))
c4.metric("Recent Alerts", len(recent_alerts))
c5.metric("High-Risk Notes", len(high_risk))

st.subheader("Sentiment Over Time")
sentiment_numeric = df["sentiment"].map({"Positive": 1, "Neutral": 0, "Negative": -1})
sent_over_time = (
    df.assign(sentiment_numeric=sentiment_numeric)
    .groupby("date")["sentiment_numeric"].mean()
    .reset_index()
)
line_chart = alt.Chart(sent_over_time).mark_line().encode(x="date:T", y="sentiment_numeric:Q")
st.altair_chart(line_chart, use_container_width=True)

st.subheader("Meeting Themes")
theme_counts = df["theme"].value_counts().reset_index()
theme_chart = alt.Chart(theme_counts).mark_bar().encode(x="index", y="theme")
st.altair_chart(theme_chart, use_container_width=True)

st.subheader("Meeting Minutiae")
minutiae = df[["date", "location", "attendees", "summary", "sentiment"]]

def highlight(row):
    color = "#fdd" if row["sentiment"] == "Negative" else ""
    return ["background-color: " + color] * len(row)

st.dataframe(minutiae.style.apply(highlight, axis=1).hide_index(), use_container_width=True)

st.subheader("Recent Alerts")
st.dataframe(recent_alerts[["date", "summary", "sentiment"]], use_container_width=True)
