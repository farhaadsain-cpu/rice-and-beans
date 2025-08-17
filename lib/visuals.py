import altair as alt
import plotly.express as px
from . import constants


def bar_chart(df, x, y, color=None):
    return alt.Chart(df).mark_bar().encode(x=x, y=y, color=color)


def line_chart(df, x, y, color=None):
    return alt.Chart(df).mark_line().encode(x=x, y=y, color=color)


def heatmap(df, x, y, z):
    return px.density_heatmap(df, x=x, y=y, z=z,
                               color_continuous_scale=[constants.PRIMARY_COLOR,
                                                       constants.SECONDARY_COLORS["orange"]])
