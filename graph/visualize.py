"""Scripts for visualizing CraftingGraphs."""

import logging
import math
import os

import graphviz

from game.buildings import BaseCraftingStation

from .crafting_graph import CraftingGraph

OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_out")

# Default attributes for graphviz
GRAPH_ATTRIBUTES = {}
NODE_ATTRIBUTES = {
    "fillcolor": "lightgray",
    "shape": "rect",
    "style": "filled",
}
EDGE_ATTRIBUTES = {}

_logger = logging.getLogger(__name__)


# TODO (Alex): Use HTML for nicer formatting
def _get_node_label(node: BaseCraftingStation, node_data: dict) -> str:
    """Generate a node label."""
    # Title/header
    stations = node_data.get("stations")
    if stations is None:
        _logger.warning("Node %s has no 'stations' data", node)
        stations = 1
    header = str(math.ceil(stations)) + "x " + str(node)

    # Inputs
    input_items = "Input:"
    for item, quantity in node.input.items():
        input_items += rf"\l- {item}: {quantity * stations:.1f}/s"

    # Outputs
    output_items = "Output:"
    for item, quantity in node.output.items():
        output_items += rf"\l- {item}: {quantity * stations:.1f}/s"

    return r"\l".join([header, input_items, output_items, ""])  # An extra "\l" is needed at the end


def visualize(graph: CraftingGraph, filename: str = "graph"):
    """Convert graph to Graphviz for visualization."""
    dot = graphviz.Digraph(
        graph_attr=GRAPH_ATTRIBUTES,
        node_attr=NODE_ATTRIBUTES,
        edge_attr=EDGE_ATTRIBUTES,
        engine="dot",
    )

    # Nodes
    for node, data in graph.nodes.items():
        label = _get_node_label(node, data)
        dot.node(name=str(id(node)), label=label, labeljust="l")

    # Edges
    for a, b in graph.edges():
        dot.edge(tail_name=str(id(a)), head_name=str(id(b)))

    # Render and save
    filename = os.path.join(OUTPUT_PATH, filename)
    dot.render(filename=filename, view="dot")
    _logger.info("Graph saved to %s", filename)
