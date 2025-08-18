PRIMARY_COLOR = "#0061A8"
SECONDARY_COLORS = {
    "navy": "#003B73",
    "orange": "#FF5F00",
    "green": "#2E7D32",
    "red": "#C62828",
    "amber": "#F59E0B",
}

# Targets for demo purposes
TARGETS = {
    "local_content_pct": 60,
    "bbee_level": 4,
}

REQUIRED_HEADERS = {
    "projects": ["project_id", "project_name", "bbee_level", "local_content_pct", "local_content_target", "avg_payment_days"],
    "contractors": ["contractor_id", "contractor_name", "bbee_level"],
    "ed_kpis_monthly": ["month", "project_id", "kpi", "value"],
    "contractor_ed_kpis_monthly": ["month", "contractor_id", "kpi", "value"],
    "esg_metrics_annual": ["year", "project_id", "kpi", "value", "target"],
    "supplier_spend_monthly": ["month", "project_id", "local_spend", "total_spend"],
    "jobs_training_monthly": ["month", "project_id", "jobs_created", "people_trained"],
    "alerts_events": ["date", "cluster", "alert_type", "severity"],
    "site_lookup": ["site_id", "project_id", "cluster"],
    "themes_lookup": ["theme", "keywords"],
    "stakeholder_minutes": [
        "date",
        "project_id",
        "location",
        "attendees",
        "summary",
        "sentiment",
        "theme",
    ],
}
