"""Base object for generic crafting station."""

from ..modules import Module
from ..recipe import Recipe
from ..science import GlobalScienceProgress
from .beacon import Beacon


class BaseCraftingStation:
    """Basic class for crafting stations."""

    def __init__(self, recipe: Recipe | None = None, beacon: Beacon | None = None):
        """Initialize a new generic crafting station."""
        # Crafting station parameters
        self._base_speed: float = 1.0
        self._base_prod: float = 1.0

        # Modules
        self._module_slots = 0
        self._modules: list[Module] = [None] * self._module_slots

        # Beacon
        self.beacon = beacon

        # Crafting recipe
        self.recipe = recipe

    @property
    def modules(self):
        """Return list of current modules."""
        return self._modules

    @modules.setter
    def modules(self, modules: tuple) -> None:
        """Set all module slots, overwriting existing slots."""
        n_modules = len(modules)
        if n_modules > self._module_slots:
            raise ValueError(f"This node takes at most {self._module_slots} modules")
        if not all(isinstance(x, Module) for x in modules):
            raise TypeError("Modules must be an iterable of Module class instances.")
        self._modules = list(modules) + [None] * (self._module_slots - n_modules)

    def add_module(self, module: Module, index: int):
        """Add a module at a specific slot."""
        if not isinstance(module, Module):
            raise TypeError("Module must be an instance of the Module class.")

        self._modules[index] = module

    @property
    def crafting_speed(self) -> float:
        """Effective crafting speed.

        Note that this is a property without a setter, since its calculated automatically
        given base speed, modules etc.
        """
        beacon_speed = 0 if not self.beacon else self.beacon.output["speed"]
        module_speed = sum(module.speed for module in self._modules if module)
        speed_factor = 1 + module_speed + beacon_speed
        return self._base_speed * speed_factor

    @property
    def productivity(self) -> float:
        """Effective productivity.

        Note that this is a property without a setter, since its calculated automatically
        given base productivity, modules etc.
        """
        prod_science = (
            GlobalScienceProgress.get_research_level(self.recipe.name) / 10
        )  # 10% / level
        prod_modules = sum(module.productivity for module in self._modules if module is not None)
        return self._base_prod + prod_modules + prod_science

    @property
    def input(self) -> dict:
        """Get the input items and their quantities per second."""
        base_input = self.crafting_speed / self.recipe.time
        return {name: base_input * quantity for name, quantity in self.recipe.input.items()}

    @property
    def output(self) -> dict:
        """Get the output items and their quantities per second."""
        base_output = (self.crafting_speed / self.recipe.time) * self.productivity
        return {name: base_output * quantity for name, quantity in self.recipe.output.items()}
