import streamlit as st
import plotly.express as px
import json
from lib import loaders, models

st.title("Predictive Risk")

alerts = loaders.load_csv("data_templates/alerts_events.csv")

summary = models.summarize_risks(alerts)
col1, col2, col3 = st.columns(3)
col1.metric("High Risk", summary["high"])
col2.metric("Emerging Risks", summary["emerging"])
col3.metric("Mitigations in Progress", summary["mitigations"])

st.subheader("Predictive Risk Trend")
trend = models.risk_trend(alerts)
fig_trend = px.line(trend, x="month", y="risk_level", markers=True)
st.plotly_chart(fig_trend, use_container_width=True)

st.subheader("Risk by Cluster")
clusters = loaders.load_csv("data_templates/site_lookup.csv")[["cluster"]].drop_duplicates()
cluster_scores = models.risk_by_cluster(alerts)
cluster_scores = clusters.merge(cluster_scores, on="cluster", how="left").fillna(0)
with open("data_templates/sa_clusters.geojson") as f:
    geojson = json.load(f)
fig_map = px.choropleth(
    cluster_scores,
    geojson=geojson,
    locations="cluster",
    featureidkey="properties.cluster",
    color="risk_score",
    color_continuous_scale="Reds",
    scope="africa",
)
fig_map.update_geos(fitbounds="locations", visible=False)
st.plotly_chart(fig_map, use_container_width=True)
