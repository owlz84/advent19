import networkx as nx
from collections import deque
from typing import List

DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]


class Navigator:
    def __init__(self, maze_map: str):
        self.maze_map = [[char for char in line] for line in maze_map.splitlines()]
        self.maze_dims = (len(self.maze_map), len(self.maze_map[0]))
        self.maze_graph = nx.Graph()
        self.summary_graph = nx.Graph()

    def build_graph(self):
        for rwix, rw in enumerate(self.maze_map):
            for colix, val in enumerate(rw):
                if val != "#":
                    self.maze_graph.add_node((rwix, colix), val=val)
                    for dx, dy in DIRECTIONS:
                        if self.check_valid_neighbour(colix, dx, dy, rwix):
                            self.maze_graph.add_edge((rwix, colix), (rwix + dx, colix + dy))

    def check_valid_neighbour(self, colix, dx, dy, rwix):
        return all([
            rwix + dx < self.maze_dims[0], rwix + dx >= 0,
            colix + dx < self.maze_dims[1], colix + dx >= 0
        ]) and self.maze_map[rwix + dx][colix + dy] != "#"

    def shortest_path(self):
        self.generate_summary_graph()
        queue = deque([("@", list(), 0)])
        goal = set(val for val in self.summary_graph.nodes if str.islower(val))
        paths = list()
        # graph_paths = dict(nx.all_pairs_dijkstra_path(self.summary_graph, weight="label"))
        graph_path_lengths = dict(nx.all_pairs_dijkstra_path_length(self.summary_graph, weight="label"))
        while len(queue) > 0:
            node, visited, distance = queue.popleft()
            visited += [node]
            keys = [n for n in visited if str.islower(n)]
            if set(keys) == goal:
                paths.append((visited, distance))
            for next_node, distance_to_next in graph_path_lengths[node].items():
                if next_node in visited:
                    continue
                if str.isupper(next_node) and next_node.lower() not in keys:
                    continue
                queue.append((next_node, visited, distance + distance_to_next))
        print(paths)
            # if set(keys) == goal:
            #     return node, parents, distance, work
            # if str.isupper(node) and node.lower() not in keys:
            #     queue.append((node, parents, distance))
            #     continue
            # else:
            #     for neighbour in self.summary_graph.neighbors(node):
            #         if neighbour not in discovered:
            #             discovered.append(neighbour)
            #             add_distance = self.summary_graph.get_edge_data(node, neighbour)["label"]
            #             queue.append((neighbour, parents + [node], distance + add_distance))


        # items = self.summary_graph.nodes
        # candidate_paths = list(p for p in permutations(items) if self.check_valid_order(p))
        # for graph_path in graph_paths:
        # path_lengths = list()
        # print(candidate_paths)
        # for path in candidate_paths:
        #     path_length = 0
        #     for ix, node in enumerate(path):
        #         if ix == 0:
        #             path_length = 0
        #         else:
        #             path_length += graph_path_lengths[node][path[ix-1]]
        #     path_lengths.append(path_length)

        # print(path_lengths)

    @staticmethod
    def check_valid_order(ordered_items):
        if ordered_items[0] != "@" or ordered_items[-1] != sorted(ordered_items)[-1]:
            return False
        keys = list()
        valid = True
        for item in ordered_items:
            if str.islower(item):
                keys += item
            if str.isupper(item):
                if item.lower() not in keys:
                    valid = False
                    break
        return valid

    def generate_summary_graph(self):
        start_node = None
        for node in self.maze_graph.nodes:
            if self.maze_graph.nodes[node]["val"] == "@":
                start_node = node
                break
        self.summary_graph.add_node("@")
        neighbours = list(self.maze_graph.neighbors(start_node))
        already_visited = [start_node]
        stack = list(zip(neighbours, ["@"] * len(neighbours)))
        path_length = 0
        while len(stack) > 0:
            node, last_item = stack.pop()
            if node not in already_visited:
                already_visited.append(node)
                path_length += 1
                current_item = self.maze_graph.nodes[node]["val"]
                if current_item != ".":
                    self.summary_graph.add_edge(self.maze_graph.nodes[node]["val"], last_item, label=path_length)
                    path_length = 0
                    last_item = current_item
                neighbours = list(self.maze_graph.neighbors(node))
                stack += list(zip(neighbours, [last_item] * len(neighbours)))
        return stack
