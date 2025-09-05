"""Graph representation of sequences of crafting stations.

Utilizes the networkx module.
"""

# TODO (Alex): Expand docstring
from typing import Iterable

import networkx as nx

from game.buildings import BaseCraftingStation


class CraftingGraph(nx.MultiDiGraph):
    """Node representing one or multiple instances of a crafting station."""

    def add_node(self, node_for_adding: BaseCraftingStation, **attr):
        """Add a crafting station to the graph in the form of a node.

        Just validates instance type then calls super.add_node().

        Args:
          node_for_adding: Crafting station instance.
          attr: Additional data.
        """
        if not isinstance(node_for_adding, BaseCraftingStation):
            raise TypeError("Node must be an instance of BaseCraftingStation or its subclasses")

        return super().add_node(node_for_adding, **attr)

    def add_nodes_from(self, nodes_for_adding: Iterable[BaseCraftingStation], **attr):
        """Add crafting stations to the graph from an iterable.

        Just validates instance type then calls super.add_nodes_from().

        Args:
          nodes_for_adding: Iterable of crafting stations.
          attr: Additional data.
        """
        if not all(isinstance(node, BaseCraftingStation) for node in nodes_for_adding):
            raise TypeError("Node must be an instance of BaseCraftingStation or its subclasses")

        return super().add_nodes_from(nodes_for_adding, **attr)
