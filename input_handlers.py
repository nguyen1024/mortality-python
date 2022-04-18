# 
from typing import Optional

#
import tcod.event

#
from actions import Action

#
from actions import EscapeAction

#
from actions import MovementAction

# Sub-class EventDispatched.
# Create class EventHandler.
class EventHandler(tcod.event.EventDispatch[Action]):
        # Create method ev_quit.
        # Override ev_quit in class EventDispatched.
        def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
                # Exit the program.
                raise SystemExit()

        # Create method ev_keydown.
        def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
                #
                action: Optional[Action] = None
                # Store the key that was pressed.
                key = event.sym
                # If key up:
                if key == tcod.event.K_UP:
                        # Create a movement action.
                        action = MovementAction(dx=0, dy=-1)
                # Else if key down:
                elif key == tcod.event.K_DOWN:
                        # Create movement action.
                        action = MovementAction(dx=0, dy=1)
                # Else if key left:
                elif key == tcod.event.K_LEFT:
                        # Create movement action.
                        action = MovementAction(dx=-1, dy=0)
                # Else if key right:
                elif key == tcod.event.K_RIGHT:
                        # Create movement action.
                        action = MovementAction(dx=1, dy=0)
                # Else if key escape:
                elif key == tcod.event.K_ESCAPE:
                        # Create escape action.
                        action = EscapeAction()
                # Return action.
                return action
