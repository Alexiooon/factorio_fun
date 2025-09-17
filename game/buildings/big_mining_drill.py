"""Module for big mining drills."""

from ..recipe import Recipe
from ._drill import BaseDrill
from .beacon import Beacon

_RESOURCE_DRAIN = (0.5, 0.41, 0.33, 0.25, 0.08)


class BigMiningDrill(BaseDrill):
    """Big mining drill class."""

    def __init__(
        self,
        quality: int,
        recipe: Recipe | None = None,
        modules: tuple | None = None,
        beacon: Beacon | None = None,
    ):
        """Initialize a new Big mining drill."""
        super().__init__(recipe=recipe, beacon=beacon)
        self._base_speed: float = 2.5
        self._base_prod: float = 1.0
        self._resource_drain: float = _RESOURCE_DRAIN[quality]
        self._module_slots: int = 4
        self._modules = [None] * self._module_slots
        if modules:
            self.modules = modules

    def __str__(self) -> str:
        """String representation i.e. name of the crafting station + recipe."""
        recipe = str(self.recipe) if self.recipe is not None else "Empty"
        return "Big Mining Drill: " + recipe
