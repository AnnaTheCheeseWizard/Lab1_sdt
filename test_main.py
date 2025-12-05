"""!
@file test_main.py
@brief Unit tests for fundamental data structures (Tree Nodes) and 2D geometric primitives.

@details This module uses the standard `unittest` framework for comprehensive verification of:
- correctness of calculations,
- traversal logic,
- and most importantly **immutability** of transformation methods.

Tested classes:
- TreeNode
- BinaryTreeNode
- Point
- Circle
- Polygon
"""

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import unittest
from math import isclose
import json
from main import (
    TreeNode, BinaryTreeNode, Point, Circle, Polygon, LineSegment,
    save_to_file, load_from_file, GeometricOperations
)


class TestTreeStructures(unittest.TestCase):
    """!
    @brief Test suite for tree data structures.

    @details Verifies correctness of:
    - node insertion and deletion,
    - value searching,
    - DFS and BFS traversal (TreeNode),
    - Inorder, Preorder and Postorder traversals (BinaryTreeNode).
    """

    # Tests for TreeNode (N-ary tree)

    def test_add_and_find_child(self):
        """!
        @test
        @brief Tests adding a child node and searching it by value.

        @details Ensures that:
        - the child is successfully added,
        - the search method correctly finds existing elements,
        - and returns None for missing values.
        """
        root = TreeNode("root")
        child = TreeNode("child")

        root.add_child(child)
        self.assertEqual(root.find("child"), child)
        self.assertIsNone(root.find("non_existent"))

    def test_remove_child_by_value(self):
        """!
        @test
        @brief Tests removal of a child node by its value.

        @details Ensures that:
        - the selected child is removed,
        - other children remain intact,
        - the tree structure remains consistent.
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
        @test
        @brief Verifies correct Depth-First Search (DFS) traversal order.

        @details Confirms pre-order traversal correctness:
        Root → Left subtree → Right subtree.
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
        @test
        @brief Verifies correct Breadth-First Search (BFS) traversal order.

        @details Confirms level-by-level traversal correctness.
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

    # Tests for BinaryTreeNode (BST)

    def test_binary_tree_insertion_and_search(self):
        """!
        @test
        @brief Tests insertion into a Binary Search Tree and searching for values.

        @details Confirms that BST properties are preserved after insertion.
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
        @test
        @brief Tests searching for a value not present in the BST.

        @details Ensures that missing elements return None.
        """
        root = BinaryTreeNode(10)
        root.insert_bst(5)

        self.assertIsNone(root.search(99))
        self.assertIsNone(root.search(1))

    def test_binary_tree_inorder_traversal(self):
        """!
        @test
        @brief Tests correct Inorder traversal (Left–Node–Right).

        @details Confirms that nodes are returned in sorted ascending order.
        """
        root = BinaryTreeNode(10)
        root.insert_bst(5)
        root.insert_bst(15)
        root.insert_bst(3)
        root.insert_bst(7)
        
        self.assertEqual(root.inorder(), [3, 5, 7, 10, 15])

    def test_binary_tree_preorder_traversal(self):
        """!
        @test
        @brief Tests correct Preorder traversal (Node–Left–Right).
        """
        root = BinaryTreeNode(10)
        root.insert_bst(5)
        root.insert_bst(15)
        root.insert_bst(3)
        root.insert_bst(7)
        
        self.assertEqual(root.preorder(), [10, 5, 3, 7, 15])

    def test_binary_tree_postorder_traversal(self):
        """!
        @test
        @brief Tests correct Postorder traversal (Left–Right–Node).
        """
        root = BinaryTreeNode(10)
        root.insert_bst(5)
        root.insert_bst(15)
        root.insert_bst(3)
        root.insert_bst(7)
        self.assertEqual(root.postorder(), [3, 7, 5, 15, 10])

class TestGeometry(unittest.TestCase):
    """!
    @brief Test suite for 2D geometric primitives.

    @details Verifies:
    - correctness of geometric transformations,
    - immutability of original objects after transformations.
    """

    # Tests for Point
    
    def test_point_move_immutability(self):
        """!
        @test
        @brief Tests immutability of the move operation for Point.
        """
        p = Point(1, 2)
        moved = p.move(3, -1)
        self.assertEqual((moved.x, moved.y), (4, 1)) 
        self.assertEqual((p.x, p.y), (1, 2)) 

    def test_point_scale_immutability(self):
        """!
        @test
        @brief Tests immutability of the scale operation for Point.
        """
        p = Point(2, 3)
        scaled = p.scale(2)
        self.assertEqual((scaled.x, scaled.y), (4, 6)) 
        self.assertEqual((p.x, p.y), (2, 3)) 

    def test_point_invert_immutability(self):
        """!
        @test
        @brief Tests immutability of the invert operation for Point.
        """
        p = Point(2, -3)
        inverted = p.invert()
        self.assertEqual((inverted.x, inverted.y), (-2, 3)) 
        self.assertEqual((p.x, p.y), (2, -3)) 

    def test_point_scale_zero(self):
        """!
        @test
        @brief Tests scaling a point with zero factor.
        """
        p = Point(5, -3)
        scaled = p.scale(0)
        self.assertEqual((scaled.x, scaled.y), (0, 0)) 

    # Tests for LineSegment
    
    def test_line_segment_creation(self):
        """!
        @test
        @brief Tests correct creation of a LineSegment.
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
        @test
        @brief Tests immutability of the move operation for Circle.
        """
        c = Circle(Point(0, 0), 5)
        moved = c.move(2, 3)
        self.assertEqual((moved.center.x, moved.center.y), (2, 3)) 
        self.assertEqual((c.center.x, c.center.y), (0, 0)) 
        self.assertEqual(c.radius, 5)

    def test_circle_scale_immutability(self):
        """!
        @test
        @brief Tests immutability of the scale operation for Circle.
        """
        c = Circle(Point(1, 1), 4)
        scaled = c.scale(0.5)
        self.assertTrue(isclose(scaled.radius, 2.0))
        self.assertEqual((scaled.center.x, scaled.center.y), (0.5, 0.5)) 
        self.assertEqual(c.radius, 4)
        self.assertEqual((c.center.x, c.center.y), (1, 1))

    def test_circle_invert_immutability(self):
        """!
        @test
        @brief Tests immutability of the invert operation for Circle.
        """
        c = Circle(Point(1, -1), 3)
        inverted = c.invert()
        self.assertEqual((inverted.center.x, inverted.center.y), (-1, 1)) 
        self.assertEqual((c.center.x, c.center.y), (1, -1))
        self.assertEqual(c.radius, 3)

    def test_circle_zero_radius(self):
        """!
        @test
        @brief Tests scaling a circle with zero radius.
        """
        c = Circle(Point(0, 0), 0)
        scaled = c.scale(10)
        self.assertEqual(scaled.radius, 0)
        self.assertEqual((scaled.center.x, scaled.center.y), (0, 0))

    def test_circle_none_center(self):
        """!
        @test
        @brief Verifies that AttributeError is raised when the circle center is None.
        """
        with self.assertRaises(AttributeError):
            Circle(None, 5).move(1, 1)

    # Tests for Polygon
    
    def test_polygon_move_immutability(self):
        """!
        @test
        @brief Tests immutability of the move operation for Polygon.
        """
        poly = Polygon([Point(0, 0), Point(1, 1)])
        moved = poly.move(2, 3)
        self.assertEqual([(p.x, p.y) for p in moved.points], [(2, 3), (3, 4)]) 
        self.assertEqual([(p.x, p.y) for p in poly.points], [(0, 0), (1, 1)]) 

    def test_polygon_scale_immutability(self):
        """!
        @test
        @brief Tests immutability of the scale operation for Polygon.
        """
        poly = Polygon([Point(1, 2), Point(3, 4)])
        scaled = poly.scale(2)
        self.assertEqual([(p.x, p.y) for p in scaled.points], [(2, 4), (6, 8)]) 
        self.assertEqual([(p.x, p.y) for p in poly.points], [(1, 2), (3, 4)]) 

    def test_polygon_invert_immutability(self):
        """!
        @test
        @brief Tests immutability of the invert operation for Polygon.
        """
        poly = Polygon([Point(1, -2), Point(-3, 4)])
        inverted = poly.invert()
        self.assertEqual([(p.x, p.y) for p in inverted.points], [(-1, 2), (3, -4)]) 
        self.assertEqual([(p.x, p.y) for p in poly.points], [(1, -2), (-3, 4)])

    def test_polygon_empty(self):
        """!
        @test
        @brief Tests transformations on an empty Polygon.
        """
        poly = Polygon([])
        moved = poly.move(1, 1)
        self.assertEqual(len(moved.points), 0)

    def test_polygon_negative_scale(self):
        """!
        @test
        @brief Tests scaling a polygon with a negative factor.
        """
        poly = Polygon([Point(1, 2)])
        scaled = poly.scale(-1)
        self.assertEqual([(p.x, p.y) for p in scaled.points], [(-1, -2)])
    
    def test_polygon_invert_empty(self):
        """!
        @test
        @brief Tests invert operation on an empty Polygon.
        """
        poly = Polygon([])
        inverted = poly.invert()
        self.assertEqual(len(inverted.points), 0)


class TestGeometricOperations(unittest.TestCase):
    """!
    @brief Test suite for GeometricOperations class.
    
    @details Verifies correctness of advanced geometric operations including:
    - circle intersection and union calculations,
    - polygon bounding circles,
    - polygon inscribed circles.
    """
    
    def test_circle_intersection_no_overlap(self):
        """!
        @test
        @brief Tests circle intersection area when circles don't overlap.
        """
        c1 = Circle(Point(0, 0), 5)
        c2 = Circle(Point(20, 0), 5)
        area = GeometricOperations.circle_intersection_area(c1, c2)
        self.assertTrue(isclose(area, 0.0, abs_tol=0.01))
    
    def test_circle_intersection_partial_overlap(self):
        """!
        @test
        @brief Tests circle intersection area with partial overlap.
        """
        c1 = Circle(Point(0, 0), 5)
        c2 = Circle(Point(5, 0), 5)
        area = GeometricOperations.circle_intersection_area(c1, c2)
        self.assertGreater(area, 0)
        self.assertLess(area, c1.area())
    
    def test_circle_intersection_one_inside_another(self):
        """!
        @test
        @brief Tests circle intersection when one circle is completely inside another.
        """
        c1 = Circle(Point(0, 0), 10)
        c2 = Circle(Point(0, 0), 5)
        area = GeometricOperations.circle_intersection_area(c1, c2)
        self.assertTrue(isclose(area, c2.area(), rel_tol=0.01))
    
    def test_circle_intersection_identical_circles(self):
        """!
        @test
        @brief Tests circle intersection when circles are identical.
        """
        c1 = Circle(Point(5, 5), 7)
        c2 = Circle(Point(5, 5), 7)
        area = GeometricOperations.circle_intersection_area(c1, c2)
        self.assertTrue(isclose(area, c1.area(), rel_tol=0.01))
    
    def test_circle_union_no_overlap(self):
        """!
        @test
        @brief Tests circle union area when circles don't overlap.
        """
        c1 = Circle(Point(0, 0), 5)
        c2 = Circle(Point(20, 0), 5)
        area = GeometricOperations.circle_union_area(c1, c2)
        expected = c1.area() + c2.area()
        self.assertTrue(isclose(area, expected, rel_tol=0.01))
    
    def test_circle_union_partial_overlap(self):
        """!
        @test
        @brief Tests circle union area with partial overlap.
        """
        c1 = Circle(Point(0, 0), 5)
        c2 = Circle(Point(5, 0), 5)
        area = GeometricOperations.circle_union_area(c1, c2)
        self.assertLess(area, c1.area() + c2.area())
        self.assertGreater(area, max(c1.area(), c2.area()))
    
    def test_circle_union_one_inside_another(self):
        """!
        @test
        @brief Tests circle union when one circle is completely inside another.
        """
        c1 = Circle(Point(0, 0), 10)
        c2 = Circle(Point(0, 0), 5)
        area = GeometricOperations.circle_union_area(c1, c2)
        self.assertTrue(isclose(area, c1.area(), rel_tol=0.01))
    
    def test_circle_union_identical_circles(self):
        """!
        @test
        @brief Tests circle union when circles are identical.
        """
        c1 = Circle(Point(3, 4), 6)
        c2 = Circle(Point(3, 4), 6)
        area = GeometricOperations.circle_union_area(c1, c2)
        self.assertTrue(isclose(area, c1.area(), rel_tol=0.01))
    
    def test_polygon_bounding_circle_triangle(self):
        """!
        @test
        @brief Tests bounding circle calculation for a triangle.
        """
        triangle = Polygon([Point(0, 0), Point(10, 0), Point(5, 10)])
        bounding = GeometricOperations.polygon_bounding_circle(triangle)
        
        self.assertIsInstance(bounding, Circle)
        for point in triangle.points:
            distance = bounding.center.distance_to(point)
            self.assertLessEqual(distance, bounding.radius + 0.01)
    
    def test_polygon_bounding_circle_square(self):
        """!
        @test
        @brief Tests bounding circle calculation for a square.
        """
        square = Polygon([Point(0, 0), Point(10, 0), Point(10, 10), Point(0, 10)])
        bounding = GeometricOperations.polygon_bounding_circle(square)
        
        self.assertIsInstance(bounding, Circle)
        self.assertTrue(isclose(bounding.center.x, 5.0, abs_tol=0.1))
        self.assertTrue(isclose(bounding.center.y, 5.0, abs_tol=0.1))
        for point in square.points:
            distance = bounding.center.distance_to(point)
            self.assertLessEqual(distance, bounding.radius + 0.01)
    
    def test_polygon_bounding_circle_regular_hexagon(self):
        """!
        @test
        @brief Tests bounding circle for a regular hexagon.
        """
        hexagon = Polygon.generate_regular_polygon(6, radius=10, center=Point(0, 0))
        bounding = GeometricOperations.polygon_bounding_circle(hexagon)
        
        self.assertIsInstance(bounding, Circle)
        for point in hexagon.points:
            distance = bounding.center.distance_to(point)
            self.assertLessEqual(distance, bounding.radius + 0.1)
    
    def test_polygon_inscribed_circle_square(self):
        """!
        @test
        @brief Tests inscribed circle approximation for a square.
        """
        square = Polygon([Point(0, 0), Point(10, 0), Point(10, 10), Point(0, 10)])
        inscribed = GeometricOperations.polygon_inscribed_circle_approximation(square)
        
        self.assertIsInstance(inscribed, Circle)
        self.assertTrue(isclose(inscribed.radius, 5.0, abs_tol=0.5))

        self.assertTrue(isclose(inscribed.center.x, 5.0, abs_tol=0.5))
        self.assertTrue(isclose(inscribed.center.y, 5.0, abs_tol=0.5))
    
    def test_polygon_inscribed_circle_triangle(self):
        """!
        @test
        @brief Tests inscribed circle approximation for a triangle.
        """
        triangle = Polygon([Point(0, 0), Point(10, 0), Point(5, 8)])
        inscribed = GeometricOperations.polygon_inscribed_circle_approximation(triangle)
        
        self.assertIsInstance(inscribed, Circle)
        self.assertGreater(inscribed.radius, 0)
        self.assertLess(inscribed.radius, 10)
    
    def test_polygon_inscribed_circle_empty(self):
        """!
        @test
        @brief Tests inscribed circle for empty polygon (edge case).
        """
        empty_poly = Polygon([])
        inscribed = GeometricOperations.polygon_inscribed_circle_approximation(empty_poly)
        
        self.assertIsInstance(inscribed, Circle)
        self.assertGreater(inscribed.radius, 0)
    
    def test_circle_intersection_touching_circles(self):
        """!
        @test
        @brief Tests circle intersection when circles are exactly touching.
        """
        c1 = Circle(Point(0, 0), 5)
        c2 = Circle(Point(10, 0), 5) 
        area = GeometricOperations.circle_intersection_area(c1, c2)
        self.assertTrue(isclose(area, 0.0, abs_tol=0.01))
    
    def test_circle_union_touching_circles(self):
        """!
        @test
        @brief Tests circle union when circles are exactly touching.
        """
        c1 = Circle(Point(0, 0), 5)
        c2 = Circle(Point(10, 0), 5)
        area = GeometricOperations.circle_union_area(c1, c2)
        expected = c1.area() + c2.area()
        self.assertTrue(isclose(area, expected, rel_tol=0.01))
    
    def test_circle_intersection_with_different_radii(self):
        """!
        @test
        @brief Tests circle intersection with different radii.
        """
        c1 = Circle(Point(0, 0), 10)
        c2 = Circle(Point(8, 0), 5)
        area = GeometricOperations.circle_intersection_area(c1, c2)
        self.assertGreater(area, 0)
        self.assertLess(area, c2.area())
    
    def test_polygon_bounding_circle_single_point(self):
        """!
        @test
        @brief Tests bounding circle for a polygon with single point.
        """
        single_point = Polygon([Point(5, 7)])
        bounding = GeometricOperations.polygon_bounding_circle(single_point)
        
        self.assertIsInstance(bounding, Circle)
        self.assertEqual(bounding.radius, 0.0)
        self.assertEqual(bounding.center.x, 5)
        self.assertEqual(bounding.center.y, 7)


class TestRandomGeneration(unittest.TestCase):
    """!
    @brief Test suite for random data generation methods.
    
    @details Verifies that random generation methods produce valid objects
    with appropriate properties and within specified ranges.
    """
    
    def test_treenode_random_generation(self):
        """!
        @test
        @brief Tests random TreeNode generation.
        """
        tree = TreeNode.generate_random(max_depth=3, max_children=3, value_range=(1, 100))
        self.assertIsNotNone(tree)
        self.assertIsInstance(tree, TreeNode)
        self.assertGreaterEqual(tree.value, 1)
        self.assertLessEqual(tree.value, 100)
    
    def test_binarytreenode_random_generation(self):
        """!
        @test
        @brief Tests random BinaryTreeNode generation and BST property.
        """
        bst = BinaryTreeNode.generate_random(size=10, value_range=(1, 100))
        self.assertIsNotNone(bst)
        self.assertIsInstance(bst, BinaryTreeNode)
        inorder = bst.inorder()
        self.assertLessEqual(len(inorder), 10)
        self.assertEqual(inorder, sorted(inorder))
    
    def test_point_random_generation(self):
        """!
        @test
        @brief Tests random Point generation within specified range.
        """
        point = Point.generate_random(x_range=(-50, 50), y_range=(-50, 50))
        self.assertIsInstance(point, Point)
        self.assertGreaterEqual(point.x, -50)
        self.assertLessEqual(point.x, 50)
        self.assertGreaterEqual(point.y, -50)
        self.assertLessEqual(point.y, 50)
    
    def test_circle_random_generation(self):
        """!
        @test
        @brief Tests random Circle generation with valid properties.
        """
        circle = Circle.generate_random(x_range=(0, 100), y_range=(0, 100), radius_range=(5, 50))
        self.assertIsInstance(circle, Circle)
        self.assertIsInstance(circle.center, Point)
        self.assertGreaterEqual(circle.radius, 5)
        self.assertLessEqual(circle.radius, 50)
    
    def test_polygon_random_generation(self):
        """!
        @test
        @brief Tests random Polygon generation with specified number of vertices.
        """
        polygon = Polygon.generate_random(num_vertices=6, x_range=(0, 100), y_range=(0, 100))
        self.assertIsInstance(polygon, Polygon)
        self.assertEqual(len(polygon.points), 6)
        for point in polygon.points:
            self.assertIsInstance(point, Point)
    
    def test_polygon_regular_generation(self):
        """!
        @test
        @brief Tests regular polygon generation with uniform vertices.
        """
        hexagon = Polygon.generate_regular_polygon(6, radius=10, center=Point(0, 0))
        self.assertIsInstance(hexagon, Polygon)
        self.assertEqual(len(hexagon.points), 6)
        distances = [Point(0, 0).distance_to(p) for p in hexagon.points]
        for dist in distances:
            self.assertTrue(isclose(dist, 10, rel_tol=0.01))


class TestSerialization(unittest.TestCase):
    """!
    @brief Test suite for serialization/deserialization (to_dict/from_dict).
    
    @details Verifies that objects can be converted to dictionaries and
    reconstructed correctly with all properties preserved.
    """
    
    def test_treenode_serialization(self):
        """!
        @test
        @brief Tests TreeNode serialization and deserialization.
        """
        root = TreeNode("root")
        child1 = TreeNode("child1")
        child2 = TreeNode("child2")
        root.add_child(child1)
        root.add_child(child2)
        
        # Serialize
        data = root.to_dict()
        self.assertIsInstance(data, dict)
        self.assertEqual(data['value'], "root")
        self.assertEqual(len(data['children']), 2)
        
        # Deserialize
        reconstructed = TreeNode.from_dict(data)
        self.assertEqual(reconstructed.value, "root")
        self.assertEqual(len(reconstructed.children), 2)
        self.assertEqual(reconstructed.traverse_dfs(), root.traverse_dfs())
    
    def test_binarytreenode_serialization(self):
        """!
        @test
        @brief Tests BinaryTreeNode serialization and deserialization.
        """
        bst = BinaryTreeNode(50)
        bst.insert_bst(30)
        bst.insert_bst(70)
        bst.insert_bst(20)
        
        # Serialize
        data = bst.to_dict()
        self.assertIsInstance(data, dict)
        self.assertEqual(data['value'], 50)
        
        # Deserialize
        reconstructed = BinaryTreeNode.from_dict(data)
        self.assertEqual(reconstructed.inorder(), bst.inorder())
        self.assertEqual(reconstructed.preorder(), bst.preorder())
    
    def test_point_serialization(self):
        """!
        @test
        @brief Tests Point serialization and deserialization.
        """
        point = Point(3.5, -7.2)
        
        data = point.to_dict()
        self.assertEqual(data['x'], 3.5)
        self.assertEqual(data['y'], -7.2)
        
        reconstructed = Point.from_dict(data)
        self.assertEqual(reconstructed.x, point.x)
        self.assertEqual(reconstructed.y, point.y)
    
    def test_circle_serialization(self):
        """!
        @test
        @brief Tests Circle serialization and deserialization.
        """
        circle = Circle(Point(10, 20), 15)
        
        data = circle.to_dict()
        self.assertIn('center', data)
        self.assertIn('radius', data)
        self.assertEqual(data['radius'], 15)
        
        reconstructed = Circle.from_dict(data)
        self.assertEqual(reconstructed.center.x, circle.center.x)
        self.assertEqual(reconstructed.center.y, circle.center.y)
        self.assertEqual(reconstructed.radius, circle.radius)
    
    def test_polygon_serialization(self):
        """!
        @test
        @brief Tests Polygon serialization and deserialization.
        """
        polygon = Polygon([Point(0, 0), Point(10, 0), Point(5, 10)])
        
        data = polygon.to_dict()
        self.assertIn('points', data)
        self.assertEqual(len(data['points']), 3)
        
        reconstructed = Polygon.from_dict(data)
        self.assertEqual(len(reconstructed.points), len(polygon.points))
        self.assertTrue(isclose(reconstructed.area(), polygon.area()))


class TestFileIO(unittest.TestCase):
    """!
    @brief Test suite for file I/O operations.
    
    @details Verifies that objects can be saved to and loaded from JSON files.
    """
    
    def setUp(self):
        """Set up test fixtures - track files to clean up."""
        self.test_files = []
    
    def tearDown(self):
        """Clean up test files after each test."""
        for filename in self.test_files:
            if os.path.exists(filename):
                try:
                    os.remove(filename)
                except:
                    pass
    
    def test_save_and_load_treenode(self):
        """!
        @test
        @brief Tests saving and loading TreeNode to/from JSON file.
        """
        filename = "test_tree.json"
        self.test_files.append(filename)
        
        root = TreeNode(100)
        root.add_child(TreeNode(50))
        root.add_child(TreeNode(150))
        
        save_to_file(root, filename)
        self.assertTrue(os.path.exists(filename))
        
        loaded = load_from_file(filename, TreeNode)
        self.assertEqual(loaded.value, root.value)
        self.assertEqual(loaded.traverse_dfs(), root.traverse_dfs())
    
    def test_save_and_load_circle(self):
        """!
        @test
        @brief Tests saving and loading Circle to/from JSON file.
        """
        filename = "test_circle.json"
        self.test_files.append(filename)
        
        circle = Circle(Point(5, 10), 7.5)
        
        save_to_file(circle, filename)
        self.assertTrue(os.path.exists(filename))
        
        loaded = load_from_file(filename, Circle)
        self.assertEqual(loaded.center.x, circle.center.x)
        self.assertEqual(loaded.radius, circle.radius)


class TestGeometricAlgorithms(unittest.TestCase):
    """!
    @brief Test suite for geometric algorithms (area, perimeter, center of mass).
    
    @details Verifies correctness of geometric calculations.
    """
    
    def test_circle_area(self):
        """!
        @test
        @brief Tests circle area calculation (πr²).
        """
        circle = Circle(Point(0, 0), 5)
        expected_area = 3.14159 * 25
        self.assertTrue(isclose(circle.area(), expected_area, rel_tol=0.01))
    
    def test_polygon_area_square(self):
        """!
        @test
        @brief Tests polygon area calculation for a square.
        """
        square = Polygon([Point(0, 0), Point(10, 0), Point(10, 10), Point(0, 10)])
        self.assertTrue(isclose(square.area(), 100.0, abs_tol=0.01))
    
    def test_polygon_center_of_mass(self):
        """!
        @test
        @brief Tests center of mass calculation.
        """
        square = Polygon([Point(0, 0), Point(10, 0), Point(10, 10), Point(0, 10)])
        center = square.center_of_mass()
        self.assertTrue(isclose(center.x, 5.0, abs_tol=0.01))
        self.assertTrue(isclose(center.y, 5.0, abs_tol=0.01))


if __name__ == "__main__":
    unittest.main()