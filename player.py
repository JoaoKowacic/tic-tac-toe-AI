

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s input our move(0-8):')
            try:
                val = int(square)
                valid_square = True
                if val not in game.avaliable_moves():
                    raise ValueError
            except ValueError:
                print("invalid number")

        return val
