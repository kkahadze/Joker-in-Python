import random
from src.player import Player
from src.game import Game

from agents.random_caller_random_player import RandomCallerRandomPlayer
from src.utils import int_to_card, card_to_int

def test_init():
    game = Game()
    assert game is not None
    assert game.players[0].number == 0 and game.players[1].number == 1 and game.players[2].number == 2 and game.players[3].number == 3
    assert game.players[0].hand is not None and game.players[1].hand is not None and game.players[2].hand is not None and game.players[3].hand is not None

    game = Game([Player(6), Player(7), Player(8), Player(9)])
    assert game is not None
    assert game.players[0].number == 6 and game.players[1].number == 7 and game.players[2].number == 8 and game.players[3].number == 9
    assert game.players[0].hand is not None and game.players[1].hand is not None and game.players[2].hand is not None and game.players[3].hand is not None

def test_reset_vars():
    # The following test makes sure that reset_vars() 
    # resets deck, players, round, play, dealer, wild_suit, jokers_remaining, in_play

    game = Game([Player(6), Player(7), Player(8), Player(9)])
    game.reset_vars()
    assert game is not None
    assert game.players[0].number == 6 and game.players[1].number == 7 and game.players[2].number == 8 and game.players[3].number == 9
    assert game.players[0].hand is not None and game.players[1].hand is not None and game.players[2].hand is not None and game.players[3].hand is not None
    assert game.round == 1
    assert game.play == 1
    assert game.dealer == (game.first_to_play - 1) % 4

def test_get_num_to_deal(): # add more tests
    game = Game(only_nines=True)
    game.reset_vars()
    assert game.get_num_to_deal() == 9

    game = Game() 
    game.reset_vars()
    assert game.get_num_to_deal() == 1

    game = Game()
    game.reset_vars()
    game.round = 2
    assert game.get_num_to_deal() == 9

    game = Game()
    game.reset_vars()
    game.round = 3
    assert game.get_num_to_deal() == 8

    game = Game()
    game.reset_vars()
    game.round = 4
    assert game.get_num_to_deal() == 9

    game = Game()
    game.reset_vars()
    game.round = 1
    game.play = 5
    assert game.get_num_to_deal() == 5

    game = Game()
    game.reset_vars()
    game.round = 1
    game.play = 8
    assert game.get_num_to_deal() == 8

    game = Game()
    game.reset_vars()
    game.round = 3
    game.play = 8
    assert game.get_num_to_deal() == 1

    game = Game()
    game.reset_vars()
    game.round = 3
    game.play = 2
    assert game.get_num_to_deal() == 7

    game = Game(only_nines=True)
    game.reset_vars()
    for round in range(1, 5):
        for play in range(1, 5):
            assert game.get_num_to_deal() == 9

def test_get_calls():
    # This function tests the get_calls() function in game.py to assure that it sets the calls of each player to a valid int corresponding to
    # the type of agent
    game = Game([RandomCallerRandomPlayer(0), RandomCallerRandomPlayer(1), RandomCallerRandomPlayer(2), RandomCallerRandomPlayer(3)])
    game.reset_vars()
    game.get_calls()
    for player_num in range(game.first_to_play, game.first_to_play + 4):
        game.deck.deal(game.players[player_num % 4].hand, times = game.get_num_to_deal()) # player num needs to be modded to get the correct players
    calls = game.get_calls()

    assert calls[0] >= 0 and calls[0] <=1
    assert calls[1] >= 0 and calls[1] <=1
    assert calls[2] >= 0 and calls[2] <=1
    assert calls[3] >= 0 and calls[3] <=1

def test_deal():
    # This function tests the deal() function in game.py to assure that it deals the correct number of cards to each player
    game = Game([RandomCallerRandomPlayer(0), RandomCallerRandomPlayer(1), RandomCallerRandomPlayer(2), RandomCallerRandomPlayer(3)])
    game.reset_vars()
    game.get_calls()
    game.deal()

    assert len(game.players[0].hand) == 1
    assert len(game.players[1].hand) == 1
    assert len(game.players[2].hand) == 1
    assert len(game.players[3].hand) == 1
    
    assert game.players[0].hand[0] != game.players[1].hand[0] and game.players[0].hand[0] != game.players[2].hand[0] and game.players[0].hand[0] != game.players[3].hand[0]

    game = Game([RandomCallerRandomPlayer(0), RandomCallerRandomPlayer(1), RandomCallerRandomPlayer(2), RandomCallerRandomPlayer(3)], only_nines=True)
    game.reset_vars()
    game.get_calls()
    game.deal()

    assert len(game.players[0].hand) == 9
    assert len(game.players[1].hand) == 9
    assert len(game.players[2].hand) == 9
    assert len(game.players[3].hand) == 9

    assert game.players[0].hand[0] != game.players[1].hand[0] and game.players[0].hand[0] != game.players[2].hand[0] and game.players[0].hand[0] != game.players[3].hand[0]

def test_reset_play():
    # This function tests the reset_play() function in game.py to assure that it resets the played variable to an
    #  empty list and resets the first suit
    game = Game([RandomCallerRandomPlayer(0), RandomCallerRandomPlayer(1), RandomCallerRandomPlayer(2), RandomCallerRandomPlayer(3)])
    game.reset()
    action = 1
    card = int_to_card(action)
    game.add_play(card_to_int(card))

        
    game.pre_plays()

    if game.is_done():
        return
            
    game.reset_play()

    assert game.in_play == []
    assert game.first_suit == 4

def test_pre_plays():
    # This function tests the pre_plays() function in game.py to assure that it finishes the play
    assert True

def test_add_play():
    # This function tests the add_play() function in game.py to assure that it adds the correct card to the in_play list
    game = Game([RandomCallerRandomPlayer(0), RandomCallerRandomPlayer(1), RandomCallerRandomPlayer(2), RandomCallerRandomPlayer(3)])
    game.reset()
    game.deal()
    action = 1
    card = int_to_card(action)
    game.add_play(card)
    assert game.in_play[0] == card

    game.reset()
    game.deal()
    card = random.choice(game.players[game.first_to_play].hand)
    game.add_play(card)
    assert game.in_play[0] == int_to_card(action)
    assert game.in_play[0] not in game.players[game.first_to_play].hand

def test_is_done():
    # This function tests the is_done() function in game.py to assure that it returns True when the game is done and False when it is not
    game = Game([RandomCallerRandomPlayer(0), RandomCallerRandomPlayer(1), RandomCallerRandomPlayer(2), RandomCallerRandomPlayer(3)], only_nines=True)
    game.reset_vars()
    game.deal()
    card = random.choice(game.players[game.first_to_play].hand)
    game.add_play(card)
    assert game.is_done() == False

    game = Game([RandomCallerRandomPlayer(0), RandomCallerRandomPlayer(1), RandomCallerRandomPlayer(2), RandomCallerRandomPlayer(3)], only_nines=True)
    game.reset_vars()
    game.play = 4
    game.round = 4
    game.update_play()
    assert game.is_done() == True

    game = Game([RandomCallerRandomPlayer(0), RandomCallerRandomPlayer(1), RandomCallerRandomPlayer(2), RandomCallerRandomPlayer(3)], only_nines=False)
    print("game.deal_amounts: ", game.deal_amounts)
    game.reset_vars()
    game.play = 8
    game.round = 3
    game.update_play()
    assert game.is_done() == False

    game.round = 4
    game.play = 4
    game.update_play()
    assert game.is_done() == True

