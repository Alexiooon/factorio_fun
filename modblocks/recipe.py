"""Module for setting crafting recipes."""
import json
import os
from collections.abc import Mapping

# Path to recipes data file, defined relative to this file
RECIPE_DATA_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "data", "recipes.json")
)

# Dictionary with all recipes. Loaded at first call of the recipe class
_RECIPES: dict | None = None


def _load_json() -> dict:
    """Load JSON file with recipes."""
    global _RECIPES  # noqa: PLW0603 - TODO: Maybe make a singleton instead later...
    with open(RECIPE_DATA_PATH, "r", encoding="utf8") as _file:
        _RECIPES = dict(json.load(_file))


class Recipe(Mapping):
    """Crafting recipe object.

    Class defining a single crafting recipe, which is set at initialization by
    its name. A KeyError will be raised if the recipe cannot be found.

    It has the following attributes:
      recipe (dict): Contains the actual recipe data.
      name (str):    Name of the crafting recipe.
      time (float):  Base crafting time of the recipe.
      input (dict):  Input items and their quantities.
      output (dict): Output items and their quantities.

    Since it inherits from the Mapping ABC, it can be treated as an immutable
    dictionary - What goes into the recipe (components, crafting time etc.)
    cannot be altered. The recipe itself can be changed though by simply
    updating the "recipe" attribute.

    For the dictionary part, it can be subscriptable to get any of its relevant
    attributes, e.g. recipe("Sulfur")["input"] gets the inputs to Sulfur recipe.
    """

    def __init__(self, name: str):
        """Initialize a new recipe instance."""
        # Load recipe data if not done already.
        if _RECIPES is None:
            _load_json()

        self.recipe = name
        self._name = name
        super().__init__()

    def __getitem__(self, key: str):
        """Get item from recipe dictionary object."""
        if key == "name":
            return self.name  # Workaround since "name" is not in the recipe dict
        return self.recipe[key]

    def __iter__(self):
        """Iterate over recipe keys like a dictionary."""
        for key in self.recipe.keys():
            yield key

    def __len__(self):
        """Length of recipe dictionary."""
        return len(self.recipe.keys())

    @property
    def recipe(self) -> dict:
        """Return current recipe."""
        return self._recipe

    @recipe.setter
    def recipe(self, name: str):
        """Set a new recipe."""
        try:
            self._recipe = _RECIPES[name]
            self._name = name
        except KeyError:
            raise KeyError(f"No recipe with the name {name}")

    @property
    def input(self) -> dict:
        """Dictionary with input items as keys and quantity as values."""
        return self["input"]

    @property
    def output(self) -> dict:
        """Dictionary with output items as keys and quantity as values."""
        return self["output"]

    @property
    def time(self) -> float:
        """Base crafting time."""
        return self["time"]

    @property
    def name(self) -> str:
        """Name of the crafting recipe."""
        # TODO: Should probably be included in the .json file for consistency
        return self._name
