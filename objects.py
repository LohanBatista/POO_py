from classes import Game, SinglePlayerGame, GameStudio

# game1 = Game("The Legend of Zelda: A Link to the Past", 1991, False, 10)
# game2 = Game("The Last of Us", 2013, True, 9.5)

# game1.technical_sheet()
# game2.technical_sheet()
# game1.evaluate(9.0)
# game1.evaluate(8.0)
# game1.average()
# game2.evaluate(7.0)
# game2.evaluate(8.0)
# game2.average()


# print(f"Total games: {Game.total_games}")

# mult_game = Game("The Last of Us", 2013, True, 9.5)
# mult_game.technical_sheet()

# sing_game = SinglePlayerGame("The Legend of Zelda: A Link to the Past", 1991, 10, "The story begins when an evil sorcerer named Agahnim kills the king of Hyrule, imprisons the descendants of the great sages in the Dark World, and takes over the kingdom for unknown reasons. Our hero Link, receiving a telepathic message from Princess Zelda, who tells him that she is locked in the dungeon of Hyrule Castle.")
# sing_game.technical_sheet()


game1 = Game("The Legend of Zelda: A Link to the Past", 1991, False, 10)
game2 = Game("The Last of Us", 2013, True, 9.5)

studio = GameStudio("Awesome Games")
studio.add_game(game1)
studio.add_game(game2)

studio.evaluate_studio_quality()

for game in studio.games:
    game.technical_sheet()

