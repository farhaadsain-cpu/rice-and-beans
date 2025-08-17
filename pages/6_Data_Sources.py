import streamlit as st
from lib import loaders, validators, constants

st.title("Data Sources")

FILES = {
    "projects.csv": "projects",
    "contractors.csv": "contractors",
    "ed_kpis_monthly.csv": "ed_kpis_monthly",
    "contractor_ed_kpis_monthly.csv": "contractor_ed_kpis_monthly",
    "esg_metrics_annual.csv": "esg_metrics_annual",
    "supplier_spend_monthly.csv": "supplier_spend_monthly",
    "jobs_training_monthly.csv": "jobs_training_monthly",
    "alerts_events.csv": "alerts_events",
    "site_lookup.csv": "site_lookup",
    "themes_lookup.csv": "themes_lookup",
    "stakeholder_minutes.csv": "stakeholder_minutes",
}

for label, key in FILES.items():
    uploaded = st.file_uploader(label, type="csv")
    if uploaded:
        df = loaders.load_uploaded_csv(uploaded)
        missing = validators.validate_headers(df, constants.REQUIRED_HEADERS[key])
        if missing:
            st.error(f"{label}: FAIL - missing {missing}")
        else:
            st.success(f"{label}: PASS")
