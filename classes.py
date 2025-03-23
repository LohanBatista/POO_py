# Father Class (Super Class) - Generalistc
class Game:
    #Class variables
    total_games = 0 

    #Contructor method
    def __init__(self,   name = "", yearLaunch = 0, multiplayer = False, note = 0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        Game.total_games +=1
        self.totalEvaluation = 0
        self.evaluators = 0

    #special methods
    def __str__(self):
        return f"\nGame: {self.name}"
    
    #instance methods
    def technical_sheet(self):
        print("###Game Data###")
        print(f"Name of the fame: {self.name}")
        print(f"Year of launch: {self.yearLaunch}")
        print(f"Multiplayer: {self.multiplayer}")
        print(f"Note: {self.note}\n")

    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1

    def average(self):
        print(f"Average note of the game {self.name}: {self.totalEvaluation / self.evaluators}")

# Derived Class (Subclass) - Specialized
class SinglePlayerGame(Game):
    def __init__(self, name="", yearLaunch=0, note=0, storyline=""):
        #subcsribe values from Super Class
        super().__init__(name, yearLaunch, multiplayer=False, note=note)
        self.storyline = storyline

    def technical_sheet(self):
        super().technical_sheet()
        print(f"Storyline: {self.storyline}\n")


class GameStudio:
    def __init__(self, name=""):
        self.name = name
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def evaluate_studio_quality(self):
        total_notes = sum(game.note for game in self.games)
        num_games = len(self.games)
        if num_games == 0:
            print(f"The studio {self.name} does not have launched games.")
        else:
            average_note = total_notes / num_games
            print(f"Average score from games of studio: {self.name}: {average_note:.2f}")