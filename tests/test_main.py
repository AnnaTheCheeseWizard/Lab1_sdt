import unittest
from math import isclose
from main import TreeNode, BinaryTreeNode, Point, Circle, Polygon, LineSegment

class TestTreeStructures(unittest.TestCase):
    """!
    @brief Unit tests for TreeNode and BinaryTreeNode structures.
    
    @details Contains test cases for general tree operations (add, remove, traverse)
    and binary search tree operations (insert, search, traversals).
    """

    # ----------- TreeNode TESTS -----------

    def test_add_and_find_child(self):
        """!
        @brief Tests that a child can be added and later found.

        @test Verifies:
            - find() returns the correct node instance.
            - Searching for a non-existent value returns None.
        """
        root = TreeNode("root")
        child = TreeNode("child")
        root.add_child(child)

        self.assertEqual(root.find("child"), child)
        self.assertIsNone(root.find("non_existent"))

    def test_remove_child_by_value(self):
        """!
        @brief Tests removing a child node by its value.

        @test Ensures:
            - Only the specified child is removed.
            - Other children remain intact.
            - The children list length is updated correctly.
        """
        root = TreeNode("root")
        child1 = TreeNode("a")
        child2 = TreeNode("b")

        root.add_child(child1)
        root.add_child(child2)
        root.remove_child_by_value("a")

        self.assertIsNone(root.find("a"))
        self.assertIsNotNone(root.find("b"))
        self.assertEqual(len(root.children), 1)

    def test_dfs_traversal_order(self):
        """!
        @brief Tests that DFS traversal returns nodes in correct depth-first order.
        
        @test Constructs a small tree and verifies the list of values matches the expected DFS sequence.
        """
        root = TreeNode("root")
        child1 = TreeNode("a")
        child2 = TreeNode("b")
        subchild = TreeNode("c")

        root.add_child(child1)
        root.add_child(child2)
        child1.add_child(subchild)

        expected_order = ["root", "a", "c", "b"]
        self.assertEqual(root.traverse_dfs(), expected_order)

    def test_bfs_traversal_order(self):
        """!
        @brief Tests that BFS traversal returns nodes in correct breadth-first order.
        
        @test Constructs a tree with multiple levels and verifies the list of values matches the expected BFS sequence.
        """
        root = TreeNode("root")
        child1 = TreeNode("a")
        child2 = TreeNode("b")
        subchild1 = TreeNode("c")
        subchild2 = TreeNode("d")

        root.add_child(child1)
        root.add_child(child2)
        child1.add_child(subchild1)
        child2.add_child(subchild2)

        expected_order = ["root", "a", "b", "c", "d"]
        self.assertEqual(root.traverse_bfs(), expected_order)

    # ----------- BinaryTreeNode TESTS -----------

    def test_binary_tree_insertion_and_search(self):
        """!
        @brief Tests insertion into a BST and searching for inserted elements.
        
        @test Verifies that values inserted into the BST can be retrieved successfully.
        """
        root = BinaryTreeNode(10)
        root.insert_bst(5)
        root.insert_bst(15)
        root.insert_bst(3)

        self.assertEqual(root.search(5).value, 5)
        self.assertEqual(root.search(15).value, 15)
        self.assertEqual(root.search(3).value, 3)

    def test_binary_tree_search_not_found(self):
        """!
        @brief Tests that searching for non-existent elements returns None.
        
        @test Verifies that search() returns None for values not present in the tree.
        """
        root = BinaryTreeNode(10)
        root.insert_bst(5)

        self.assertIsNone(root.search(99))
        self.assertIsNone(root.search(1))

    def test_binary_tree_inorder_traversal(self):
        """!
        @brief Tests inorder traversal returns sorted list of values.
        
        @test Verifies that inorder traversal results in [3, 5, 7, 10, 15].
        """
        root = BinaryTreeNode(10)
        root.insert_bst(5)
        root.insert_bst(15)
        root.insert_bst(3)
        root.insert_bst(7)

        self.assertEqual(root.inorder(), [3, 5, 7, 10, 15])

    def test_binary_tree_preorder_traversal(self):
        """!
        @brief Tests preorder traversal correctness.
        
        @test Verifies that preorder traversal results in [10, 5, 3, 7, 15].
        """
        root = BinaryTreeNode(10)
        root.insert_bst(5)
        root.insert_bst(15)
        root.insert_bst(3)
        root.insert_bst(7)

        self.assertEqual(root.preorder(), [10, 5, 3, 7, 15])

    def test_binary_tree_postorder_traversal(self):
        """!
        @brief Tests postorder traversal correctness.
        
        @test Verifies that postorder traversal results in [3, 7, 5, 15, 10].
        """
        root = BinaryTreeNode(10)
        root.insert_bst(5)
        root.insert_bst(15)
        root.insert_bst(3)
        root.insert_bst(7)

        self.assertEqual(root.postorder(), [3, 7, 5, 15, 10])


class TestGeometry(unittest.TestCase):
    """!
    @brief Unit tests for Point, LineSegment, Circle, and Polygon.
    
    @details Focuses on verifying geometric calculations and immutability of the operations.
    """

    # ----------- Point TESTS -----------

    def test_point_move_immutability(self):
        """!
        @brief Tests that move() returns a new Point without modifying the original.
        
        @test Verifies:
            - The new point has updated coordinates.
            - The original point remains at (1, 2).
        """
        p = Point(1, 2)
        moved = p.move(3, -1)

        self.assertEqual((moved.x, moved.y), (4, 1))
        self.assertEqual((p.x, p.y), (1, 2))

    def test_point_scale_immutability(self):
        """!
        @brief Tests that scale() returns a new Point without modifying the original.
        
        @test Verifies:
            - The new point has scaled coordinates.
            - The original point remains unchanged.
        """
        p = Point(2, 3)
        scaled = p.scale(2)

        self.assertEqual((scaled.x, scaled.y), (4, 6))
        self.assertEqual((p.x, p.y), (2, 3))

    def test_point_invert_immutability(self):
        """!
        @brief Tests that invert() returns a new Point without modifying the original.
        
        @test Verifies coordinate inversion logic and object immutability.
        """
        p = Point(2, -3)
        inverted = p.invert()

        self.assertEqual((inverted.x, inverted.y), (-2, 3))
        self.assertEqual((p.x, p.y), (2, -3))

    def test_point_scale_zero(self):
        """!
        @brief Tests that scaling by zero returns (0, 0).
        
        @test Verifies edge case where scale factor is 0.
        """
        p = Point(5, -3)
        scaled = p.scale(0)

        self.assertEqual((scaled.x, scaled.y), (0, 0))

    # ----------- LineSegment TESTS -----------

    def test_line_segment_creation(self):
        """!
        @brief Tests LineSegment initialization.
        
        @test Verifies that the LineSegment correctly stores start and end Points.
        """
        p1 = Point(1, 1)
        p2 = Point(5, 5)
        ls = LineSegment(p1, p2)

        self.assertEqual(ls.p1.x, 1)
        self.assertEqual(ls.p2.y, 5)
        self.assertIsInstance(ls.p1, Point)

    # ----------- Circle TESTS -----------

    def test_circle_move_immutability(self):
        """!
        @brief Tests move() returns new Circle without modifying the original.
        
        @test Verifies that moving a circle updates the center but keeps the original object intact.
        """
        c = Circle(Point(0, 0), 5)
        moved = c.move(2, 3)

        self.assertEqual((moved.center.x, moved.center.y), (2, 3))
        self.assertEqual((c.center.x, c.center.y), (0, 0))
        self.assertEqual(c.radius, 5)

    def test_circle_scale_immutability(self):
        """!
        @brief Tests scale() returns new Circle and scales radius + center.
        
        @test Verifies that scaling affects both the radius and the center's distance from origin.
        """
        c = Circle(Point(1, 1), 4)
        scaled = c.scale(0.5)

        self.assertTrue(isclose(scaled.radius, 2.0))
        self.assertEqual((scaled.center.x, scaled.center.y), (0.5, 0.5))
        self.assertEqual(c.radius, 4)
        self.assertEqual((c.center.x, c.center.y), (1, 1))

    def test_circle_invert_immutability(self):
        """!
        @brief Tests invert() returns new Circle without modifying the original.
        
        @test Verifies that inversion reflects the center across the origin but keeps the radius.
        """
        c = Circle(Point(1, -1), 3)
        inverted = c.invert()

        self.assertEqual((inverted.center.x, inverted.center.y), (-1, 1))
        self.assertEqual((c.center.x, c.center.y), (1, -1))
        self.assertEqual(c.radius, 3)

    def test_circle_zero_radius(self):
        """!
        @brief Tests that scaling a zero-radius circle keeps radius zero.
        
        @test Verifies edge case for zero radius.
        """
        c = Circle(Point(0, 0), 0)
        scaled = c.scale(10)

        self.assertEqual(scaled.radius, 0)
        self.assertEqual((scaled.center.x, scaled.center.y), (0, 0))

    def test_circle_none_center(self):
        """!
        @brief Tests that calling move() on a circle with None center raises an error.
        
        @test Verifies error handling when Circle is initialized improperly for operations.
        """
        with self.assertRaises(AttributeError):
            Circle(None, 5).move(1, 1)

    # ----------- Polygon TESTS -----------

    def test_polygon_move_immutability(self):
        """!
        @brief Tests that move() returns a new Polygon without modifying the original.
        
        @test Verifies that all points in the polygon are shifted correctly.
        """
        poly = Polygon([Point(0, 0), Point(1, 1)])
        moved = poly.move(2, 3)

        self.assertEqual([(p.x, p.y) for p in moved.points],
                         [(2, 3), (3, 4)])
        self.assertEqual([(p.x, p.y) for p in poly.points],
                         [(0, 0), (1, 1)])

    def test_polygon_scale_immutability(self):
        """!
        @brief Tests that scale() creates a new Polygon with scaled points.
        
        @test Verifies that all points are scaled relative to the origin.
        """
        poly = Polygon([Point(1, 2), Point(3, 4)])
        scaled = poly.scale(2)

        self.assertEqual([(p.x, p.y) for p in scaled.points],
                         [(2, 4), (6, 8)])

    def test_polygon_invert_immutability(self):
        """!
        @brief Tests that invert() returns new Polygon with inverted points.
        
        @test Verifies that all points are inverted across the origin.
        """
        poly = Polygon([Point(1, -2), Point(-3, 4)])
        inverted = poly.invert()

        self.assertEqual([(p.x, p.y) for p in inverted.points],
                         [(-1, 2), (3, -4)])

    def test_polygon_empty(self):
        """!
        @brief Tests that operations on an empty polygon return empty results.
        
        @test Verifies behavior when the Polygon has no points.
        """
        poly = Polygon([])
        moved = poly.move(1, 1)

        self.assertEqual(len(moved.points), 0)

    def test_polygon_negative_scale(self):
        """!
        @brief Tests that negative scaling inverts coordinates as expected.
        
        @test Verifies that a negative scale factor both scales and inverts the polygon.
        """
        poly = Polygon([Point(1, 2)])
        scaled = poly.scale(-1)

        self.assertEqual([(p.x, p.y) for p in scaled.points],
                         [(-1, -2)])

    def test_polygon_invert_empty(self):
        """!
        @brief Tests invert() on an empty polygon.
        
        @test Verifies inversion logic on an empty list of points.
        """
        poly = Polygon([])
        inverted = poly.invert()

        self.assertEqual(len(inverted.points), 0)


if __name__ == "__main__":
    unittest.main()