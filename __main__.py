from simulator import *

_logger = logger.get_logger(__name__)

def main():
    _logger.info("Blackjack Hall of Fame - Version 0.1")
    house_rules = HouseRules(
        decks_in_shoe=6,
        shuffle_mode=ShuffleMode.NO_SHUFFLE,
        dealer_hit_mode=DealerHitMode.ON_SIXTEEN
    )
    game = Game(house_rules)


if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
