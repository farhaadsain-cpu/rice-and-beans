from dataclasses import dataclass

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

# Percentage thresholds for alert scoring
ALERT_THRESHOLDS = {
    "high": 50,
    "medium": 25,
}

REQUIRED_HEADERS = {
    "projects": ["project_id", "project_name", "bbee_level", "local_content_pct", "local_content_target", "avg_payment_days"],
    "contractors": ["contractor_id", "contractor_name", "bbee_level"],
    "ed_kpis_monthly": ["timestamp", "project_id", "kpi", "obligation", "actual"],
    "contractor_ed_kpis_monthly": ["timestamp", "contractor_id", "kpi", "obligation", "actual"],
    "esg_metrics_annual": ["year", "project_id", "kpi", "value", "target"],
    "supplier_spend_monthly": ["month", "project_id", "local_spend", "total_spend"],
    "jobs_training_monthly": ["month", "project_id", "jobs_created", "people_trained"],
    "alerts_events": ["date", "cluster", "alert_type", "severity"],
    "site_lookup": ["site_id", "project_id", "cluster"],
    "themes_lookup": ["theme", "keywords"],
    "stakeholder_minutes": ["date", "project_id", "attendees", "summary", "sentiment", "theme"],
}
