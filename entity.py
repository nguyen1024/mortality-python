#
from __future__ import annotations

#
import copy

#
from typing import Tuple

#
from typing import TypeVar

#
from typing import TYPE_CHECKING

#
if TYPE_CHECKING:
        from game_map import GameMap

#
T = TypeVar("T", bound="Entity")

class Entity:
        """
        A generic object to represent players, enemies, items, etc.
        """
        # Create initialise menthod.
        def __init__(
                        #
                        self,
                        #
                        x: int = 0,
                        #
                        y: int = 0,
                        #
                        char: str = "?",
                        #
                        color: Tuple[int, int, int] = (255, 255, 255),
                        #
                        name: str = "<Unnamed>",
                        #
                        blocks_movement: bool = False):
                self.x = x
                self.y = y
                self.char = char
                self.color = color
                self.name = name
                self.blocks_movement = blocks_movement

        #
        def spawn(
                        #
                        self: T,
                        #
                        game_map: GameMap,
                        #
                        x: int,
                        #
                        y: int) -> T:
                """Spawn a copy of this instance at the specified location."""
                #
                clone = copy.deepcopy(self)
                # Set position x.
                clone.x = x
                # Set position y.
                clone.y = y
                # Add the clone to the game map.
                game_map.entities.add(clone)
                #
                return clone
                

        #
        def move(self, dx: int, dy: int) -> None:
                self.x += dx
                self.y += dy

