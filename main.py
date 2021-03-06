#
import copy

# Import The Chronicles of Doryen Library.
import tcod

#
from engine import Engine

#
import entity_factories

#
from input_handlers import EventHandler

#
from proc_gen import generate_dungeon2

#
def main():
        # Set screen width.
        screen_width = 80
        # Set screen height.
        screen_height = 50
        # Set map width.
        map_width = 80
        # Set map height.
        map_height = 50
        # Set the maximum room size.
        room_max_size = 10
        # Set the minimum room size.
        room_min_size = 6
        # Set the maximum number of room.
        max_rooms = 30
        # Set the maximum number of monsters per room.
        max_monsters_per_room = 2
        # Set font.
        tileset = tcod.tileset.load_tilesheet("dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)
        # Create an event handler object.
        event_handler = EventHandler()
        # Create a copy of a player entity.
        player = copy.deepcopy(entity_factories.player)
        
        # Create a game map.
        game_map = generate_dungeon2(
                max_rooms=max_rooms,
                room_min_size=room_min_size,
                room_max_size=room_max_size,
                map_width=map_width,
                map_height=map_height,
                max_monsters_per_room=max_monsters_per_room,
                player=player)
        # Create an engine.
        engine = Engine(event_handler=event_handler, game_map=game_map, player=player)
        # Create a screen.
        with tcod.context.new_terminal(
                        screen_width,
                        screen_height,
                        tileset=tileset,
                        title="Mortality",
                        vsync=True,) as context:
                # Create a console.
                root_console = tcod.Console(
                        screen_width,
                        screen_height,
                        order="F")
                # Begin game loop.
                while True:
                        #
                        engine.render(console=root_console, context=context)
                        #
                        events = tcod.event.wait()
                        #
                        engine.handle_events(events)
                       
#
if __name__ == "__main__":
        #
	main()
