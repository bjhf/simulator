from .houserules import *
from .shoe import Shoe


class Game:
    _logger = simulator.util.logger.get_logger(__name__)
    _house_rules = None
    _shoe = None

    def __init__(self, house_rules: HouseRules):
        self._logger.info("New Game Loaded!")
        self._house_rules = house_rules
        self._logger.info("House Rules:")
        self._logger.info("\t      Decks in Shoe %s", self._house_rules.decks_in_shoe)
        self._logger.info("\t       Shuffle Mode %s", self._house_rules.shuffle_mode.name)
        self._logger.info("\t    Dealer Hit Mode %s", self._house_rules.dealer_hit_mode.name)
        self._logger.info("\tDouble Restrictions %s", self._house_rules.double_restrictions.name)
        self._logger.info("\t Double After Split %s", self._house_rules.double_after_split.name)
        self._logger.info("\t         Split Aces %s", self._house_rules.aces_split_limit.name)
        self._logger.info("\t  Surrender Allowed %s", self._house_rules.surrender_allowed)
        self._logger.info("\t       Dealer Peeks %s", self._house_rules.dealer_peek)
        self._logger.info("\t   Blackjack Payout %s", self._house_rules.blackjack_payout)
        self.reset_game()

    def reset_game(self):
        _shoe = Shoe(self._house_rules.decks_in_shoe, self._house_rules.shuffle_mode)