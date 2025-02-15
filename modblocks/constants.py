"""Static data/constants."""

from enum import IntEnum


class QualityLevel(IntEnum):
    """Integer representation of quality levels.

    These are designed for ease of use with iterables where each element is a
    quality level, in order.
    """
    NORMAL = 0
    UNCOMMON = 1
    RARE = 2
    EPIC = 3
    LEGENDARY = 4
