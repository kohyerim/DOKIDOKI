__author__ = 'justinarmstrong'

from . import setup, tools
from .states import main_menu, load_screen, level1, level2, level3, level4
from . import constants as c


def main():
    """Add stage(level) here"""
    """Add states to control here."""
    run_it = tools.Control(setup.ORIGINAL_CAPTION)
    state_dict = {c.MAIN_MENU: main_menu.Menu(),
                  c.LOAD_SCREEN: load_screen.LoadScreen(),
                  c.TIME_OUT: load_screen.TimeOut(),
                  c.GAME_OVER: load_screen.GameOver(),
                  c.LEVEL1: level1.Level1(),
                  c.LEVEL2: level2.Level2(),
                  c.LEVEL3: level3.Level3(),
                  c.LEVEL4: level4.Level4(),
                  c.ENDING: load_screen.Ending(),
                  c.TOSTAGE2: load_screen.ToStage2(),
                  c.TOSTAGE3: load_screen.ToStage3(),
                  c.TOSTAGE4: load_screen.ToStage4()}
    run_it.setup_states(state_dict, c.MAIN_MENU)
    run_it.main()


