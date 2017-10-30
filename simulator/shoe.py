from math import floor
import simulator
from itertools import product
from .enum import *
from .util import print_cards
from random import random


class Shoe:
    _logger = simulator.logger.get_logger(__name__)
    _decks_in_shoe = None
    _shuffle_mode = None
    _cut_card_position = None
    _cards = []

    def __init__(self, decks_in_shoe: int, shuffle_mode: ShuffleMode):
        self._decks_in_shoe = decks_in_shoe
        self._shuffle_mode = shuffle_mode
        self.reset_shoe()

    def reset_shoe(self):
        fresh_deck = [(rank | suit) for (rank, suit) in product(
            [Card.SPADE, Card.DIAMOND, Card.CLUB, Card.HEART],
            [Card.ACE, Card.TWO, Card.THREE, Card.FOUR, Card.FIVE, Card.SIX, Card.SEVEN, Card.EIGHT, Card.NINE,
             Card.TEN, Card.JACK, Card.QUEEN, Card.KING]
        )]
        fresh_shoe = []
        for x in range(0, self._decks_in_shoe):
            fresh_shoe.extend(fresh_deck)
        self._cards = self.shuffle(fresh_shoe)

    def shuffle(self, input_cards):
        if self._shuffle_mode is ShuffleMode.FISHER_YATES:
            back_deck_swap_index = len(input_cards)
            while back_deck_swap_index > 1:
                i = int(floor(random() * back_deck_swap_index))
                back_deck_swap_index -= 1
                input_cards[i], input_cards[back_deck_swap_index] = input_cards[back_deck_swap_index], input_cards[i]
        elif self._shuffle_mode is ShuffleMode.NO_SHUFFLE:
            return input_cards
