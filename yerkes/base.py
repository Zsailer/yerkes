# -*- coding: utf-8 -*-

"""Main module."""

import pandas as pd
import altair as alt


# default_palette = {
#     "turquoise": "#1abc9c",
#     "green_sea": "#16a085",
#     "sun_flower": "#f1c40f",
#     "orange": "#f39c12",
#     "emerland": "#2ecc71",
#     "nephritis": "#27ae60",
#     "carrot": "#e67e22",
#     "pumpkin": "#d35400",
#     "peter_river":"#3498db",
#     "belize_hole": "#2980b9",
#     "alizarin": "#e74c3c",
#     "pomegranate": "#c0392b",
#     "amethyst": "#af7ac4",
#     "wisteria": "#8e44ad",
#     "clouds": "#ecf0f1",
#     "silver": "#bdc3c7",
#     "wet_asphalt": "#34495e",
#     "midnight_blue": "#2c3e50",
#     "concrete": "#aab7b7",
#     "asbestos": "#98a3a3"
# }


class EmptyPalette(object):
    """Base palette object for.

    Parameters
    ----------
    square_size : int
        Width and height of palette squares.

    orientations : string
        How to orient the palette; "horizontal" or "vertical".
    """

    def __init__(self, square_size=50, orientation="horizontal"):
        self.colors = []
        self.square_size = square_size
        self.orientation = orientation

    @property
    def df(self):
        """Color palette dataframe."""
        df = pd.DataFrame(self.colors, columns=["hex"])
        return df

    def add(self, code):
        """Add a color to the palette."""
        self.colors.append(code)

    def to_chart(self):
        """Write color palette to Altair Chart.
        """
        encoding, properties = {}, {}

        if self.orientation == "horizontal":
            # Set the axis
            encoding["x"] = alt.X(
                "hex",
                axis=None,
                scale=alt.Scale(zero=False, padding=0)
            )

            # Set the rectangle size.
            properties["width"] = len(self.df)*self.square_size
            properties["height"] = self.square_size

        elif self.orientation == "vertical":
            # Set the axis
            encoding["y"] = alt.Y(
                "hex",
                axis=None,
                scale=alt.Scale(zero=False, padding=0)
            )

            # Set the rectangle size.
            properties["height"] = len(self.df)*self.square_size
            properties["width"] = self.square_size

        # Build a chart.
        tooltip = list(self.df.columns)
        chart = alt.Chart(self.df).mark_rect().encode(
            color=alt.Color("hex", legend=None, scale=alt.Scale(range=self.colors)),
            tooltip=tooltip,
            **encoding
        ).properties(
            **properties
        )
        return chart

    def _repr_mimebundle_(self, *args, **kwargs):
        """Return a MIME bundle for display in Jupyter frontends."""
        chart = self.to_chart()
        dct = chart.to_dict()
        return alt.renderers.get()(dct)
