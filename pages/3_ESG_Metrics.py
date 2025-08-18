import streamlit as st
import pandas as pd
import altair as alt
from lib import loaders, constants

# Mapping of KPIs to categories and descriptions
KPI_DETAILS = {
    "carbon_emissions_avoided": (
        "Environmental",
        "Tonnes of CO₂ emissions avoided through EDF projects, supporting carbon neutrality goals."
    ),
    "recycling_rate": (
        "Environmental",
        "Percentage of waste recycled, contributing to circular economy targets."
    ),
    "water_use": (
        "Environmental",
        "Annual water consumption, targeted for responsible resource use."
    ),
    "training_hours": (
        "Social",
        "Total hours of workforce training delivered, advancing skills development."
    ),
    "dei_percentage": (
        "Social",
        "Share of workforce from underrepresented groups, aligning with EDF's diversity commitments."
    ),
    "csr_objectives_met": (
        "Governance",
        "Number of corporate social responsibility objectives achieved, reinforcing EDF's governance standards."
    ),
}

st.title("ESG Metrics")

esg = loaders.load_csv("data_templates/esg_metrics_annual.csv")
esg["category"] = esg["kpi"].map(lambda k: KPI_DETAILS.get(k, ("Other", ""))[0])
esg["description"] = esg["kpi"].map(lambda k: KPI_DETAILS.get(k, ("", ""))[1])

for category in ["Environmental", "Social", "Governance"]:
    st.header(category)
    cat_df = esg[esg["category"] == category]
    for kpi, group in cat_df.groupby("kpi"):
        group = group.assign(
            progress=group["value"] / group["target"],
            status_color=lambda df: df["value"] >= df["target"],
        )
        group["status_color"] = group["status_color"].map(
            {True: constants.SECONDARY_COLORS["green"], False: constants.SECONDARY_COLORS["red"]}
        )
        chart = alt.Chart(group).mark_bar().encode(
            x=alt.X("project_id:N", title="Project"),
            y=alt.Y("progress:Q", title="Progress", axis=alt.Axis(format="%")),
            color=alt.Color("status_color:N", scale=None),
            tooltip=["project_id", "value", "target", "description"],
        ).properties(title=kpi.replace("_", " ").title())
        target_rule = alt.Chart(pd.DataFrame({"target": [1]})).mark_rule(
            color=constants.SECONDARY_COLORS["amber"]
        ).encode(y="target:Q")
        st.altair_chart(chart + target_rule, use_container_width=True)
        st.caption(group["description"].iloc[0])
