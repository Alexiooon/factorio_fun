"""PoC for modular implementation."""

import numpy as np


class Stream():
    """Stream of materials."""

    def __init__(self, name: str, max_quality: int = 3):
        """Initialize a new stream of materials."""
        self._name = name
        self._flow = np.array([0.] * max_quality)
        self.test = 0

    def __str__(self):
        """Name of the material in the stream."""
        return self.name

    @property
    def flow(self):
        """Flow of material per time unit."""
        return self._flow

    @flow.setter
    def flow(self, value: np.ndarray) -> None:
        """Update flow."""
        self._flow = value

    @property
    def name(self) -> str:
        """Name of the material."""
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Change the name of the material stream."""
        self._name = new_name


class EMPlant():
    """EM Plant."""

    module_slots = 4

    def __init__(self, speed: float = 1., prod: float = 0.):
        """Initialize a new generic node.

        Args:
         - speed (float): Base crafting speed of the station. Defaults to 1.
         - prod (float): Productivity bonus of the station, excluding modules. Defaults to 0.
        """
        self._speed = speed
        self._prod = prod
        self._input = {}

        self._prodmat: np.ndarray | None = None  # Production matrix


def main():
    """Main functionality."""


if __name__ == "__main__":
    main()
