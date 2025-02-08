"""Base object for generic crafting station."""


class BaseCraftingStation():
    """Basic class for crafting stations."""

    def __init__(self):
        """Initialize a new generic crafting station."""
        self._base_speed: float = 1.0
        self._base_prod: float = 1.0
        self._module_slots: int = 0
        self._modules = [None] * self._module_slots

    @property
    def modules(self):
        """Return list of current modules."""
        return list(self._modules)

    @modules.setter
    def modules(self, modules: tuple) -> None:
        """Set all module slots, overwriting existing slots."""
        n_modules = len(modules)
        if n_modules > self._module_slots:
            raise ValueError(f"This node takes at most {self._module_slots} modules")
        self._modules = list(modules) + [None] * (n_modules - self._module_slots)

    def add_module(self, module: str, index: int):
        """Add a module at a specific slot."""
        self._module_slots[index] = module

    @property
    def crafting_speed(self) -> float:
        """Effective crafting speed.

        Note that this is a property without a setter, since its calculated automatically
        given base speed, modules etc.
        """
        # TODO: Include beacons
        # TODO: Include science bonus (if applicable)
        speed_factor = 1 + sum(module["speed"] for module in self._modules)
        return self._base_speed * speed_factor

    @property
    def productivity(self) -> float:
        """Effective productivity.

        Note that this is a property without a setter, since its calculated automatically
        given base productivity, modules etc.
        """
        # TODO: Include science bonus (if applicable)
        prod_modules = sum(module["productivity"] for module in self._modules)
        return self._base_prod * prod_modules
