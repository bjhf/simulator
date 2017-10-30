import simulator
from .houserules import *
from .shoe import Shoe


class Game:
    _logger = simulator.logger.get_logger(__name__)
    _house_rules = None
    _shoe = None

    def __init__(self, house_rules: HouseRules):
        self._logger.info("New Game Loaded!")
        self._house_rules = house_rules
        self._logger.info(
            "House Rules: %s Decks in Shoe, Shuffle Mode: %s, Dealer Hits: %s",
            self._house_rules.decks_in_shoe,
            self._house_rules.shuffle_mode.name,
            self._house_rules.dealer_hit_mode.name
        )
        self.reset_game()

    def reset_game(self):
        _shoe = Shoe(self._house_rules.decks_in_shoe, self._house_rules.shuffle_mode)