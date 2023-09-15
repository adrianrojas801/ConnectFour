#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.
class Player:
    
    def __init__(self, checker):
        """ constructs a new Player object by initializing the
            attribute checker that represents the gamepiece 
            for the playerand an attribute num_moves that 
            stores how many moves the player has made so far
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
        
    def __repr__(self):
        """ returns a string representing a Player object 
            indicating which checker the Player object is 
            using
        """
        return 'Player ' + self.checker
    
    
    def opponent_checker(self):
        if self.checker == 'X':
            return 'O'
        return 'X'
    
    
    def next_move(self, b):
        """ returns the column where the player wants to make 
            the next move
        """
        self.num_moves += 1 
        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col) == False:
                print('Try again!')
            else: 
                break
        return col
    