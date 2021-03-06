import unittest
from WeakVertices import Vertex, SimpleGraph


class TestUM(unittest.TestCase):
    def test_empty_list(self):
        self.size = 0
        self.sg = SimpleGraph(self.size)
        self.assertEqual(self.sg.WeakVertices(), [])

    def test_loop(self):
        #    A
        #   / \
        #  B   C
        #   \ /
        #    D
        self.size = 4
        self.sg = SimpleGraph(self.size)
        self.sg.AddVertex("A")
        self.sg.AddVertex("B")
        self.sg.AddVertex("C")
        self.sg.AddVertex("D")
        self.sg.AddEdge(0, 1)  # A + B
        self.sg.AddEdge(0, 2)  # A + C
        self.sg.AddEdge(1, 3)  # B + D
        self.sg.AddEdge(2, 3)  # C + D
        self.assertEqual(
            self.sg.m_adjacency,
            [
                [0, 1, 1, 0],
                [1, 0, 0, 1],
                [1, 0, 0, 1],
                [0, 1, 1, 0],
            ],
        )
        self.assertEqual(
            [x.Value for x in self.sg.WeakVertices()],
            ['A', 'B', 'C', 'D'],
        )


    def test(self):
        self.size = 10
        self.sg = SimpleGraph(self.size)
        self.sg.AddVertex("A")
        self.sg.AddVertex("B")
        self.sg.AddVertex("C")
        self.sg.AddVertex("D")
        self.sg.AddVertex("E")
        self.sg.AddVertex("F")
        self.sg.AddVertex("G")
        self.sg.AddVertex("H")
        self.sg.AddVertex("I")
        self.sg.AddVertex("J")

        self.assertEqual(self.sg.m_adjacency, [[0] * self.size for _ in range(self.size)])

        #    A---------B  J
        #   / \        |
        #  C---D-------F--G
        #   \ /         \ |
        #    E        I---H
        #
        #  B and I points are weak vertices

        self.sg.AddEdge(0, 1)  # A + B
        self.sg.AddEdge(0, 2)  # A + C
        self.sg.AddEdge(0, 3)  # A + D

        self.sg.AddEdge(1, 5)  # B + F

        self.sg.AddEdge(2, 3)  # C + D
        self.sg.AddEdge(2, 4)  # C + E

        self.sg.AddEdge(3, 4)  # D + E
        self.sg.AddEdge(3, 5)  # D + F

        self.sg.AddEdge(5, 6)  # F + G
        self.sg.AddEdge(5, 7)  # F + H

        self.sg.AddEdge(6, 7)  # G + H

        self.sg.AddEdge(7, 8)  # H + I

        self.assertEqual(
            self.sg.m_adjacency,
            [
                [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                [1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
                [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0, 0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
        )

        self.assertEqual(
            [x.Value for x in self.sg.WeakVertices()],
            ['B', 'I', 'J'],
        )


if __name__ == "__main__":
    unittest.main()
