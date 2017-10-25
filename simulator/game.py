import simulator
from .houserules import *


class Game:
    _logger = simulator.logger.get_logger(__name__)
    house_rules = None

    def __init__(self, house_rules: HouseRules):
        self._logger.info("New Game Loaded!")
        self.house_rules = house_rules
        self._logger.info(
            "House Rules: %s Decks in Shoe, Shuffle Mode: %s, Dealer Hits: %s",
            self.house_rules.decks_in_shoe,
            self.house_rules.shuffle_mode.name,
            self.house_rules.dealer_hit_mode.name
        )

