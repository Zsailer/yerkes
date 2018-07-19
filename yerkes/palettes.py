from .base import EmptyPalette


class NewPalette(EmptyPalette):
    """Create a new palette in Altair from a list of colors.

    Parameters
    ----------
    colors : list
        List of hex codes.

    square_size : int
        Width and height of palette squares.

    orientations : string
        How to orient the palette; "horizontal" or "vertical".
    """
    def __init__(self, colors=None, square_size=50, orientation="horizontal"):
        super().__init__(square_size=square_size, orientation=orientation)
        self.colors = colors
