class Player:
    def __init__(self):
        """
        Instance Variables:

        names : str
        points_earned : int

        Methods:

        choice(): will be overridden and will vary beteween player types, dictates what players choose as gestures 
        """
        self.name = ""
        self.choice = ["Lizard", "Spock", "Rock", "Paper", "Scissors"]
        self.points_earned = 0
    
    def choose_gesture(self):
        pass