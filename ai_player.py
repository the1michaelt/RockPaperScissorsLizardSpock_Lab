from players import Player
import random

class AiPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Player 2"

    def choose_gesture(self):
        bot_selects = random.choice(self.choice)
        return bot_selects