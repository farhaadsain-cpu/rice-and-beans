import streamlit as st
import altair as alt
from lib import loaders

st.title("ED Performance")

ed = loaders.load_csv("data_templates/ed_kpis_monthly.csv")
contractor_ed = loaders.load_csv("data_templates/contractor_ed_kpis_monthly.csv")

proj_rollup = ed.groupby("project_id")["value"].mean().reset_index()
cont_rollup = contractor_ed.groupby("contractor_id")["value"].mean().reset_index()

st.subheader("Project Rollup")
st.dataframe(proj_rollup)

st.subheader("Contractor Rollup")
st.dataframe(cont_rollup)

red_flags = ed[ed["value"] < 50]
st.subheader("Red Flags")
st.dataframe(red_flags)

st.subheader("Trends")
chart = alt.Chart(ed).mark_line().encode(x="month", y="value", color="project_id")
st.altair_chart(chart, use_container_width=True)
