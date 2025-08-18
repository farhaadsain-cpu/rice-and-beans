import altair as alt
from . import constants


def bar_chart(df, x, y, color=None):
    return alt.Chart(df).mark_bar().encode(x=x, y=y, color=color)


def line_chart(df, x, y, color=None):
    return alt.Chart(df).mark_line().encode(x=x, y=y, color=color)
