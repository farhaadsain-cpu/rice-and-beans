import streamlit as st
from lib import loaders, transforms, constants, visuals

st.title("Overview")

projects = loaders.load_csv("data_templates/projects.csv")
contractors = loaders.load_csv("data_templates/contractors.csv")
minutes = loaders.load_csv("data_templates/stakeholder_minutes.csv")
alerts = loaders.load_csv("data_templates/alerts_events.csv")

minutes = transforms.normalize_minutes(minutes)
alert_score, alert_tier = transforms.compute_alert_score(alerts)
taxi_sent = transforms.taxi_association_sentiment(minutes)
avg_bbee = contractors["bbee_level"].mean()
local_vs_target = (
    projects["local_content_pct"].mean() - projects["local_content_target"].mean()
)

color_map = {
    "High": constants.SECONDARY_COLORS["red"],
    "Medium": constants.SECONDARY_COLORS["amber"],
    "Low": constants.SECONDARY_COLORS["green"],
}

st.markdown(
    f"""
    <div style='background-color:{color_map[alert_tier]}; padding:10px; border-radius:5px; text-align:center; color:white;'>
        Alert Score: {alert_score:.1f}% ({alert_tier})
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Avg B-BBEE Level", f"{avg_bbee:.1f}")
with col2:
    st.metric("Local Content vs Target", f"{local_vs_target:.1f}")
with col3:
    st.metric("Taxi Association Sentiment", f"{taxi_sent:.2f}")

st.subheader("Alerts Trend")
alert_trend = alerts.groupby(["date", "severity"]).size().reset_index(name="count")
chart = visuals.bar_chart(alert_trend, "date", "count", color="severity")
st.altair_chart(chart, use_container_width=True)
