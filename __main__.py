from simulator import *

_logger = logger.get_logger(__name__)


def main():
    _logger.info("Blackjack Hall of Fame - Version 0.1")
    house_rules = HouseRules(
        decks_in_shoe=6,
        shuffle_mode=ShuffleMode.FISHER_YATES,
        dealer_hit_mode=DealerHitMode.ON_SIXTEEN,
        double_restrictions=DoubleRestrictions.NONE,
        double_after_split=DoubleAfterSplit.ALLOWED,
        aces_split_limit=AcesSplitLimit.THRICE,
        surrender_allowed=True,
        dealer_peek=True,
        blackjack_payout=1.5
    )
    game = Game(house_rules)


if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
