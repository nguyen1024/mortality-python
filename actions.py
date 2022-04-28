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
class ActionWithDirection(Action):
        #
        def __init__(self, dx: int, dy: int):
                #
                super().__init__()
                #
                self.dx = dx
                #
                self.dy = dy

        #
        def perform(self, engine: Engine, entity: Entity) -> None:
                #
                raise NotImplementedError()

#
class MeleeAction(ActionWithDirection):
        #
        def perform(self, engine: Engine, entity: Entity) -> None:
                # Calculate destination x.
                dest_x = entity.x + self.dx
                # Calculate destination y.
                dest_y = entity.y + self.dy
                # Get the blocking entity at the specified location
                target = engine.game_map.get_blocking_entity_at_location(dest_x, dest_y)
                # If there is no blocking entity:
                if not target:
                        # Return early.
                        return
                # Print diagnostic.
                print(f"You kick the {target.name}, much to its annoynance!")

#
class MovementAction(ActionWithDirection):
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
                # If the destination has a blocking entity:
                if engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
                        # Return early.
                        return
                # Move entity.
                entity.move(self.dx, self.dy)

#
class BumpAction(ActionWithDirection):
        #
        def perform(self, engine: Engine, entity: Entity) -> None:
                # Calculate x destination.
                dest_x = entity.x + self.dx
                # Calculate y destination.
                dest_y = entity.y + self.dy
                # If there is a blocking entity at the specified location:
                if engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
                        # Hit the entity at the specified location.
                        return MeleeAction(self.dx, self.dy).perform(engine, entity)
                # Else:
                else:
                        # Move into the specified location.
                        return MovementAction(self.dx, self.dy).perform(engine, entity)
