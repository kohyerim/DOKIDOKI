__author__ = "@kohyerim"

from . import constants as c

# use in tools.Control.update temporarily
# function working


class Level:
    def __init__(self):
        self.level = 1

    def level_up(self):
        self.level += 1

    def level_calculator(self, score):  # final_score : level1.game_info[c.SCORE])
        if self.level == 1 and score < 3000:
            return c.OVER
        elif self.level == 1 and score >= 3000:
            self.level_up()
            return c.CONTINUE

        elif self.level == 2 and 3000 < score < 7000:
            return c.OVER

        elif self.level == 2 and score >= 7000:
            self.level_up()
            return c.CONTINUE

        elif self.level == 3 and 7000 < score < 14000:
            return c.OVER

        elif self.level == 3 and score >= 14000:
            self.level_up()
            return c.CONTINUE
