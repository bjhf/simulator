from enum import Enum, Flag, auto


class ShuffleMode(Enum):
    NO_SHUFFLE = auto()
    FISHER_YATES = auto()


class DealerHitMode(Enum):
    ON_SIXTEEN = auto()
    ON_SOFT_SEVENTEEN = auto()


class SplitAcesLimit(Enum):
    ONCE = auto()
    TWICE = auto()
    THRIVE = auto()


class Card(Flag):
    SPADE = auto()
    DIAMOND = auto()
    CLUB = auto()
    HEART = auto()
    ACE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()
    ISHIGH = auto()
