"""Script for calculating base resources needed for making science packs."""

import json

from game import GlobalScienceProgress, Module, QualityLevel, Recipe
from game.buildings import (
    AssemblingMachine,
    BaseCraftingStation,
    Beacon,
    Biochamber,
    ChemicalPlant,
    CryogenicPlant,
    ElectricFurnace,
    ElectromagneticPlant,
    Foundry,
)

TARGET_RATE = 10000 / 60  # Science packs per second per type
SCIENCE_PROGRESS_FILE = "science_progress.json"

PM2Rare = Module("Productivity module 2", QualityLevel.RARE)
PM3Epic = Module("Productivity module 3", QualityLevel.EPIC)
SM3Rare = Module("Speed module 3", QualityLevel.RARE)
SM3Epic = Module("Speed module 3", QualityLevel.EPIC)
BEACON = Beacon(quality=QualityLevel.EPIC, modules=(SM3Epic,) * 2, quantity=2)

PLANETS = ["Nauvis", "Fulgora", "Vulcanus", "Gleba", "Aquillo"]

INPUT_ITEMS = {
    "Nauvis": [
        "Iron plate",
        "Copper plate",
        "Steel plate",
        "Stone",
        "Stone brick",
        "Coal",
        "Electronic circuit",
        "Advanced circuit",
        "Processing unit",
        "Petroleum",
        "Lubricant",
        "Water",
    ],
    "Fulgora": [
        "Iron plate",
        "Copper plate",
        "Electronic circuit",
        "Plastic bar",
        "Battery",
        "Holmium ore",
        "Stone",
        "Heavy oil",
        "Water",
    ],
    "Gleba": [
        "Bioflux",
        "Pentapod egg",
    ],
    "Vulcanus": [
        "Lava",
        "Calcite",
        "Coal",
        "Tungsten ore",
        "Sulfuric acid",
    ],
    "Aquillo": [
        "Ice",
        "Solid fuel",
        "Holmium plate",
        "Ammonia",
        "Lithium brine",
        "Fluorine",
    ],
}

CRAFTING_STATION: dict[str:BaseCraftingStation] = {
    "Assembling machine": AssemblingMachine,
    "Biochamber": Biochamber,
    "Chemical plant": ChemicalPlant,
    "Cryogenic plant": CryogenicPlant,
    "Electric furnace": ElectricFurnace,
    "Electromagnetic plant": ElectromagneticPlant,
    "Foundry": Foundry,
}

SCIENCE_TYPES = {
    "Nauvis": [
        "Automation science pack",
        "Logistic science pack",
        "Chemical science pack",
        "Military science pack",
        "Production science pack",
        "Utility science pack",
    ],
    "Fulgora": ["Electromagnetic science pack"],
    "Vulcanus": ["Metallurgic science pack"],
    "Gleba": ["Agricultural science pack"],
    "Aquillo": ["Cryogenic science pack"],
}


def generate_graph(
    name: str,
    output_quantity: float,
    output_dict: dict[str:float],
    station_count: dict[str:float],
    planet: str,
):
    """Recursively generate a graph of input items."""
    # Define the stuff
    recipe = Recipe(name=name)
    station_name = recipe.recipe["station"]
    crafting_station = CRAFTING_STATION[station_name](
        quality=QualityLevel.EPIC, recipe=recipe, beacon=BEACON
    )
    modules = (PM3Epic,) if "productivity" in recipe.recipe["modules"] else (SM3Epic,)
    crafting_station.modules = modules * len(crafting_station.modules)

    # Calculate the amount of crafting stations needed
    factor = output_quantity / crafting_station.output[name]
    if name not in station_count:
        station_count[name] = 0.0
    station_count[name] += factor

    # Calculate the input flows
    for item in crafting_station.input:
        ingredient_quantity = crafting_station.input[item] * factor

        if item not in INPUT_ITEMS[planet]:  # Delve deeper into the recipe graph
            generate_graph(
                name=item,
                output_quantity=ingredient_quantity,
                output_dict=output_dict,
                station_count=station_count,
                planet=planet,
            )
        else:  # Append into the total inputs
            if item not in output_dict:
                output_dict[item] = 0.0
            output_dict[item] += ingredient_quantity


def do_science(name: str, planet: str) -> dict:
    """Big think."""
    local_input = {}  # Updated within generate_graph
    station_count = {}  # Updated within generate_graph
    print(f"\n========== {name} ==========")
    generate_graph(name, TARGET_RATE, local_input, station_count, planet)
    print("Input:")
    for key, val in local_input.items():
        print(f"  {key}: {val:.1f}/s")
    print("Crafting stations:")
    for key, val in station_count.items():
        print(f"  {key}: {val:.1f}")
    return local_input


def main():
    """Main entry point for the script."""
    # Set research levels for bonus productivity
    with open(SCIENCE_PROGRESS_FILE, "r", encoding="utf8") as _file:
        dat = json.load(_file)
    GlobalScienceProgress.load(dat)

    # Run simulation for each planet
    for planet in PLANETS:
        global_input = {item: 0.0 for item in INPUT_ITEMS[planet]}
        for science_pack in SCIENCE_TYPES[planet]:
            local_input = do_science(science_pack, planet)
            for name, flow in local_input.items():
                global_input[name] += flow

        # Print the summary
        print(f"\n\n========== Summary {planet} ==========")
        print(f"Target science: {TARGET_RATE:.1f}/s ({TARGET_RATE * 60:.0f}/min)\n")
        for name, flow in global_input.items():
            print(f"{name}: {flow:.1f}/s")


if __name__ == "__main__":
    main()
