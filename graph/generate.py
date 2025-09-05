"""Tools to generate and manipulate crafting graphs."""

import copy
from collections import Counter

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
    reduce: bool = True,
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

    if reduce:
        graph = reduce_graph(graph)

    return graph


def reduce_graph(g: CraftingGraph) -> CraftingGraph:
    """Merge identical nodes/crafting stations while preserving edges."""
    g_new = CraftingGraph(g)

    names = Counter([str(node) for node in g.nodes])
    names = {k: v for k, v in names.items() if v > 1}  # If theres only one, no duplicates exist

    for name in names:
        new_node = None
        new_data = {}

        # Create the new node and sum data
        nodes_to_merge = []
        for node, data in g.nodes(data=True):
            if str(node) != name:
                continue
            nodes_to_merge.append(node)

            # Create a new node as a deep copy
            if new_node is None:
                new_node = copy.deepcopy(node)

            # Append old data
            for k, v in data.items():
                if k not in new_data:
                    new_data[k] = 0
                new_data[k] += v

        g_new.add_node(new_node, **new_data)

        # Move edges
        edges_to_move = list(g_new.out_edges(keys=True, data=True)) + list(
            g_new.in_edges(keys=True, data=True)
        )
        for u, v, k, data in edges_to_move:
            if u in nodes_to_merge:
                g_new.add_edge(new_node, v, key=k, **data)
            elif v in nodes_to_merge:
                g_new.add_edge(u, new_node, key=k, **data)

        # Remove old node (and edges automatically)
        for node in nodes_to_merge:
            g_new.remove_node(node)

    return g_new
