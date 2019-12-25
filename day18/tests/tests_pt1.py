import unittest
import networkx as nx
from graphviz import render
from day18.MazeNavigator import Navigator


class TestCase01(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/pt1_test1", "r") as fh:
            self.maze_map = fh.read()

    def test_shortest_path(self):
        navigator = Navigator(self.maze_map)
        # print(navigator.maze_map)
        navigator.build_graph()
        with open("test1.gv", "w+") as fh:
            nx.drawing.nx_agraph.write_dot(navigator.maze_graph, fh)

        render('dot', 'png', 'test1.gv')

        print(navigator.shortest_path())
        with open("test1_summary.gv", "w+") as fh:
            nx.drawing.nx_agraph.write_dot(navigator.summary_graph, fh)

        render('dot', 'png', 'test1_summary.gv')

        self.assertEqual(True, False)


class TestCase02(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/pt1_test2", "r") as fh:
            self.maze_map = fh.read()

    def test_shortest_path(self):
        navigator = Navigator(self.maze_map)
        navigator.build_graph()
        with open("test2.gv", "w+") as fh:
            nx.drawing.nx_agraph.write_dot(navigator.maze_graph, fh)

        render('dot', 'png', 'test2.gv')

        navigator.shortest_path()
        with open("test2_summary.gv", "w+") as fh:
            nx.drawing.nx_agraph.write_dot(navigator.summary_graph, fh)

        render('dot', 'png', 'test2_summary.gv')

        self.assertEqual(True, False)


class TestCase03(unittest.TestCase):
    def setUp(self) -> None:
        with open("../data/pt1_test3", "r") as fh:
            self.maze_map = fh.read()

    def test_shortest_path(self):
        navigator = Navigator(self.maze_map)
        navigator.build_graph()
        with open("test3.gv", "w+") as fh:
            nx.drawing.nx_agraph.write_dot(navigator.maze_graph, fh)

        render('dot', 'png', 'test3.gv')

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
