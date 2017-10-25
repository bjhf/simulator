import simulator
from .enum import *

class HouseRules:
    decks_in_shoe = int
    shuffle_mode = ShuffleMode
    dealer_hit_mode = DealerHitMode
    _logger = simulator.logger.get_logger(__name__)

    def __init__(self, decks_in_shoe: int, shuffle_mode: ShuffleMode, dealer_hit_mode: DealerHitMode):
        self._logger.info("blah")
        self.decks_in_shoe = decks_in_shoe
        self.shuffle_mode = shuffle_mode
        self.dealer_hit_mode = dealer_hit_mode
