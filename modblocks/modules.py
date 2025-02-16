"""Classes for all tiers of effectivity/productivity/quality/speed modules."""
import json
import os

from .constants import QualityLevel

# Load data from JSON file
# See the JSON file specified by the path below for format
MODULE_DATA_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "data", "modules.json")
)

# Dictionary with all modules. Loaded at first call of the recipe class
_MODULES: dict | None = None


def _load_json() -> dict:
    """Load JSON file with recipes."""
    global _MODULES  # noqa: PLW0603 - TODO: Maybe make a singleton instead later...
    with open(MODULE_DATA_PATH, "r", encoding="utf8") as _file:
        _MODULES = dict(json.load(_file))


class Module():
    """Base class for all tiers and types of modules."""

    energy_consumption = 0.
    pollution = 0.
    productivity = 0.
    quality = 0.
    speed = 0.

    def __init__(self, name: str, quality: QualityLevel):
        """Initialize module."""
        # Load module data if not done already.
        if _MODULES is None:
            _load_json()

        # Validate input
        if name not in _MODULES.keys():
            # ValueError also seems reasonable, but I want to be consistent with the fact that
            # its a dictionary lookup
            raise KeyError(f"No module type named {name}")
        if quality not in [ql.value for ql in QualityLevel]:
            # Same reasoning as above
            raise IndexError(f"Invalid quality level: {quality}")

        self.energy_consumption = _MODULES[name]["energy_consumption"][quality]
        self.pollution = _MODULES[name]["pollution"][quality]
        self.productivity = _MODULES[name]["productivity"][quality]
        self.quality = _MODULES[name]["quality"][quality]
        self.speed = _MODULES[name]["speed"][quality]
