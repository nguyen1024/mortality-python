#
import numpy

#
from tcod.console import Console

#
import tile_types

# Create class GameMap.
class GameMap:
    # Create an initialisation function.
    def __init__(self, width: int, height: int):
        # Store the width.
        self.width = width
        # 
        self.height = height
        # Create a two dimensional array filled with wall tiles.
        self.tiles = numpy.full((width, height), fill_value=tile_types.wall, order="F")

    #
    def in_bounds(self, x: int, y: int) -> bool:
        """Return true if x and y are within the bounds of the map."""
        return 0 <= x < self.width and 0 <= y < self.height

    #
    def render(self, console: Console) -> None:
        # Render the two dimensional array.
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]
