#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#   

from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b
def process_move(p, b):
    """ takes a Player object, p , for the player whose move 
        is being processed, and a Board object, b, for the 
        board on which the game is being played. The function 
        will make a single move by player p on board b
    """
    print(str(p) +"'s turn")
    print()
    next_col = p.next_move(b)
    if b.can_add_to(next_col) == True:
        b.add_checker(p.checker, next_col)
    print()
    print(b)
    if b.is_win_for(p.checker) == True:
        print(p, 'wins in', p.num_moves ,'moves')
        print('Congratulations!')
        return True
    if b.is_win_for(p.checker) == True and b.is_win_for(p.opponent_checker()) == True:
        print("It's a tie!")
        return True
    if b.is_full() == True:
        print("It's a tie!")
        return True
    if b.is_win_for(p.checker) == False:
        return False

class RandomPlayer(Player):
    """ inherits from Player class
    """
    def next_move(slef, b):
        """ randomly selects a non-full column to play
        """
        available = []
        for col in range(b.width):
            if b.can_add_to(col):
                available += [col]
        return random.choice(available)
    














































