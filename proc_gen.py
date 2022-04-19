#
import random

#
from typing import Iterator

#
from typing import Tuple

#
from game_map import GameMap

#
import tcod

#
import tile_types

#
class RectangularRoom:
    #
    def __init__(self, x: int, y: int, width: int, height: int):
        # Set x1.
        self.x1 = x
        # Set y1.
        self.y1 = y
        # Set x2.
        self.x2 = x + width
        # Set y2.
        self.y2 = y + height

    # Create a property.
    @property
    #
    def center(self) -> Tuple[int, int]:
        #
        center_x = int((self.x1 + self.x2) / 2)
        #
        center_y = int((self.y1 + self.y2) / 2)
        #
        return center_x, center_y

    #
    @property
    #
    def inner(self) -> Tuple[slice, slice]:
        """Return the inner area of this room as a 2D array index."""
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)

#
def tunnel_between(start: Tuple[int, int],
                   end: Tuple[int, int]) -> Iterator[Tuple[int, int]]:
    """Return an L-shaped tunnerl between two points."""
    #
    x1, y1 = start
    #
    x2, y2 = end
    #
    if random.random() < 0.5:
        # Move horizontally.
        corner_x = x2
        # Move vertically.
        corner_y = y1
    #
    else:
        # Move vertically.
        corner_y = y2
        # Move horizontally.
        corner_x = x1
    # Generate coordinates for tunnel.
    for x, y in tcod.los.bresenham((x1, y1), (corner_x, corner_y)).tolist():
        # Return values but keep local state.
        yield x, y
    #
    for x, y in tcod.los.bresenham((corner_x, corner_y), (x2, y2)).tolist():
        # Return values but keep local state.
        yield x, y
    
#
def generate_dungeon(map_width, map_height) -> GameMap:
    #
    dungeon = GameMap(map_width, map_height)
    #
    room_1 = RectangularRoom(x=20, y=15, width=10, height=15)
    #
    room_2 = RectangularRoom(x=35, y=15, width=10, height=15)
    #
    dungeon.tiles[room_1.inner] = tile_types.floor
    #
    dungeon.tiles[room_2.inner] = tile_types.floor
    # For each position in the tunnel:
    for x, y in tunnel_between(room_2.center, room_1.center):
        # Set the tile type to floor
        dungeon.tiles[x, y] = tile_types.floor
    #
    return dungeon
