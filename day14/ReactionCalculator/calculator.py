from typing import List, Tuple
import networkx as nx
from itertools import chain
from math import ceil


class Formula:
    def __init__(self, lhs, rhs):
        self.lhs = self.parse(lhs)
        self.rhs = self.parse(rhs)

    @staticmethod
    def parse(unit) -> List[Tuple[str, int]]:
        return [(k, int(v)) for v, k in [
                tuple(unit.split(" ")) for unit in unit.split(", ")]]

    @property
    def edges(self) -> List[Tuple[str, str, dict]]:
        rhs_elem, rhs_qty = self.rhs[0]
        return [(rhs_elem, lh_elem, dict(ratio=(rhs_qty, lh_qty))) for lh_elem, lh_qty in self.lhs]


class Calculator:
    def __init__(self, formula_inputs: List[str]):
        self.formulae = [Formula(*formula_input.split(" => ")) for formula_input in formula_inputs]
        self.dependency_graph = nx.DiGraph()
        self.dependency_graph.add_edges_from(list(chain.from_iterable(formula.edges for formula in self.formulae)))

    def ore_requirement(self, fuel_units: int = 1) -> int:
        for node in nx.topological_sort(self.dependency_graph):
            parents = list(self.dependency_graph.predecessors(node))
            if len(parents) == 0:
                self.dependency_graph.nodes[node]["qty"] = fuel_units
            else:
                parent_weights = [self.dependency_graph[parent][node]["ratio"] for parent in parents]
                parent_values = [self.dependency_graph.nodes[parent]["qty"] for parent in parents]
                value = sum(
                    dst_wt * ceil(src_val / src_wt)
                    for (src_wt, dst_wt), src_val
                    in zip(parent_weights, parent_values)
                )
                self.dependency_graph.nodes[node]["qty"] = value
        return self.dependency_graph.nodes["ORE"]["qty"]

    def fuel_per_qty_ore(self, ore_units: int = 1) -> int:
        min_fuel = 0
        fuel = 1
        while True:
            required = self.ore_requirement(fuel)
            if required > ore_units:
                break
            min_fuel = fuel
            fuel *= 2
        max_fuel = fuel
        while True:
            required = self.ore_requirement(fuel)
            if abs(max_fuel - min_fuel) <= 1:
                break
            elif required < ore_units:
                min_fuel = fuel
                fuel += (max_fuel - min_fuel) // 2
            else:
                max_fuel = fuel
                fuel -= (max_fuel - min_fuel) // 2
        required = self.ore_requirement(min_fuel)
        print(f"producing {min_fuel} unit(s) of fuel requires {required} unit(s) of ore")
        return min_fuel




