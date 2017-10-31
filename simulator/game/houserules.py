import simulator
from simulator.util.enum import *

class HouseRules:
    decks_in_shoe = int
    shuffle_mode = ShuffleMode
    dealer_hit_mode = DealerHitMode
    double_restrictions = DoubleRestrictions
    double_after_split = DoubleAfterSplit
    aces_split_limit = AcesSplitLimit
    surrender_allowed = None
    dealer_peek = None
    blackjack_payout = None
    _logger = simulator.util.logger.get_logger(__name__)

    def __init__(self, decks_in_shoe: int, shuffle_mode: ShuffleMode, dealer_hit_mode: DealerHitMode,
                 double_restrictions: DoubleRestrictions, double_after_split: DoubleAfterSplit,
                 aces_split_limit: AcesSplitLimit, surrender_allowed: bool, dealer_peek: bool,
                 blackjack_payout: float):
        self.decks_in_shoe = decks_in_shoe
        self.shuffle_mode = shuffle_mode
        self.dealer_hit_mode = dealer_hit_mode
        self.double_restrictions = double_restrictions
        self.double_after_split = double_after_split
        self.aces_split_limit = aces_split_limit
        self.surrender_allowed = surrender_allowed
        self.dealer_peek = dealer_peek
        self.blackjack_payout = blackjack_payout
