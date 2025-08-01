"""Module for assembling machines."""

from ..recipe import Recipe
from .beacon import Beacon
from .crafting_station import BaseCraftingStation

SPEED_BY_QUALITY = (1.25, 1.625, 2.0, 2.375, 3.125)


class AssemblingMachine(BaseCraftingStation):
    """Assembling Machine 3 class."""

    def __init__(
        self,
        quality: int,
        recipe: Recipe | None = None,
        modules: tuple | None = None,
        beacon: Beacon | None = None,
    ):
        """Initialize a new Assembling Machine 3."""
        super().__init__(recipe=recipe, beacon=beacon)
        self._base_speed: float = SPEED_BY_QUALITY[quality]
        self._base_prod: float = 1.0
        self._module_slots: int = 4
        self._modules = [None] * self._module_slots
        if modules:
            self.modules = modules

    def __str__(self) -> str:
        """String representation i.e. name of the crafting station + recipe."""
        recipe = str(self.recipe) if self.recipe is not None else "Empty"
        return "Assembling machine 3: " + recipe
