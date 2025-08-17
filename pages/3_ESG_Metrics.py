import streamlit as st
import altair as alt
from lib import loaders

st.title("ESG Metrics")

esg = loaders.load_csv("data_templates/esg_metrics_annual.csv")

st.dataframe(esg)

bar = alt.Chart(esg).mark_bar().encode(
    x="project_id",
    y="value",
    color="kpi",
)
st.altair_chart(bar, use_container_width=True)
