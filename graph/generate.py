"""Recursively delve through a crafting path to calculate input quantities."""

from game import Module, QualityLevel, Recipe
from game.buildings import (
    AssemblingMachine,
    BaseCraftingStation,
    Beacon,
    ChemicalPlant,
    CryogenicPlant,
    ElectricFurnace,
    ElectromagneticPlant,
    Foundry,
)

from .crafting_graph import CraftingGraph

_CRAFTING_STATION: dict[str:BaseCraftingStation] = {
    "Assembling machine": AssemblingMachine,
    "Chemical plant": ChemicalPlant,
    "Cryogenic plant": CryogenicPlant,
    "Electric furnace": ElectricFurnace,
    "Electromagnetic plant": ElectromagneticPlant,
    "Foundry": Foundry,
}

_SM3Epic = Module("Speed module 3", QualityLevel.EPIC)
_PM3Epic = Module("Productivity module 3", QualityLevel.EPIC)


def generate_graph(
    target_item: str,
    target_quantity: float,
    input_items: list[str],
    beacon: Beacon | None = None,
) -> CraftingGraph:
    """Generate a CraftingGraph from a target and input item."""

    def _generate(name: str, quantity: float, parent: BaseCraftingStation | None):
        """Generate the graph recursively."""
        # Set up the crafting station instance
        recipe = Recipe(name=name)
        station_name = recipe.recipe["station"]
        module = (_PM3Epic,) if "productivity" in recipe.recipe["modules"] else (_SM3Epic,)
        crafting_station = _CRAFTING_STATION[station_name](
            quality=QualityLevel.EPIC, recipe=recipe, beacon=beacon
        )
        crafting_station.modules = module * len(crafting_station.modules)

        # Calculate the amount of crafting stations needed
        n_stations = quantity / crafting_station.output[name]
        graph.add_node(crafting_station, stations=n_stations)
        if parent is not None:
            graph.add_edge(crafting_station, parent, **crafting_station.output)

        # Go through the input items
        for item in crafting_station.input:
            ingredient_quantity = crafting_station.input[item] * n_stations

            if item not in input_items:  # Delve deeper into the recipe graph
                _generate(
                    name=item,
                    quantity=ingredient_quantity,
                    parent=crafting_station,
                )

    graph = CraftingGraph()
    _generate(name=target_item, quantity=target_quantity, parent=None)

    return graph
