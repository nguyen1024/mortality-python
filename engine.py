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
from entity import Entity

#
from game_map import GameMap

#
from input_handlers import EventHandler

class Engine:
    # Create initialiser function.
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, game_map: GameMap, player: Entity):
        # Store entities.
        self.entities = entities
        # Store event handler.
        self.event_handler = event_handler
        #
        self.game_map = game_map
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
            action.perform(self, self.player)

    # Create a render function.
    def render(self, console: Console, context: Context) -> None:
        #
        self.game_map.render(console=console)
        # For each entity:
        for entity in self.entities:
            # Print entity in the back buffer.
            console.print(entity.x, entity.y, entity.char, fg=entity.color)
        # Present the back buffer.
        context.present(console)
        # Clear the back buffer.
        console.clear()
