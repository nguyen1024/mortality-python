#
from typing import Tuple

#
import numpy

# Create a graphic data type.
graphic_dt = numpy.dtype([
    # Something unicode for the character..
    ("ch", numpy.int32),
    # 3 unsigned bytes for RGB.
    ("fg", "3B"),
    # 3 unsigned bytes for RGB.
    ("bg", "3B")])


# Create a tile data type.
tile_dt = numpy.dtype([
    # Store whether the tile is walkable.
    ("walkable", numpy.bool),
    # Store whether the tile is transparent.
    ("transparent", numpy.bool),
    # Graphic for this tile is not in the field of view.
    ("dark", graphic_dt),
    # Graphic for when the tile is in the field of view.
    ("light", graphic_dt)])

# Create a helper function for definining individual tile types.
def new_tile(
        *,
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
        light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]]) -> numpy.array:
    # Create an array that contains one tile.
    return numpy.array((walkable, transparent, dark, light), dtype=tile_dt)

# Create a tile to represent unseen tiles.
SHROUD = numpy.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype = graphic_dt)
        
# Create floor tile.
floor = new_tile(
    #
    walkable=True,
    #
    transparent=True,
    #
    dark=(
        # Set character.
        ord("."),
        # Set foreground colour.
        (255, 255, 255),
        # Set background colour.
        (50, 50, 150)),
    #
    light=(
        # Set character.
        ord("."),
        # Set foreground colour.
        (255, 255, 255),
        # Set background colour.
        (200, 180, 50)))

# Create wall tile.
wall = new_tile(
    #
    walkable=False,
    #
    transparent=False,
    #
    dark=(
        # Set character.
        ord("#"),
        # Set foreground colour.
        (255, 255, 255),
        # Set background colour.
        (0, 0, 100)),
    #
    light=(
        # Set character.
        ord("#"),
        # Set foreground colour.
        (255, 255, 255),
        # Set background colour.
        (130, 110, 50)))

