import streamlit as st
import altair as alt
import pandas as pd
from lib import loaders

st.title("ED Performance")

ed = loaders.load_csv("data_templates/ed_kpis_monthly.csv")
contractor_ed = loaders.load_csv("data_templates/contractor_ed_kpis_monthly.csv")

# Prepare timestamps and quarters
for df in (ed, contractor_ed):
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["quarter"] = df["timestamp"].dt.to_period("Q").astype(str)

# Quarterly aggregation for projects
proj_quarterly = (
    ed.groupby(["project_id", "quarter"])
    .agg({"obligation": "sum", "actual": "sum"})
    .reset_index()
)
proj_quarterly["deviation"] = proj_quarterly["actual"] - proj_quarterly["obligation"]

# Quarterly aggregation for contractors
cont_quarterly = (
    contractor_ed.groupby(["contractor_id", "quarter"])
    .agg({"obligation": "sum", "actual": "sum"})
    .reset_index()
)
cont_quarterly["deviation"] = cont_quarterly["actual"] - cont_quarterly["obligation"]

st.subheader("Project Quarterly Performance")
st.dataframe(proj_quarterly)

proj_chart_data = proj_quarterly.melt(
    id_vars=["project_id", "quarter"],
    value_vars=["obligation", "actual"],
    var_name="type",
    value_name="value",
)
proj_chart = (
    alt.Chart(proj_chart_data)
    .mark_line()
    .encode(
        x="quarter:O",
        y="value:Q",
        color="project_id:N",
        strokeDash="type:N",
    )
)
st.altair_chart(proj_chart, use_container_width=True)

st.subheader("Contractor Quarterly Performance")
st.dataframe(cont_quarterly)

cont_chart_data = cont_quarterly.melt(
    id_vars=["contractor_id", "quarter"],
    value_vars=["obligation", "actual"],
    var_name="type",
    value_name="value",
)
cont_chart = (
    alt.Chart(cont_chart_data)
    .mark_line()
    .encode(
        x="quarter:O",
        y="value:Q",
        color="contractor_id:N",
        strokeDash="type:N",
    )
)
st.altair_chart(cont_chart, use_container_width=True)

# Red flag indicators
st.subheader("Project Obligation Shortfalls")
proj_red_flags = proj_quarterly[proj_quarterly["actual"] < proj_quarterly["obligation"]]
st.dataframe(proj_red_flags)

st.subheader("Contractor Obligation Shortfalls")
cont_red_flags = cont_quarterly[cont_quarterly["actual"] < cont_quarterly["obligation"]]
st.dataframe(cont_red_flags)
