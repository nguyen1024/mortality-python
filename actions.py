#
from __future__ import annotations

#
from typing import TYPE_CHECKING

#
if TYPE_CHECKING:
        #
        from engine import Engine
        #
        from entity import Entity

#
class Action:
        #
        def perform(self, engine: Engine, entity: Entity) -> None:
                """Perform this action with the objects needed to determine its scope.
                `engine` is the scope this action is being performed in.
                `entity` is the object performing the action.
                This method must be overridden by Action subclasees"""
                # 
                raise NotImplementedError()

#
class EscapeAction(Action):
        #
        def perform(self, engine: Engine, entity: Entity) -> None:
                # Exit the program.
                raise SystemExit()

#
class MovementAction(Action):
        #
        def __init__(self, dx: int, dy: int):
                #
                super().__init__()
                #
                self.dx = dx
                #
                self.dy = dy

        #
        def perform(self, engine: Egine, entity: Entity) -> None:
                # Calculate destination x.
                dest_x = entity.x + self.dx
                # Calculate destination y.
                dest_y = entity.y + self.dy
                # If the destination is not in bounds:
                if not engine.game_map.in_bounds(dest_x, dest_y):
                        # Return early.
                        return
                # If the destination is not walkable:
                if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
                        # Return early.
                        return
                # Move entity.
                entity.move(self.dx, self.dy)
