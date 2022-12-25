from src.utils import suit_count, least_common_suit_in_hand, wildsuit_count

class RuleBasedAgent():
    def __init__(self, env):
        self.env = env

    # SUIT: DIAMONDS    CLUBS   HEARTS    SPADES
    # VALUES
    # 6:        0         1       2         3
    # 7:        4         5       6         7
    # 8:        8         9       10        11
    # 9:        12        13      14        15
    # 10:       16        17      18        19
    # JACK:     20        21      22        23
    # QUEEN:    24        25      26        27
    # KING:     28        29      30        31
    # ACE:      32        33      34        35
        
    def act(self, observation):
        unimplemented()

    def choose_how_to_play_joker(self, observation):
        '''
        Returns the best way to play the joker given the current observation, 
        0 - 3 = ვიში/Highest (Diamonds to Spades), 
        4-7 = წაიღოს/Take (Diamonds to Spades), 
        8 = Play Default
        9 = Play Under
        '''

        # Variables that the optimal play of a Joker depends on

        if first_to_play(observation):
            if want_to_win(observation):
                return 4 + choose_suit_for_highest()
            else:
                return choose_suit_for_take()
        else: # second, third or fourth to play
            if want_to_win(observation):
                return 8
            else:
                return 9