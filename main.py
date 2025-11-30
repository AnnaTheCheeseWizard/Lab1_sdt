"""!
@file main.py
@brief Library for fundamental data structures (General Tree, BST) and 2D geometric shapes.

@details This module provides basic implementations for tree nodes (general N-ary and binary search tree)
and common geometric primitives (Point, LineSegment, Circle, Polygon) with transformation methods.
"""

import math

class TreeNode:
    """!
    @brief Represents a node in a general N-ary tree (can have multiple children).
    
    @details Implements core tree operations including adding/removing children, Depth-First Search (DFS),
    Breadth-First Search (BFS), and value lookup.
    """
    
    ## @name Public Attributes
    # @{
    ## @var value
    # Зберігає дані, що знаходяться у вузлі (будь-якого типу).
    #
    ## @var children
    # Список дочірніх вузлів (list[TreeNode]), прикріплених до поточного вузла.
    # @}

    def __init__(self, value):
        """!
        @brief Constructor for a general tree node.
        @param value The data value stored in the node.
        """
        self.value = value
        self.children = []

    def add_child(self, child_node):
        """!
        @brief Adds a given TreeNode as a child to the current node.
        @param child_node The TreeNode object to add.
        """
        self.children.append(child_node)

    def remove_child_by_value(self, value):
        """!
        @brief Removes any child nodes whose value matches the given value.
        @param value The value of the child node(s) to remove.
        """
        self.children = [child for child in self.children if child.value != value]

    def find(self, value):
        """!
        @brief Searches for a node with the given value in the subtree.

        Performs a recursive search (DFS).

        @param value The value to search for.
        @return TreeNode | None Returns the found node or None if not found.
        """
        if self.value == value:
            return self
        for child in self.children:
            found = child.find(value)
            if found:
                return found
        return None

    def traverse_dfs(self):
        """!
        @brief Performs a recursive Depth-First Traversal (pre-order) starting from this node.
        @return list A list of node values in DFS order.
        """
        result = [self.value]
        for child in self.children:
            result.extend(child.traverse_dfs())
        return result

    def traverse_bfs(self):
        """!
        @brief Performs a Breadth-First Traversal (BFS) starting from this node.
        @return list A list of node values in BFS order (level-by-level).
        """
        result = []
        queue = [self]
        while queue:
            current = queue.pop(0)
            result.append(current.value)
            queue.extend(current.children)
        return result

class BinaryTreeNode:
    """!
    @brief Represents a node in a Binary Search Tree (BST).
    
    @details Each node has at most two children (left and right). Implements BST insertion,
    searching, and the three standard traversal methods.
    """

    ## @name Public Attributes
    # @{
    ## @var value
    # Значення, що зберігається у вузлі.
    #
    ## @var left
    # Лівий дочірній вузол (BinaryTreeNode | None).
    #
    ## @var right
    # Правий дочірній вузол (BinaryTreeNode | None).
    # @}

    def __init__(self, value):
        """!
        @brief Constructor for a binary tree node.
        @param value The data value stored in the node.
        """
        self.value = value
        self.left = None
        self.right = None

    def insert_bst(self, value):
        """!
        @brief Inserts a new value into the BST following the binary search tree rules.
        @param value The value to insert.
        """
        if value < self.value:
            if self.left:
                self.left.insert_bst(value)
            else:
                self.left = BinaryTreeNode(value)
        else: # Assumes right for equal or greater values
            if self.right:
                self.right.insert_bst(value)
            else:
                self.right = BinaryTreeNode(value)

    def search(self, value):
        """!
        @brief Searches the BST for a node containing the specified value.
        @param value The value to search for.
        @return BinaryTreeNode or None The node containing the value, or None if not found.
        """
        if self.value == value:
            return self
        elif value < self.value and self.left:
            return self.left.search(value)
        elif value > self.value and self.right:
            return self.right.search(value)
        return None

    def inorder(self):
        """!
        @brief Performs an Inorder traversal (Left, Root, Right).
        @return list A list of node values in ascending order (for a correct BST).
        """
        result = []
        if self.left:
            result.extend(self.left.inorder())
        result.append(self.value)
        if self.right:
            result.extend(self.right.inorder())
        return result

    def preorder(self):
        """!
        @brief Performs a Preorder traversal (Root, Left, Right).
        @return list A list of node values.
        """
        result = [self.value]
        if self.left:
            result.extend(self.left.preorder())
        if self.right:
            result.extend(self.right.preorder())
        return result

    def postorder(self):
        """!
        @brief Performs a Postorder traversal (Left, Right, Root).
        @return list A list of node values.
        """
        result = []
        if self.left:
            result.extend(self.left.postorder())
        if self.right:
            result.extend(self.right.postorder())
        result.append(self.value)
        return result


class Point:
    """!
    @brief Represents a 2D geometric point (x, y).
    
    @details Provides methods for standard geometric transformations, returning a new Point object each time (immutable pattern).
    """

    ## @name Public Attributes
    # @{
    ## @var x
    # X-координата (float).
    #
    ## @var y
    # Y-координата (float).
    # @}

    def __init__(self, x, y):
        """!
        @brief Constructor for the Point.
        @param x The X-coordinate.
        @param y The Y-coordinate.
        """
        self.x = x
        self.y = y

    def move(self, dx, dy):
        """!
        @brief Translates the point by given offsets.
        @param dx The displacement along the X-axis.
        @param dy The displacement along the Y-axis.
        @return Point A new Point object after the translation.
        """
        return Point(self.x + dx, self.y + dy)

    def scale(self, factor):
        """!
        @brief Scales the point relative to the origin (0,0).
        @param factor The scaling factor.
        @return Point A new Point object after scaling.
        """
        return Point(self.x * factor, self.y * factor)

    def invert(self):
        """!
        @brief Inverts the point's coordinates (reflection across the origin).
        @return Point A new Point object with inverted coordinates (-x, -y).
        """
        return Point(-self.x, -self.y)

class LineSegment:
    """!
    @brief Represents a line segment defined by two Point objects.
    """

    ## @name Public Attributes
    # @{
    ## @var p1
    # Початкова точка відрізка (Point object).
    #
    ## @var p2
    # Кінцева точка відрізка (Point object).
    # @}

    def __init__(self, p1: Point, p2: Point):
        """!
        @brief Constructor for the LineSegment.
        @param p1 The first endpoint (Point object).
        @param p2 The second endpoint (Point object).
        """
        self.p1 = p1
        self.p2 = p2


class Circle:
    """!
    @brief Represents a circle defined by a center Point and a radius.
    """

    ## @name Public Attributes
    # @{
    ## @var center
    # Центр кола (Point object).
    #
    ## @var radius
    # Радіус кола (float).
    # @}

    def __init__(self, center: Point, radius: float):
        """!
        @brief Constructor for the Circle.
        @param center The center of the circle (Point object).
        @param radius The radius of the circle.
        """
        self.center = center
        self.radius = radius

    def move(self, dx, dy):
        """!
        @brief Moves the circle by translating its center.
        @param dx The displacement along the X-axis.
        @param dy The displacement along the Y-axis.
        @return Circle A new Circle object.
        """
        return Circle(self.center.move(dx, dy), self.radius)

    def scale(self, factor):
        """!
        @brief Scales the circle (scales both the center and the radius).
        @param factor The scaling factor.
        @return Circle A new Circle object.
        """
        return Circle(self.center.scale(factor), self.radius * factor)

    def invert(self):
        """!
        @brief Inverts the circle by inverting its center.
        @return Circle A new Circle object.
        """
        return Circle(self.center.invert(), self.radius)

class Polygon:
    """!
    @brief Represents a polygon defined by a list of Point objects (vertices).
    """

    ## @name Public Attributes
    # @{
    ## @var points
    # Список вершин багатокутника (list[Point]).
    # @}

    def __init__(self, points):
        """!
        @brief Constructor for the Polygon.
        @param points A list of Point objects representing the vertices.
        """
        self.points = points

    def move(self, dx, dy):
        """!
        @brief Translates the polygon by moving all its vertices.
        @param dx The displacement along the X-axis.
        @param dy The displacement along the Y-axis.
        @return Polygon A new Polygon object after translation.
        """
        return Polygon([p.move(dx, dy) for p in self.points])

    def scale(self, factor):
        """!
        @brief Scales the polygon relative to the origin (0,0) by scaling all vertices.
        @param factor The scaling factor.
        @return Polygon A new Polygon object after scaling.
        """
        return Polygon([p.scale(factor) for p in self.points])

    def invert(self):
        """!
        @brief Inverts the polygon through the origin.
        @return Polygon A new Polygon instance with inverted vertices.
        """
        return Polygon([p.invert() for p in self.points])