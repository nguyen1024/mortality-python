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

        # Create an array to store the tiles that the player can currently see.
        self.visible = numpy.full((width, height), fill_value=False, order="F")

        # Create an array to store the tiles that the player has seen before.
        self.explored = numpy.full((width, height), fill_value=False, order="F")
        
    #
    def in_bounds(self, x: int, y: int) -> bool:
        """Return true if x and y are within the bounds of the map."""
        return 0 <= x < self.width and 0 <= y < self.height

    #
    def render(self, console: Console) -> None:
        # Render the two dimensional array.
        #console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]
        """Renders the map.
        If a tile is in the visible array, then draw it with its "light" colour.
        If a title is not in the visible array, but it is in the explored array, then draw it with its "dark" colour.
        Otherwise, the default is "shroud"."""
        #
        console.tiles_rgb[0:self.width, 0:self.height] = numpy.select(
            #
            condlist=[self.visible, self.explored],
            #
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            #
            default=tile_types.SHROUD)
