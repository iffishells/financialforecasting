import yfinance as yf
import pandas as pd
import numpy as np
import os
import glob
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_scatter(df, x_feature_names=None, y_feature_names=None):
    # os.makedirs("../plots/Iteration_03", exist_ok=True)
    saturday_Df = df[df["day_of_week"] == 5]
    sunday_Df = df[df["day_of_week"] == 6]
    friday_Df = df[df["day_of_week"] == 4]
    thursday_Df = df[df["day_of_week"] == 3]
    wednesday_Df = df[df["day_of_week"] == 2]
    Tuesday_Df = df[df["day_of_week"] == 1]
    monday_Df = df[df["day_of_week"] == 0]

    jan_Df = df[df["month"] == 1]
    feb_Df = df[df["month"] == 2]
    march_Df = df[df["month"] == 3]
    april_Df = df[df["month"] == 4]
    may_Df = df[df["month"] == 5]
    june_Df = df[df["month"] == 6]
    july_Df = df[df["month"] == 7]
    aug_Df = df[df["month"] == 8]
    sept_Df = df[df["month"] == 9]
    oct_Df = df[df["month"] == 10]
    Nov_Df = df[df["month"] == 11]
    decem_Df = df[df["month"] == 12]

    fig = make_subplots()

    fig.add_trace(
        go.Scatter(
            x=df[x_feature_names],
            y=df[y_feature_names],
            mode="markers+lines",
            name="Quantity",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=saturday_Df[x_feature_names],
            y=saturday_Df[y_feature_names],
            mode="markers",
            name="-Saturday-Quantity",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=sunday_Df[x_feature_names],
            y=sunday_Df[y_feature_names],
            mode="markers",
            name="-Sunday-Quantity",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=friday_Df[x_feature_names],
            y=friday_Df[y_feature_names],
            mode="markers",
            name="-friday-Quantity",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=thursday_Df[x_feature_names],
            y=thursday_Df[y_feature_names],
            mode="markers",
            name="-Thursday-Quantity",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=wednesday_Df[x_feature_names],
            y=wednesday_Df[y_feature_names],
            mode="markers",
            name="-Wednesday-Quantity",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=Tuesday_Df[x_feature_names],
            y=Tuesday_Df[y_feature_names],
            mode="markers",
            name="-Tuesday-Quantity",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=monday_Df[x_feature_names],
            y=monday_Df[y_feature_names],
            mode="markers",
            name="-Monday-Quantity",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=jan_Df[x_feature_names],
            y=jan_Df[y_feature_names],
            mode="markers+lines",
            name="-Jan-Quantity",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=feb_Df[x_feature_names],
            y=feb_Df[y_feature_names],
            mode="markers+lines",
            name="-Feb-Quantity",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=march_Df[x_feature_names],
            y=march_Df[y_feature_names],
            mode="markers+lines",
            name="-March-Quantity",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=april_Df[x_feature_names],
            y=april_Df[y_feature_names],
            mode="markers+lines",
            name="-April-Quantity",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=may_Df[x_feature_names],
            y=may_Df[y_feature_names],
            mode="markers+lines",
            name="-May-Quantity",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=june_Df[x_feature_names],
            y=june_Df[y_feature_names],
            mode="markers+lines",
            name="-June-Quantity",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=july_Df[x_feature_names],
            y=july_Df[y_feature_names],
            mode="markers+lines",
            name="-july-Quantity",
        ),
    )
    fig.add_trace(
        go.Scatter(
            x=aug_Df[x_feature_names],
            y=aug_Df[y_feature_names],
            mode="markers+lines",
            name="-Aug-Quantity",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=sept_Df[x_feature_names],
            y=sept_Df[y_feature_names],
            mode="markers+lines",
            name="-Sept-Quantity",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=Nov_Df[x_feature_names],
            y=Nov_Df[y_feature_names],
            mode="markers+lines",
            name="-Nov-Quantity",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=oct_Df[x_feature_names],
            y=oct_Df[y_feature_names],
            mode="markers+lines",
            name="-Oct-Quantity",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=decem_Df[x_feature_names],
            y=decem_Df[y_feature_names],
            mode="markers+lines",
            name="-Decem-Quantity",
        )
    )

    fig.update_layout(
        title="Amazon Stock Price Over Time", height=600, width=1800, font_size=14
    )
    fig.update_yaxes(title_text="Close Price", row=1, col=1)
    fig.show()
    fig.write_html(f"../Plots/EDAPlots/detailed_visualization.html")