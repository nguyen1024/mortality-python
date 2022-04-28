# To allow classes to reference themselves.
from __future__ import annotations

#
import random

#
from typing import Iterator

#
from typing import List

#
from typing import Tuple

#
from typing import TYPE_CHECKING

#
from game_map import GameMap

#
import tcod

#
import entity_factories

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
    def intersects(self, other: RectangularRoom) -> bool:
        """Return True if this room overlaps with another RectangularRoom."""
        # 
        return (
            #
            self.x1 <= other.x2
            #
            and self.x2 >= other.x1
            #
            and self.y1 <= other.y2
            #
            and self.y2 >= other.y1)

#
def place_entities(
        #
        room: RectangularRoom,
        #
        dungeon: GameMap,
        #
        maximum_monsters: int) -> None:
    # Set the number of monsters.
    number_of_monsters = random.randint(0, maximum_monsters)
    # For each monster:
    for i in range(number_of_monsters):
        # Set position x.
        x = random.randint(room.x1 + 1, room.x2 - 1)
        # Set position y.
        y = random.randint(room.y1 + 1, room.y2 - 1)
        # If there is not an entity at the specified position:
        if not any(entity.x == x and entity.y == y for entity in dungeon.entities):
            # If less than 80%:
            if random.random() < 0.8:
                # Plance an orc.
                entity_factories.orc.spawn(dungeon, x, y)
            else:
                # Place a troll.
                entity_factories.troll.spawn(dungeon, x, y)
    
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

#
def generate_dungeon2(
        # Maximum number of rooms.
        max_rooms: int,
        # Minimum room size.
        room_min_size: int,
        # Maximum room size.
        room_max_size: int,
        # Map width.
        map_width: int,
        # Map height.
        map_height: int,
        #
        max_monsters_per_room: int,
        # Player.
        player: Entity) -> GameMap:
    """Generate a new dungeon map."""
    # Create a game map.
    dungeon = GameMap(map_width, map_height, entities=[player])
    # Create a list to store room.
    rooms: List[RectangularRoom] = []
    # For 0 to the maximum number of rooms:
    for r in range(max_rooms):
        # Set room width.
        room_width = random.randint(room_min_size, room_max_size)
        # Set room height.
        room_height = random.randint(room_min_size, room_max_size)
        # Set room x position.
        x = random.randint(0, dungeon.width - room_width - 1)
        # Set room y position.
        y = random.randint(0, dungeon.height - room_height - 1)
        # Create a room.
        new_room = RectangularRoom(x, y, room_width, room_height)
        # If this room intersects with any other room:
        if any(new_room.intersects(other_room) for other_room in rooms):
            # Skip subsequent code, go to next attempt.
            continue
        # Carve out this room.
        dungeon.tiles[new_room.inner] = tile_types.floor
        # If this is the first room:
        if len(rooms) == 0:
            #
            player.x, player.y = new_room.center
        # Else:
        else:
            # For each position in the tunnel between the last room in the list and the new room.
            for x, y in tunnel_between(rooms[-1].center, new_room.center):
                # Carve out the position.
                dungeon.tiles[x, y] = tile_types.floor
        #
        place_entities(new_room, dungeon, max_monsters_per_room)
        # Append the new room to the list.
        rooms.append(new_room)
    #
    return dungeon

