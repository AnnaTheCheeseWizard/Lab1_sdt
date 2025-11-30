"""!
@file test_structures_geometry.py
@brief Unit tests for fundamental data structures (Tree Nodes) and 2D geometric primitives.

@details This module uses the standard `unittest` framework for comprehensive verification of core functionality,
correctness of calculations, traversal logic, and, most importantly, **immutability** of
transformation methods in the following classes: **TreeNode**, **BinaryTreeNode**, **Point**, **Circle**, and **Polygon**.
"""
import unittest
from math import isclose
from main import TreeNode, BinaryTreeNode, Point, Circle, Polygon

class TestTreeStructures(unittest.TestCase):
    """!
    @brief Test suite for data structures: **TreeNode** (N-ary tree) and **BinaryTreeNode** (BST).
    @details Verifies the correctness of node manipulation operations (addition, removal, search)
    and the accuracy of traversal algorithms for different tree types (DFS, BFS, Inorder, Preorder, Postorder).
    """

    # Tests for TreeNode (General N-ary Tree)
    
    def test_add_and_find_child(self):
        """!
        @brief Verifies the basic functionality of adding a child node and finding it by value.
        
        @example
        root = TreeNode("root"); child = TreeNode("child")
        root.add_child(child)
        assert root.find("child") == child
        assert root.find("missing") is None
        """
        root = TreeNode("root")
        child = TreeNode("child")
        root.add_child(child)
        self.assertEqual(root.find("child"), child)
        self.assertIsNone(root.find("non_existent"))

    def test_remove_child_by_value(self):
        """!
        @brief Verifies the successful removal of a child node by its value.
        
        @details Ensures the targeted node is removed from the children list, while other children remain intact.
        
        @example
        root.add_child(TreeNode("a")); root.add_child(TreeNode("b"))
        root.remove_child_by_value("a")
        assert root.find("a") is None
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
        @brief Verifies the correct sequence of Depth-First Search (**DFS**) traversal.
        
        @return A list corresponding to a pre-order traversal (Root, Child, Grandchild...).
        
        @example
        Structure: root -> a -> c; root -> b
        Result: ["root", "a", "c", "b"]
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
        @brief Verifies the correct sequence of Breadth-First Search (**BFS**) traversal.
        
        @return A list corresponding to a level-by-level traversal.
        
        @example
        Structure: root (Level 0); a, b (Level 1); c, d (Level 2)
        Result: ["root", "a", "b", "c", "d"]
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

    # Tests for BinaryTreeNode (Binary Search Tree)
    
    def test_binary_tree_insertion_and_search(self):
        """!
        @brief Verifies the correctness of element insertion into a **BST** and their successful retrieval.
        
        @details Insertion must maintain the BST property (lesser values left, greater values right).
        
        @example
        root.insert_bst(10, 5, 15, 3)
        assert root.search(5).value == 5
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
        @brief Verifies searching for values not present in the **BST**.
        
        @return `None` for non-existent elements.
        """
        root = BinaryTreeNode(10)
        root.insert_bst(5)

        self.assertIsNone(root.search(99))
        self.assertIsNone(root.search(1))

    def test_binary_tree_inorder_traversal(self):
        """!
        @brief Verifies the **Inorder** (LNR) traversal.
        
        @return A list of elements sorted in ascending order, consistent with BST properties.
        """
        root = BinaryTreeNode(10)
        root.insert_bst(5)
        root.insert_bst(15)
        root.insert_bst(3)
        root.insert_bst(7)
        
        self.assertEqual(root.inorder(), [3, 5, 7, 10, 15])

    def test_binary_tree_preorder_traversal(self):
        """!
        @brief Verifies the **Preorder** (NLR) traversal.
        """
        root = BinaryTreeNode(10)
        root.insert_bst(5)
        root.insert_bst(15)
        root.insert_bst(3)
        root.insert_bst(7)
        
        self.assertEqual(root.preorder(), [10, 5, 3, 7, 15])

    def test_binary_tree_postorder_traversal(self):
        """!
        @brief Verifies the **Postorder** (LRN) traversal.
        """
        root = BinaryTreeNode(10)
        root.insert_bst(5)
        root.insert_bst(15)
        root.insert_bst(3)
        root.insert_bst(7)
        self.assertEqual(root.postorder(), [3, 7, 5, 15, 10])

class TestGeometry(unittest.TestCase):
    """!
    @brief Test suite for 2D geometric primitives: **Point**, **LineSegment**, **Circle**, and **Polygon**.
    @details The primary focus is on the correctness of geometric transformations (**move**, **scale**, **invert**)
    and the **immutability** of the original objects after transformation.
    """

    # Tests for Point
    
    def test_point_move_immutability(self):
        """!
        @brief Verifies that the move operation returns a new **Point** object and does not modify the original.
        
        @param dx X-axis offset (3)
        @param dy Y-axis offset (-1)
        @return New object (4, 1), original (1, 2)
        """
        p = Point(1, 2)
        moved = p.move(3, -1)
        self.assertEqual((moved.x, moved.y), (4, 1)) 
        self.assertEqual((p.x, p.y), (1, 2)) 

    def test_point_scale_immutability(self):
        """!
        @brief Verifies that the scale operation returns a new **Point** object and does not modify the original.
        
        @param factor Scaling factor (2)
        @return New object (4, 6), original (2, 3)
        """
        p = Point(2, 3)
        scaled = p.scale(2)
        self.assertEqual((scaled.x, scaled.y), (4, 6)) 
        self.assertEqual((p.x, p.y), (2, 3)) 

    def test_point_invert_immutability(self):
        """!
        @brief Verifies that the invert operation returns a new **Point** object with negated coordinates, and does not modify the original.
        
        @return New object (-2, 3), original (2, -3)
        """
        p = Point(2, -3)
        inverted = p.invert()
        self.assertEqual((inverted.x, inverted.y), (-2, 3)) 
        self.assertEqual((p.x, p.y), (2, -3)) 

    def test_point_scale_zero(self):
        """!
        @brief Tests scaling a point by a zero factor.
        
        @return The point should move to the origin (0, 0).
        """
        p = Point(5, -3)
        scaled = p.scale(0)
        self.assertEqual((scaled.x, scaled.y), (0, 0)) 

    # Tests for LineSegment
    
    def test_line_segment_creation(self):
        """!
        @brief Verifies the successful creation of a **LineSegment**
        and the correct initialization of its endpoints.
        
        @param p1 First point (1, 1)
        @param p2 Second point (5, 5)
        """
        p1 = Point(1, 1)
        p2 = Point(5, 5)
        ls = LineSegment(p1, p2)
        self.assertEqual(ls.p1.x, 1)
        self.assertEqual(ls.p2.y, 5)
        self.assertIsInstance(ls.p1, Point) 

    # Tests for Circle
    
    def test_circle_move_immutability(self):
        """!
        @brief Verifies that the move operation translates the center but does not modify the original circle.
        
        @param dx X offset (2)
        @param dy Y offset (3)
        @return A new circle with center (2, 3) and radius 5.
        """
        c = Circle(Point(0, 0), 5)
        moved = c.move(2, 3)
        self.assertEqual((moved.center.x, moved.center.y), (2, 3)) 
        self.assertEqual((c.center.x, c.center.y), (0, 0)) 
        self.assertEqual(c.radius, 5)

    def test_circle_scale_immutability(self):
        """!
        @brief Verifies that the scale operation is applied to the center and radius, and the original object remains unchanged.
        
        @param factor Scaling factor (0.5)
        @return A new circle with center (0.5, 0.5) and radius 2.0.
        """
        c = Circle(Point(1, 1), 4)
        scaled = c.scale(0.5)
        self.assertTrue(isclose(scaled.radius, 2.0))
        self.assertEqual((scaled.center.x, scaled.center.y), (0.5, 0.5)) 
        self.assertEqual(c.radius, 4)
        self.assertEqual((c.center.x, c.center.y), (1, 1))

    def test_circle_invert_immutability(self):
        """!
        @brief Verifies that the invert operation negates the center coordinates, and the original circle remains unchanged.
        
        @return A new circle with center (-1, 1) and radius 3.
        """
        c = Circle(Point(1, -1), 3)
        inverted = c.invert()
        self.assertEqual((inverted.center.x, inverted.center.y), (-1, 1)) 
        self.assertEqual((c.center.x, c.center.y), (1, -1))
        self.assertEqual(c.radius, 3)

    def test_circle_zero_radius(self):
        """!
        @brief Tests that scaling a circle with a zero radius does not lead to errors.
        """
        c = Circle(Point(0, 0), 0)
        scaled = c.scale(10)
        self.assertEqual(scaled.radius, 0)
        self.assertEqual((scaled.center.x, scaled.center.y), (0, 0))

    def test_circle_none_center(self):
        """!
        @brief Checks if the expected **AttributeError** is raised when attempting a transformation if the center is **None**.
        
        @throws AttributeError
        """
        # Assuming the Circle class might initialize without proper validation, leading to an AttributeError upon calling a method that accesses center attributes.
        with self.assertRaises(AttributeError):
            Circle(None, 5).move(1, 1)

    # Tests for Polygon
    
    def test_polygon_move_immutability(self):
        """!
        @brief Verifies that the move operation translates all vertices, and the original polygon remains unchanged.
        
        @param dx X offset (2)
        @param dy Y offset (3)
        @return A new polygon with vertices [(2, 3), (3, 4)].
        """
        poly = Polygon([Point(0, 0), Point(1, 1)])
        moved = poly.move(2, 3)
        self.assertEqual([(p.x, p.y) for p in moved.points], [(2, 3), (3, 4)]) 
        self.assertEqual([(p.x, p.y) for p in poly.points], [(0, 0), (1, 1)]) 

    def test_polygon_scale_immutability(self):
        """!
        @brief Verifies that the scale operation is applied to all vertices, and the original polygon remains unchanged.
        """
        poly = Polygon([Point(1, 2), Point(3, 4)])
        scaled = poly.scale(2)
        self.assertEqual([(p.x, p.y) for p in scaled.points], [(2, 4), (6, 8)]) 
        self.assertEqual([(p.x, p.y) for p in poly.points], [(1, 2), (3, 4)]) 

    def test_polygon_invert_immutability(self):
        """!
        @brief Verifies that the invert operation is applied to all vertices, and the original polygon remains unchanged.
        """
        poly = Polygon([Point(1, -2), Point(-3, 4)])
        inverted = poly.invert()
        self.assertEqual([(p.x, p.y) for p in inverted.points], [(-1, 2), (3, -4)]) 
        self.assertEqual([(p.x, p.y) for p in poly.points], [(1, -2), (-3, 4)])

    def test_polygon_empty(self):
        """!
        @brief Verifies that the move operation correctly handles an empty polygon.
        
        @return An empty list of points.
        """
        poly = Polygon([])
        moved = poly.move(1, 1)
        self.assertEqual(len(moved.points), 0)

    def test_polygon_negative_scale(self):
        """!
        @brief Tests scaling a polygon by a negative factor (reflection).
        """
        poly = Polygon([Point(1, 2)])
        scaled = poly.scale(-1)
        self.assertEqual([(p.x, p.y) for p in scaled.points], [(-1, -2)])
    
    def test_polygon_invert_empty(self):
        """!
        @brief Verifies that the invert operation correctly handles an empty polygon.
        
        @return An empty list of points.
        """
        poly = Polygon([])
        inverted = poly.invert()
        self.assertEqual(len(inverted.points), 0)

if __name__ == "__main__":
    unittest.main()