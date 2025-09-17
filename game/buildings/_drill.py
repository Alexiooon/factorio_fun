"""Module for a generic drill/pumpjack."""

from ..recipe import Recipe
from .beacon import Beacon
from .crafting_station import BaseCraftingStation


class BaseDrill(BaseCraftingStation):
    """Base mining drill class."""

    def __init__(
        self,
        recipe: Recipe | None = None,
        beacon: Beacon | None = None,
    ):
        """Initialize a new drill."""
        super().__init__(recipe=recipe, beacon=beacon)
        self._resource_drain = 1.0

    def __str__(self) -> str:
        recipe = str(self.recipe) if self.recipe is not None else "Empty"
        return "Base Drill: " + recipe
