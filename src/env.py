import gym
from gym import spaces
import numpy as np

class JokerEnv(gym.Env):
    metadata = {}

    def __init__(self):
        # Observations are dictionaries containing the player's hand
        self.observation_space = spaces.Dict(
            {
                # all can be any card or no card (meaning that the current player is the first to play)
                "in_play": spaces.MultiDiscrete([37, 37, 37]), # 0-36, 36 = no card
                "wild_suit": spaces.Discrete(4),
                # "wild_value": spaces.Discrete(10), # 0-9
                "players": spaces.Dict(
                    {
                        "0": spaces.Dict(
                            {
                                # the first one is 36 since the player must have at least one card in possesion when taking an action
                                "hand": spaces.MultiDiscrete([36, 37, 37, 37, 37, 37, 37, 37, 37]), 
                                "desired": spaces.Discrete(10), # 0-9
                                "taken": spaces.Discrete(10), # 0-9
                            }        
                        ),
                        "1": spaces.Dict(
                            {
                                "desired": spaces.Discrete(10), # 0-9
                                "taken": spaces.Discrete(10), # 0-9
                            }        
                        ),
                        "2": spaces.Dict(
                            {
                                "desired": spaces.Discrete(10), # 0-9
                                "taken": spaces.Discrete(10), # 0-9
                            }        
                        ),
                        "3": spaces.Dict(
                            {
                                "desired": spaces.Discrete(10), # 0-9
                                "taken": spaces.Discrete(10), # 0-9
                            }        
                        ),
                        
                    }
                ),
                # "jokers_remaining": spaces.Discrete(3), # 0-2
                # "gone": spaces.MultiBinary(36)
                # "scores": spaces.MultiDiscrete([10, 10, 10, 10]),
                # others scores (who does it benefit to hurt)
                # premia 
            }
        )

        # Actions represent the card that a player chooses to play.
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
        self.action_space = spaces.Discrete(36)