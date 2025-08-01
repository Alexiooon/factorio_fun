"""Scripts for visualizing CraftingGraphs."""

import os

import graphviz

from .crafting_graph import CraftingGraph

OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_out")


def visualize(graph: CraftingGraph, filename="mygraph"):
    """Convert graph to Graphviz for visualization."""
    dot = graphviz.Digraph(engine="dot")

    for node in graph.nodes():
        dot.node(name=str(id(node)), label=str(node), style="filled", shape="rect")

    for a, b in graph.edges():
        dot.edge(str(id(a)), str(id(b)))

    dot.render(filename=os.path.join(OUTPUT_PATH, filename), view="dot")
