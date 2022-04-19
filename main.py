# Import The Chronicles of Doryen Library.
import tcod

#
from engine import Engine

#
from entity import Entity

#
from input_handlers import EventHandler

#
from proc_gen import generate_dungeon

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
        # Set font.
        tileset = tcod.tileset.load_tilesheet("dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)
        # Create an event handler object.
        event_handler = EventHandler()
        # Create a player entity.
        player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
        # Create a non-player character entitiy.
        npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
        # Put entities into a set.
        entities = {npc, player}
        # Create a game map.
        game_map = generate_dungeon(map_width, map_height)
        # Create an engine.
        engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)
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
