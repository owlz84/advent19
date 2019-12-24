import networkx as nx
from itertools import chain
from math import ceil


class Formula:
    def __init__(self, lhs, rhs):
        self.lhs = self.parse(lhs)
        self.rhs = self.parse(rhs)

    @staticmethod
    def parse(unit):
        return [(k, int(v)) for v, k in [
                tuple(unit.split(" ")) for unit in unit.split(", ")]]

    @property
    def edges(self):
        rhs_elem, rhs_ratio = self.rhs[0]
        return [(rhs_elem, lh_elem, dict(label=(rhs_ratio, lh_ratio))) for lh_elem, lh_ratio in self.lhs]


class Calculator:
    def __init__(self, formula_inputs):
        self.formulae = [Formula(*formula_input.split(" => ")) for formula_input in formula_inputs]
        self.dependency_graph = nx.DiGraph()
        self.dependency_graph.add_edges_from(list(chain.from_iterable(formula.edges for formula in self.formulae)))

    @property
    def ore_requirement(self):
        for node in nx.topological_sort(self.dependency_graph):
            parents = list(self.dependency_graph.predecessors(node))
            if len(parents) == 0:
                self.dependency_graph.nodes[node]["label"] = dict(name=node, value=1)
            else:
                parent_weights = [self.dependency_graph[parent][node]["label"] for parent in parents]
                parent_values = [self.dependency_graph.nodes[parent]["label"]["value"] for parent in parents]
                value = sum(
                    dst_wt * ceil(src_val / src_wt) for (src_wt, dst_wt), src_val in zip(parent_weights, parent_values))
                self.dependency_graph.nodes[node]["label"] = dict(name=node, value=value)
        return self.dependency_graph.nodes['ORE']['label']['value']




