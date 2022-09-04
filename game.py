
from ai_player import AiPlayer
from human_player import HumanPlayer

class Game:
    def __init__(self):
        self.user_1 = HumanPlayer("Player 1")
        self.user_2 = self.choose_opponent() 


    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.play_game()


    def display_welcome(self):
        print("\n Wanna play Rock, Paper, Scissors, Lizard, and Spock? \n")

    def choose_rounds(self):
        options = [3, 5, 7, 9] 
       
        selected_option = options[(int(input('''Choose the amount of rounds: 
        1: 3 rounds
        2: 5 round
        3: 7 rounds
        4: 9 rounds
        '''))) - 1]
    
        if options == 0 or 1 or 2 or 3:
            return selected_option
        else:
            self.choose_rounds()

    def choose_opponent(self):
        who_you_chose = int(input('''Choose your opponent: AI (Computer) or Multiplayer (another Human)
        1: Ai
        2: Multiplayer
        '''))
        if who_you_chose == 1:
            return AiPlayer()

        elif who_you_chose == 2:
            return HumanPlayer("Player 2")

        else:
            self.choose_opponent()#works with integers but not letters

    def display_rules(self):
        print('''Remember the rules: 
Scissors cuts Paper, Scissors decapitates Lizard
Paper covers Rock, Paper disproves Spock
Rock crushes Lizard, Rock crushes Scissors
Lizard poisons Spock, Lizard eats Paper
Spock smashes Scissors, Spock vaporizes Rock

Ready to play?
''')

    def round_for_user(self):
        self.user_1.points_earned += 1
        print(f"{self.user_1.name} won the round and has {self.user_1.points_earned} points total.")             
                
                        
    def play_game(self):
        number_of_rounds = self.choose_rounds()
        current_round = 0
        while current_round < number_of_rounds:         
            current_round += 1
            print(f'''
Round {current_round}:
{self.user_1.name} choose gesture: ''')

            player_one_choice = self.user_1.choose_gesture()
            print(f"{self.user_2.name} choose gesture:")
            user_2_choice = self.user_2.choose_gesture()

            if player_one_choice== "Lizard" and (user_2_choice== "Spock" or user_2_choice == "Paper"):
                self.round_for_user()

            elif player_one_choice== "Rock" and (user_2_choice== "Scissors" or user_2_choice== "Lizard"): 
                self.round_for_user()

            elif player_one_choice== "Scissors" and (user_2_choice == "Paper" or user_2_choice == "Lizard"):  
                self.round_for_user()
        
            elif player_one_choice== "Spock" and (user_2_choice== "Scissors" or user_2_choice== "Rock"):  
                self.round_for_user()

            elif player_one_choice== "Paper" and (user_2_choice== "Rock" or user_2_choice== "Spock"): 
                self.round_for_user()

            elif player_one_choice== user_2_choice:
                current_round -= 1
                print("Tie. Replaying the round")

            else:
                self.user_2.points_earned += 1
                print(f"{self.user_2.name} won the round and has {self.user_2.points_earned} points total.")

            print(f"\n{self.user_1.name} chose {player_one_choice}") 
            print(f"{self.user_2.name} chose {user_2_choice}") 
        
            current_round = self.display_winner(number_of_rounds, current_round) 


    def game_over(self):
        print("\nGAME OVER")
        print(f"{self.user_1.name} won {self.user_1.points_earned} rounds")
        print(f"{self.user_2.name} won {self.user_2.points_earned} rounds")
  

    def display_winner(self, number_of_rounds, current_round):
        thatvar = False
        if self.user_1.points_earned >= (number_of_rounds / 2):
            print("\n" + f"{self.user_1.name} WINS")
            self.game_over()
            thatvar = True
        
        elif self.user_2.points_earned >= (number_of_rounds / 2):
            print(f"{self.user_2.name} wins!")
            self.game_over()
            thatvar = True
           
        if thatvar == True:
            current_round = number_of_rounds
            return current_round
        else:
            current_round = current_round
            return current_round
        