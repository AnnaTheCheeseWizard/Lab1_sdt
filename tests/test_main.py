import unittest
from math import isclose
from main import TreeNode, BinaryTreeNode, Point, Circle, Polygon

class TestTreeStructures(unittest.TestCase):
# Тести для TreeNode
    def test_add_and_find_child(self):
        root = TreeNode("root")
        child = TreeNode("child")
        root.add_child(child)
        self.assertEqual(root.find("child"), child)
        self.assertIsNone(root.find("non_existent"))

    def test_remove_child_by_value(self):
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
# Тести для BinaryTreeNode
    def test_binary_tree_insertion_and_search(self):
        root = BinaryTreeNode(10)
        root.insert_bst(5)
        root.insert_bst(15)
        root.insert_bst(3)

        self.assertEqual(root.search(5).value, 5)
        self.assertEqual(root.search(15).value, 15)
        self.assertEqual(root.search(3).value, 3)

    def test_binary_tree_search_not_found(self):
        root = BinaryTreeNode(10)
        root.insert_bst(5)

        self.assertIsNone(root.search(99))
        self.assertIsNone(root.search(1))

    def test_binary_tree_inorder_traversal(self):
        root = BinaryTreeNode(10)
        root.insert_bst(5)
        root.insert_bst(15)
        root.insert_bst(3)
        root.insert_bst(7)
       
        self.assertEqual(root.inorder(), [3, 5, 7, 10, 15])

    def test_binary_tree_preorder_traversal(self):
        root = BinaryTreeNode(10)
        root.insert_bst(5)
        root.insert_bst(15)
        root.insert_bst(3)
        root.insert_bst(7)
        
        self.assertEqual(root.preorder(), [10, 5, 3, 7, 15])

    def test_binary_tree_postorder_traversal(self):
        root = BinaryTreeNode(10)
        root.insert_bst(5)
        root.insert_bst(15)
        root.insert_bst(3)
        root.insert_bst(7)
        self.assertEqual(root.postorder(), [3, 7, 5, 15, 10])

class TestGeometry(unittest.TestCase):
# Тести для Point 
    def test_point_move_immutability(self):
        p = Point(1, 2)
        moved = p.move(3, -1)
        self.assertEqual((moved.x, moved.y), (4, 1))      
        self.assertEqual((p.x, p.y), (1, 2))             

    def test_point_scale_immutability(self):
        p = Point(2, 3)
        scaled = p.scale(2)
        self.assertEqual((scaled.x, scaled.y), (4, 6))    
        self.assertEqual((p.x, p.y), (2, 3))               

    def test_point_invert_immutability(self):
        p = Point(2, -3)
        inverted = p.invert()
        self.assertEqual((inverted.x, inverted.y), (-2, 3))  
        self.assertEqual((p.x, p.y), (2, -3)) 

    def test_point_scale_zero(self):
        p = Point(5, -3)
        scaled = p.scale(0)
        self.assertEqual((scaled.x, scaled.y), (0, 0)) 
#Тести для LineSegment 
    def test_line_segment_creation(self):
        p1 = Point(1, 1)
        p2 = Point(5, 5)
        ls = LineSegment(p1, p2)
        self.assertEqual(ls.p1.x, 1)
        self.assertEqual(ls.p2.y, 5)
        self.assertIsInstance(ls.p1, Point)   
#Тести для Circle 
    def test_circle_move_immutability(self):
        c = Circle(Point(0, 0), 5)
        moved = c.move(2, 3)
        self.assertEqual((moved.center.x, moved.center.y), (2, 3))  
        self.assertEqual((c.center.x, c.center.y), (0, 0))          
        self.assertEqual(c.radius, 5)

    def test_circle_scale_immutability(self):
        c = Circle(Point(1, 1), 4)
        scaled = c.scale(0.5)
        self.assertTrue(isclose(scaled.radius, 2.0))
        self.assertEqual((scaled.center.x, scaled.center.y), (0.5, 0.5)) 
        self.assertEqual(c.radius, 4)
        self.assertEqual((c.center.x, c.center.y), (1, 1))

    def test_circle_invert_immutability(self):
        c = Circle(Point(1, -1), 3)
        inverted = c.invert()
        self.assertEqual((inverted.center.x, inverted.center.y), (-1, 1))  
        self.assertEqual((c.center.x, c.center.y), (1, -1))
        self.assertEqual(c.radius, 3)

    def test_circle_zero_radius(self):
        c = Circle(Point(0, 0), 0)
        scaled = c.scale(10)
        self.assertEqual(scaled.radius, 0)
        self.assertEqual((scaled.center.x, scaled.center.y), (0, 0))

    def test_circle_none_center(self):
        with self.assertRaises(AttributeError):
            Circle(None, 5).move(1, 1)
#Тести для Polygon
    def test_polygon_move_immutability(self):
        poly = Polygon([Point(0, 0), Point(1, 1)])
        moved = poly.move(2, 3)
        self.assertEqual([(p.x, p.y) for p in moved.points], [(2, 3), (3, 4)])  
        self.assertEqual([(p.x, p.y) for p in poly.points], [(0, 0), (1, 1)])  

    def test_polygon_scale_immutability(self):
        poly = Polygon([Point(1, 2), Point(3, 4)])
        scaled = poly.scale(2)
        self.assertEqual([(p.x, p.y) for p in scaled.points], [(2, 4), (6, 8)])  
        self.assertEqual([(p.x, p.y) for p in poly.points], [(1, 2), (3, 4)])    

    def test_polygon_invert_immutability(self):
        poly = Polygon([Point(1, -2), Point(-3, 4)])
        inverted = poly.invert()
        self.assertEqual([(p.x, p.y) for p in inverted.points], [(-1, 2), (3, -4)]) 
        self.assertEqual([(p.x, p.y) for p in poly.points], [(1, -2), (-3, 4)])

    def test_polygon_empty(self):
        poly = Polygon([])
        moved = poly.move(1, 1)
        self.assertEqual(len(moved.points), 0)

    def test_polygon_negative_scale(self):
        poly = Polygon([Point(1, 2)])
        scaled = poly.scale(-1)
        self.assertEqual([(p.x, p.y) for p in scaled.points], [(-1, -2)])
  
    def test_polygon_invert_empty(self):
        poly = Polygon([])
        inverted = poly.invert()
        self.assertEqual(len(inverted.points), 0)

if __name__ == "__main__":
    unittest.main()
