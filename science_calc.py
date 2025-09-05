"""Script for calculating base resources needed for making science packs."""

import argparse
import json

from game import GlobalScienceProgress, Module, QualityLevel
from game.buildings import Beacon
from graph import CraftingGraph, generate_graph, visualize

TARGET_RATE = 10000 / 60  # Science packs per second per type
SCIENCE_PROGRESS_FILE = "science_progress.json"

SM3Epic = Module("Speed module 3", QualityLevel.EPIC)
BEACON = Beacon(quality=QualityLevel.EPIC, modules=(SM3Epic,) * 2, quantity=2)

PLANETS = [
    "Nauvis",
    "Fulgora",
    "Vulcanus",
    "Aquillo",
]


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
    "Aquillo": ["Cryogenic science pack"],
}


def do_science(name: str, planet: str) -> CraftingGraph:
    """Big think."""
    graph = generate_graph(name, TARGET_RATE, INPUT_ITEMS[planet], BEACON, reduce=True)

    return graph


def get_args() -> argparse.Namespace:
    """Get input arguments."""
    args = argparse.ArgumentParser()

    args.add_argument(
        "--draw",
        "-d",
        action="store_true",
        required=False,
        default=False,
        help="Generate graphviz visualization",
    )

    return args.parse_args()


def main():
    """Main entry point for the script."""
    args = get_args()

    # Set research levels for bonus productivity
    with open(SCIENCE_PROGRESS_FILE, "r", encoding="utf8") as _file:
        dat = json.load(_file)
    GlobalScienceProgress.load(dat)

    # Run simulation for each planet
    for planet in PLANETS:
        global_input = {item: 0.0 for item in INPUT_ITEMS[planet]}
        for science_pack in SCIENCE_TYPES[planet]:
            graph = do_science(science_pack, planet)

            if args.draw:
                visualize(graph)

            for node, data in graph.nodes.items():
                for item in global_input:
                    global_input[item] += node.input.get(item, 0) * data.get("stations")

        # Print the summary
        print(f"\n\n========== Summary {planet} ==========")
        print(f"Target science: {TARGET_RATE:.1f}/s ({TARGET_RATE * 60:.0f}/min)\n")
        for name, flow in global_input.items():
            print(f"{name}: {flow:.1f}/s")


if __name__ == "__main__":
    main()
