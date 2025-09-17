"""Module for Electric mining drills."""

from ..recipe import Recipe
from ._drill import BaseDrill
from .beacon import Beacon

_RESOURCE_DRAIN = (1.0, 0.83, 0.66, 0.50, 0.16)


class ElectricMiningDrill(BaseDrill):
    """Electric mining drill class."""

    def __init__(
        self,
        quality: int,
        recipe: Recipe | None = None,
        modules: tuple | None = None,
        beacon: Beacon | None = None,
    ):
        """Initialize a new Electric mining drill."""
        super().__init__(recipe=recipe, beacon=beacon)
        self._base_speed: float = 0.5
        self._base_prod: float = 1.0
        self._resource_drain: float = _RESOURCE_DRAIN[quality]
        self._module_slots: int = 3
        self._modules = [None] * self._module_slots
        if modules:
            self.modules = modules

    def __str__(self) -> str:
        """String representation i.e. name of the crafting station + recipe."""
        recipe = str(self.recipe) if self.recipe is not None else "Empty"
        return "Electric Mining Drill: " + recipe
