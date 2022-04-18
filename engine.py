#
from typing import Set

#
from typing import Iterable

#
from typing import Any

#
from tcod.context import Context

#
from tcod.console import Console

#
from actions import EscapeAction

#
from actions import MovementAction

#
from entity import Entity

#
from input_handlers import EventHandler

class Engine:
    # Create initialiser function.
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, player: Entity):
        # Store entities.
        self.entities = entities
        # Store event handler.
        self.event_handler = event_handler
        # Store player.
        self.player = player

    # Create an event handler.
    def handle_events(self, events: Iterable[Any]) -> None:
        # For each event:
        for event in events:
            # Send event to the event handler.
            action = self.event_handler.dispatch(event)
            # If there is no action:
            if action is None:
                # Skip over the remaining code.
                continue
            # Else if there is a movement action:
            elif isinstance(action, MovementAction):
                # Move the player.
                self.player.move(dx=action.dx, dy=action.dy)
            # Else if there is an escape action:
            elif isinstance(action, EscapeAction):
                # Exit the program.
                raise SystemExit()

    # Create a render function.
    def render(self, console: Console, context: Context) -> None:
        # For each entity:
        for entity in self.entities:
            # Print entity in the back buffer.
            console.print(entity.x, entity.y, entity.char, fg=entity.color)
        # Present the back buffer.
        context.present(console)
        # Clear the back buffer.
        console.clear()
