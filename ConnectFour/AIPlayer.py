#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    """ inherits from Player class
    """
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    
    def __repr__(self):
        """ returns a string representing an AIPlayer object
        """
        return 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
    
    
    def max_score_column(self, scores):
        """ takes a list scores containing a score for each 
            column of the board, and that returns the index of 
            the column with the maximum score
        """
        max_scores = []
        max_score = max(scores)
        for score in range(len(scores)):
            if scores[score] == max_score:
                max_scores += [score]
        if self.tiebreak == 'LEFT':
            return max_scores[0]
        if self.tiebreak == 'RIGHT':
            return max_scores[-1]
        return random.choice(max_scores)
    
    
    def scores_for(self, b):
        """ takes a Board object, b, and determines the called 
            AIPlayer‘s scores for the columns in b, returning 
            a list containing one score for each column
        """
        scores = [50] * b.width
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opp = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opp.scores_for(b)
                if max(opp_scores) == 0:
                    scores[col] = 100
                elif max(opp_scores) == 100:
                    scores[col] = 0
                else:
                    scores[col] = 50 
                b.remove_checker(col)
        return scores
                
                
                
    def next_move(self, b):
        """ returns the called AIPlayer‘s judgment of its 
            best possible move
        """
        return self.max_score_column(self.scores_for(b))
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                