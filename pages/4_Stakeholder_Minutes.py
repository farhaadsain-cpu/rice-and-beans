import streamlit as st
import altair as alt
from lib import loaders, transforms

st.title("Stakeholder Minutes")

uploaded = st.file_uploader("Upload stakeholder minutes", type="csv")
if uploaded:
    df = loaders.load_uploaded_csv(uploaded)
else:
    df = loaders.load_csv("data_templates/stakeholder_minutes.csv")

df = transforms.normalize_minutes(df)

st.subheader("Themes")
counts = df["theme"].value_counts().reset_index()
chart = alt.Chart(counts).mark_bar().encode(x="index", y="theme")
st.altair_chart(chart, use_container_width=True)

st.subheader("Table")
st.dataframe(df)
