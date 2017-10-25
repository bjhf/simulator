from enum import Enum, auto


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
