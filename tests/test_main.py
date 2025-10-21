import unittest
from math import isclose
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import TreeNode, BinaryTreeNode, Point, Circle, Polygon

class TestTreeStructures(unittest.TestCase):

    def test_add_and_find_child(self):
        root = TreeNode("root")
        child = TreeNode("child")
        root.add_child(child)
        self.assertEqual(root.find("child"), child)

    def test_remove_child_by_value(self):
        root = TreeNode("root")
        child1 = TreeNode("a")
        child2 = TreeNode("b")
        root.add_child(child1)
        root.add_child(child2)
        root.remove_child_by_value("a")
        self.assertIsNone(root.find("a"))

    def test_dfs_traversal_order(self):
        root = TreeNode("root")
        child1 = TreeNode("a")
        child2 = TreeNode("b")
        root.add_child(child1)
        root.add_child(child2)
        output = []
        def capture(node): output.append(node.value)
        TreeNode.traverse_dfs = lambda self: [capture(self)] + [child.traverse_dfs() for child in self.children]
        root.traverse_dfs()
        self.assertEqual(output, ["root", "a", "b"])

    def test_bfs_traversal_order(self):
        root = TreeNode("root")
        child1 = TreeNode("a")
        child2 = TreeNode("b")
        root.add_child(child1)
        root.add_child(child2)
        output = []
        TreeNode.traverse_bfs = lambda self: [output.append(node.value) for node in [self] + self.children]
        root.traverse_bfs()
        self.assertEqual(output, ["root", "a", "b"])

    def test_binary_tree_insertion_and_search(self):
        root = BinaryTreeNode(10)
        root.insert_bst(5)
        root.insert_bst(15)
        self.assertEqual(root.search(5).value, 5)
        self.assertEqual(root.search(15).value, 15)

    def test_binary_tree_search_not_found(self):
        root = BinaryTreeNode(10)
        root.insert_bst(5)
        self.assertIsNone(root.search(99))

    def test_binary_tree_inorder_traversal(self):
        root = BinaryTreeNode(10)
        root.insert_bst(5)
        root.insert_bst(15)
        result = []
        BinaryTreeNode.inorder = lambda self: result.extend([self.left.inorder() if self.left else None, self.value, self.right.inorder() if self.right else None])
        root.inorder()
        self.assertIn(5, result)
        self.assertIn(10, result)
        self.assertIn(15, result)

class TestGeometry(unittest.TestCase):

    def test_point_move(self):
        p = Point(1, 2)
        moved = p.move(3, -1)
        self.assertEqual((moved.x, moved.y), (4, 1))

    def test_point_scale(self):
        p = Point(2, 3)
        scaled = p.scale(2)
        self.assertEqual((scaled.x, scaled.y), (4, 6))

    def test_point_invert(self):
        p = Point(2, -3)
        inverted = p.invert()
        self.assertEqual((inverted.x, inverted.y), (-2, 3))

    def test_circle_move(self):
        c = Circle(Point(0, 0), 5)
        moved = c.move(2, 3)
        self.assertEqual((moved.center.x, moved.center.y), (2, 3))

    def test_circle_scale(self):
        c = Circle(Point(1, 1), 4)
        scaled = c.scale(0.5)
        self.assertTrue(isclose(scaled.radius, 2.0))

    def test_circle_invert(self):
        c = Circle(Point(1, -1), 3)
        inverted = c.invert()
        self.assertEqual((inverted.center.x, inverted.center.y), (-1, 1))

    def test_polygon_move(self):
        poly = Polygon([Point(0, 0), Point(1, 1)])
        moved = poly.move(2, 3)
        self.assertEqual([(p.x, p.y) for p in moved.points], [(2, 3), (3, 4)])

    def test_polygon_scale(self):
        poly = Polygon([Point(1, 2), Point(3, 4)])
        scaled = poly.scale(2)
        self.assertEqual([(p.x, p.y) for p in scaled.points], [(2, 4), (6, 8)])

    def test_polygon_invert(self):
        poly = Polygon([Point(1, -2), Point(-3, 4)])
        inverted = poly.invert()
        self.assertEqual([(p.x, p.y) for p in inverted.points], [(-1, 2), (3, -4)])

    def test_polygon_empty(self):
        poly = Polygon([])
        moved = poly.move(1, 1)
        self.assertEqual(len(moved.points), 0)

    def test_circle_zero_radius(self):
        c = Circle(Point(0, 0), 0)
        scaled = c.scale(10)
        self.assertEqual(scaled.radius, 0)

if __name__ == "__main__":
    unittest.main()
