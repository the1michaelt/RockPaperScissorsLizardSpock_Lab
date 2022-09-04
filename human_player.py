from players import Player

class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def choose_gesture(self):
        selected_choice =  self.choice[(int(input(f'''Choose your gesture, 1-5: 
        1: {self.choice[0]}
        2: {self.choice[1]}
        3: {self.choice[2]}
        4: {self.choice[3]}
        5: {self.choice[4]}
        ''')))-1]
        return selected_choice