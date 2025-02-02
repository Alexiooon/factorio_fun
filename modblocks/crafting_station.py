"""Base object for generic crafting station."""


class BaseCraftingStation():
    """Basic class for crafting stations."""

    def __init__(self):
        """Initialize a new generic crafting station."""
        self.__base_speed: float = 1.0
        self.__base_prod: float = 1.0
        self.__module_slots: int = 0
        self.__modules = [None] * self.__module_slots

    @property
    def modules(self):
        """Return list of current modules."""
        return list(self.__modules)

    @modules.setter
    def modules(self, modules: tuple) -> None:
        """Set all module slots, overwriting existing slots."""
        n_modules = len(modules)
        if n_modules > self.__module_slots:
            raise ValueError(f"This node takes at most {self.__module_slots} modules")
        self.__modules = list(modules) + [None] * (n_modules - self.__module_slots)

    def add_module(self, module: str, index: int):
        """Add a module at a specific slot."""
        self.__module_slots[index] = module

    @property
    def crafting_speed(self) -> float:
        """Effective crafting speed.

        Note that this is a property without a setter, since its calculated automatically
        given base speed, modules etc.
        """
        # TODO: Include beacons
        # TODO: Include science bonus (if applicable)
        speed_factor = 1 + sum(module["speed"] for module in self.__modules)
        return self.__base_speed * speed_factor

    @property
    def productivity(self) -> float:
        """Effective productivity.

        Note that this is a property without a setter, since its calculated automatically
        given base productivity, modules etc.
        """
        # TODO: Include science bonus (if applicable)
        prod_modules = sum(module["productivity"] for module in self.__modules)
        return self.__base_prod * prod_modules
