"""Beacon module."""

from .modules import Module

EFFICIENCY_BY_QUALITY = (1.5, 1.7, 1.9, 2.1, 2.5)


class Beacon:
    """Beacon emitting modules at high efficiency."""

    def __init__(self, quality: int, modules: tuple | None = None, quantity: int = 1):
        """Initialize a new beacon."""
        self._transmission_efficiency = EFFICIENCY_BY_QUALITY[quality]
        self.quantity = quantity  # Number of beacons this instance represents
        self._module_slots = 2
        self._modules: list[Module] = [None] * self._module_slots
        if modules:
            self.modules = modules

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
    def output(self) -> dict:
        """Effective output."""
        net_effect = self._transmission_efficiency * self.quantity**0.5
        output = {
            "energy_consumption": net_effect
            * sum(module.energy_consumption for module in self._modules if module),
            "pollution": net_effect * sum(module.pollution for module in self._modules if module),
            "quality": net_effect * sum(module.quality for module in self._modules if module),
            "speed": net_effect * sum(module.speed for module in self._modules if module),
        }
        return output
