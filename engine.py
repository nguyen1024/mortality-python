#
from typing import Iterable

#
from typing import Any

#
from tcod.context import Context

#
from tcod.console import Console

#
from tcod.map import compute_fov

#
from entity import Entity

#
from game_map import GameMap

#
from input_handlers import EventHandler

class Engine:
    # Create initialiser function.
    def __init__(self, event_handler: EventHandler, game_map: GameMap, player: Entity):
        # Store event handler.
        self.event_handler = event_handler
        #
        self.game_map = game_map
        # Store player.
        self.player = player
        # Call function to update the field of view.
        self.update_fov()

    #
    def handle_enemy_turns(self) -> None:
        # For each entity except the player:
        for entity in self.game_map.entities - {self.player}:
            #
            print(f"The {entity.name} wonders when it will get to take a real turn.")

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
            #
            action.perform(self, self.player)
            # Let each non-player character have a turn.
            self.handle_enemy_turns()
            # Update the field of view.
            self.update_fov()

    #
    def update_fov(self) -> None:
        """
        Recompute the visible area based on the players point of view.
        """
        #
        self.game_map.visible[:] = compute_fov(
            # Pass transparent tiles.
            self.game_map.tiles["transparent"],
            # Pass player position.
            (self.player.x, self.player.y),
            # Pass how far the player can see.
            radius=8)
        # If a tile is "visible" then add it to "explored".
        self.game_map.explored |= self.game_map.visible

    # Create a render function.
    def render(self, console: Console, context: Context) -> None:
        #
        self.game_map.render(console=console)
        # Present the back buffer.
        context.present(console)
        # Clear the back buffer.
        console.clear()
