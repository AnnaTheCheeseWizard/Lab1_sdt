"""!
@file main.py
@brief Library for fundamental data structures (General Tree, BST) and 2D geometric shapes.

@details This module provides basic implementations for tree nodes (general N-ary and binary search tree)
and common geometric primitives (Point, LineSegment, Circle, Polygon) with transformation methods.
"""

import math
import random
import json

class TreeNode:
    """!
    @brief Represents a node in a general N-ary tree (can have multiple children).
    
    @details Implements core tree operations including adding/removing children, Depth-First Search (DFS),
    Breadth-First Search (BFS), and value lookup.
    """
    
    ## @name Public Attributes
    # @{
    ## @var value
    # Stores the data contained in the node (of any type).
    #
    ## @var children
    # A list of child nodes (list[TreeNode]) attached to the current node.
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

    def __str__(self):
        """!
        @brief Returns a string representation of the tree.
        @return str String representation showing the tree structure.
        """
        return self._str_helper(0)

    def _str_helper(self, level):
        """Helper method for string representation with indentation."""
        indent = "  " * level
        result = f"{indent}{self.value}\n"
        for child in self.children:
            result += child._str_helper(level + 1)
        return result

    def __repr__(self):
        """!
        @brief Returns a detailed representation of the node.
        @return str Representation string.
        """
        return f"TreeNode(value={self.value}, children={len(self.children)})"

    @staticmethod
    def generate_random(max_depth=3, max_children=4, value_range=(1, 100)):
        """!
        @brief Generates a random tree with random values.
        @param max_depth Maximum depth of the tree.
        @param max_children Maximum number of children per node.
        @param value_range Tuple (min, max) for random values.
        @return TreeNode Root of the randomly generated tree.
        """
        def _generate_helper(depth):
            if depth >= max_depth:
                return None
            node = TreeNode(random.randint(*value_range))
            num_children = random.randint(0, max_children)
            for _ in range(num_children):
                child = _generate_helper(depth + 1)
                if child:
                    node.add_child(child)
            return node
        return _generate_helper(0)

    def to_dict(self):
        """!
        @brief Converts the tree to a dictionary for JSON serialization.
        @return dict Dictionary representation of the tree.
        """
        return {
            'value': self.value,
            'children': [child.to_dict() for child in self.children]
        }

    @staticmethod
    def from_dict(data):
        """!
        @brief Creates a tree from a dictionary.
        @param data Dictionary representation of the tree.
        @return TreeNode Root of the reconstructed tree.
        """
        node = TreeNode(data['value'])
        for child_data in data.get('children', []):
            node.add_child(TreeNode.from_dict(child_data))
        return node

class BinaryTreeNode:
    """!
    @brief Represents a node in a Binary Search Tree (BST).
    
    @details Each node has at most two children (left and right). Implements BST insertion,
    searching, and the three standard traversal methods.
    """

    ## @name Public Attributes
    # @{
    ## @var value
    # The value stored in the node.
    #
    ## @var left
    # The left child node (BinaryTreeNode | None).
    #
    ## @var right
    # The right child node (BinaryTreeNode | None).
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

    def __str__(self):
        """!
        @brief Returns a string representation of the BST.
        @return str String representation showing the tree structure.
        """
        return self._str_helper(0, "Root")

    def _str_helper(self, level, prefix):
        """Helper method for string representation with indentation."""
        indent = "  " * level
        result = f"{indent}{prefix}: {self.value}\n"
        if self.left:
            result += self.left._str_helper(level + 1, "L")
        if self.right:
            result += self.right._str_helper(level + 1, "R")
        return result

    def __repr__(self):
        """!
        @brief Returns a detailed representation of the node.
        @return str Representation string.
        """
        return f"BinaryTreeNode(value={self.value})"

    @staticmethod
    def generate_random(size=10, value_range=(1, 100)):
        """!
        @brief Generates a random BST with random values.
        @param size Number of nodes to generate.
        @param value_range Tuple (min, max) for random values.
        @return BinaryTreeNode Root of the randomly generated BST.
        """
        if size == 0:
            return None
        values = random.sample(range(*value_range), min(size, value_range[1] - value_range[0]))
        root = BinaryTreeNode(values[0])
        for val in values[1:]:
            root.insert_bst(val)
        return root

    def to_dict(self):
        """!
        @brief Converts the BST to a dictionary for JSON serialization.
        @return dict Dictionary representation of the BST.
        """
        return {
            'value': self.value,
            'left': self.left.to_dict() if self.left else None,
            'right': self.right.to_dict() if self.right else None
        }

    @staticmethod
    def from_dict(data):
        """!
        @brief Creates a BST from a dictionary.
        @param data Dictionary representation of the BST.
        @return BinaryTreeNode Root of the reconstructed BST.
        """
        if data is None:
            return None
        node = BinaryTreeNode(data['value'])
        node.left = BinaryTreeNode.from_dict(data.get('left'))
        node.right = BinaryTreeNode.from_dict(data.get('right'))
        return node


class Point:
    """!
    @brief Represents a 2D geometric point (x, y).
    
    @details Provides methods for standard geometric transformations, returning a new Point object each time (immutable pattern).
    """

    ## @name Public Attributes
    # @{
    ## @var x
    # The X-coordinate (float).
    #
    ## @var y
    # The Y-coordinate (float).
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

    def distance_to(self, other):
        """!
        @brief Calculates the Euclidean distance to another point.
        @param other Another Point object.
        @return float The distance between the two points.
        """
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __str__(self):
        """!
        @brief Returns a string representation of the point.
        @return str String in format "(x, y)".
        """
        return f"({self.x:.2f}, {self.y:.2f})"

    def __repr__(self):
        """!
        @brief Returns a detailed representation of the point.
        @return str Representation string.
        """
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        """!
        @brief Checks equality between two points.
        @param other Another Point object.
        @return bool True if points are equal.
        """
        if not isinstance(other, Point):
            return False
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)

    @staticmethod
    def generate_random(x_range=(-100, 100), y_range=(-100, 100)):
        """!
        @brief Generates a random point.
        @param x_range Tuple (min, max) for X coordinate.
        @param y_range Tuple (min, max) for Y coordinate.
        @return Point A randomly generated point.
        """
        x = random.uniform(*x_range)
        y = random.uniform(*y_range)
        return Point(x, y)

    def to_dict(self):
        """!
        @brief Converts the point to a dictionary.
        @return dict Dictionary with x and y coordinates.
        """
        return {'x': self.x, 'y': self.y}

    @staticmethod
    def from_dict(data):
        """!
        @brief Creates a point from a dictionary.
        @param data Dictionary with 'x' and 'y' keys.
        @return Point The reconstructed point.
        """
        return Point(data['x'], data['y'])

class LineSegment:
    """!
    @brief Represents a line segment defined by two Point objects.
    """

    ## @name Public Attributes
    # @{
    ## @var p1
    # The starting point of the segment (Point object).
    #
    ## @var p2
    # The ending point of the segment (Point object).
    # @}

    def __init__(self, p1: Point, p2: Point):
        """!
        @brief Constructor for the LineSegment.
        @param p1 The first endpoint (Point object).
        @param p2 The second endpoint (Point object).
        """
        self.p1 = p1
        self.p2 = p2

    def length(self):
        """!
        @brief Calculates the length of the line segment.
        @return float The length of the segment.
        """
        return self.p1.distance_to(self.p2)

    def move(self, dx, dy):
        """!
        @brief Translates the line segment.
        @param dx The displacement along the X-axis.
        @param dy The displacement along the Y-axis.
        @return LineSegment A new LineSegment object.
        """
        return LineSegment(self.p1.move(dx, dy), self.p2.move(dx, dy))

    def scale(self, factor):
        """!
        @brief Scales the line segment relative to the origin.
        @param factor The scaling factor.
        @return LineSegment A new LineSegment object.
        """
        return LineSegment(self.p1.scale(factor), self.p2.scale(factor))

    def invert(self):
        """!
        @brief Inverts the line segment through the origin.
        @return LineSegment A new LineSegment object.
        """
        return LineSegment(self.p1.invert(), self.p2.invert())

    def __str__(self):
        """!
        @brief Returns a string representation of the line segment.
        @return str String representation.
        """
        return f"LineSegment[{self.p1} -> {self.p2}]"

    def __repr__(self):
        """!
        @brief Returns a detailed representation of the line segment.
        @return str Representation string.
        """
        return f"LineSegment(p1={repr(self.p1)}, p2={repr(self.p2)})"

    @staticmethod
    def generate_random(x_range=(-100, 100), y_range=(-100, 100)):
        """!
        @brief Generates a random line segment.
        @param x_range Tuple (min, max) for X coordinates.
        @param y_range Tuple (min, max) for Y coordinates.
        @return LineSegment A randomly generated line segment.
        """
        p1 = Point.generate_random(x_range, y_range)
        p2 = Point.generate_random(x_range, y_range)
        return LineSegment(p1, p2)

    def to_dict(self):
        """!
        @brief Converts the line segment to a dictionary.
        @return dict Dictionary representation.
        """
        return {'p1': self.p1.to_dict(), 'p2': self.p2.to_dict()}

    @staticmethod
    def from_dict(data):
        """!
        @brief Creates a line segment from a dictionary.
        @param data Dictionary representation.
        @return LineSegment The reconstructed line segment.
        """
        return LineSegment(Point.from_dict(data['p1']), Point.from_dict(data['p2']))


class Circle:
    """!
    @brief Represents a circle defined by a center Point and a radius.
    """

    ## @name Public Attributes
    # @{
    ## @var center
    # The center of the circle (Point object).
    #
    ## @var radius
    # The radius of the circle (float).
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

    def area(self):
        """!
        @brief Calculates the area of the circle.
        @return float The area (π * r²).
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """!
        @brief Calculates the perimeter (circumference) of the circle.
        @return float The perimeter (2π * r).
        """
        return 2 * math.pi * self.radius

    def contains_point(self, point: Point):
        """!
        @brief Checks if a point is inside the circle.
        @param point The Point to check.
        @return bool True if the point is inside or on the circle.
        """
        return self.center.distance_to(point) <= self.radius

    def intersects_circle(self, other):
        """!
        @brief Checks if this circle intersects with another circle.
        @param other Another Circle object.
        @return bool True if circles intersect.
        """
        distance = self.center.distance_to(other.center)
        return distance <= (self.radius + other.radius)

    def __str__(self):
        """!
        @brief Returns a string representation of the circle.
        @return str String representation.
        """
        return f"Circle[center={self.center}, radius={self.radius:.2f}]"

    def __repr__(self):
        """!
        @brief Returns a detailed representation of the circle.
        @return str Representation string.
        """
        return f"Circle(center={repr(self.center)}, radius={self.radius})"

    @staticmethod
    def generate_random(x_range=(-100, 100), y_range=(-100, 100), radius_range=(1, 50)):
        """!
        @brief Generates a random circle.
        @param x_range Tuple (min, max) for X coordinate of center.
        @param y_range Tuple (min, max) for Y coordinate of center.
        @param radius_range Tuple (min, max) for radius.
        @return Circle A randomly generated circle.
        """
        center = Point.generate_random(x_range, y_range)
        radius = random.uniform(*radius_range)
        return Circle(center, radius)

    def to_dict(self):
        """!
        @brief Converts the circle to a dictionary.
        @return dict Dictionary representation.
        """
        return {'center': self.center.to_dict(), 'radius': self.radius}

    @staticmethod
    def from_dict(data):
        """!
        @brief Creates a circle from a dictionary.
        @param data Dictionary representation.
        @return Circle The reconstructed circle.
        """
        return Circle(Point.from_dict(data['center']), data['radius'])

class Polygon:
    """!
    @brief Represents a polygon defined by a list of Point objects (vertices).
    """

    ## @name Public Attributes
    # @{
    ## @var points
    # A list of the polygon's vertices (list[Point]).
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

    def area(self):
        """!
        @brief Calculates the area of the polygon using the Shoelace formula.
        @return float The area of the polygon (always positive).
        """
        if len(self.points) < 3:
            return 0.0
        total = 0.0
        n = len(self.points)
        for i in range(n):
            j = (i + 1) % n
            total += self.points[i].x * self.points[j].y
            total -= self.points[j].x * self.points[i].y
        return abs(total) / 2.0

    def perimeter(self):
        """!
        @brief Calculates the perimeter of the polygon.
        @return float The total length of all edges.
        """
        if len(self.points) < 2:
            return 0.0
        total = 0.0
        n = len(self.points)
        for i in range(n):
            j = (i + 1) % n
            total += self.points[i].distance_to(self.points[j])
        return total

    def center_of_mass(self):
        """!
        @brief Calculates the center of mass (centroid) of the polygon.
        @return Point The centroid of the polygon.
        """
        if not self.points:
            return Point(0, 0)
        if len(self.points) == 1:
            return Point(self.points[0].x, self.points[0].y)
        if len(self.points) == 2:
            return Point((self.points[0].x + self.points[1].x) / 2,
                        (self.points[0].y + self.points[1].y) / 2)
        
        area = self.area()
        if area == 0:
            # Degenerate case: return average of points
            avg_x = sum(p.x for p in self.points) / len(self.points)
            avg_y = sum(p.y for p in self.points) / len(self.points)
            return Point(avg_x, avg_y)
        
        cx = 0.0
        cy = 0.0
        n = len(self.points)
        for i in range(n):
            j = (i + 1) % n
            cross = self.points[i].x * self.points[j].y - self.points[j].x * self.points[i].y
            cx += (self.points[i].x + self.points[j].x) * cross
            cy += (self.points[i].y + self.points[j].y) * cross
        
        # Account for signed area in calculation
        signed_area = 0.0
        for i in range(n):
            j = (i + 1) % n
            signed_area += self.points[i].x * self.points[j].y - self.points[j].x * self.points[i].y
        signed_area /= 2.0
        
        cx /= (6.0 * signed_area)
        cy /= (6.0 * signed_area)
        return Point(cx, cy)

    def bounding_box(self):
        """!
        @brief Calculates the axis-aligned bounding box of the polygon.
        @return tuple (min_x, min_y, max_x, max_y) The bounding box coordinates.
        """
        if not self.points:
            return (0, 0, 0, 0)
        min_x = min(p.x for p in self.points)
        max_x = max(p.x for p in self.points)
        min_y = min(p.y for p in self.points)
        max_y = max(p.y for p in self.points)
        return (min_x, min_y, max_x, max_y)

    def contains_point(self, point: Point):
        """!
        @brief Checks if a point is inside the polygon using ray casting algorithm.
        @param point The Point to check.
        @return bool True if the point is inside the polygon.
        """
        if len(self.points) < 3:
            return False
        
        n = len(self.points)
        inside = False
        
        j = n - 1
        for i in range(n):
            xi, yi = self.points[i].x, self.points[i].y
            xj, yj = self.points[j].x, self.points[j].y
            
            if ((yi > point.y) != (yj > point.y)) and \
               (point.x < (xj - xi) * (point.y - yi) / (yj - yi) + xi):
                inside = not inside
            
            j = i
        
        return inside

    def __str__(self):
        """!
        @brief Returns a string representation of the polygon.
        @return str String representation.
        """
        points_str = ", ".join(str(p) for p in self.points)
        return f"Polygon[{len(self.points)} vertices: {points_str}]"

    def __repr__(self):
        """!
        @brief Returns a detailed representation of the polygon.
        @return str Representation string.
        """
        return f"Polygon(points={[repr(p) for p in self.points]})"

    @staticmethod
    def generate_random(num_vertices=5, x_range=(-100, 100), y_range=(-100, 100)):
        """!
        @brief Generates a random polygon.
        @param num_vertices Number of vertices.
        @param x_range Tuple (min, max) for X coordinates.
        @param y_range Tuple (min, max) for Y coordinates.
        @return Polygon A randomly generated polygon.
        """
        points = [Point.generate_random(x_range, y_range) for _ in range(num_vertices)]
        return Polygon(points)

    @staticmethod
    def generate_regular_polygon(num_sides, radius=50, center=None):
        """!
        @brief Generates a regular polygon (e.g., equilateral triangle, square, etc.).
        @param num_sides Number of sides.
        @param radius Distance from center to vertex.
        @param center Center point (default is origin).
        @return Polygon A regular polygon.
        """
        if center is None:
            center = Point(0, 0)
        points = []
        for i in range(num_sides):
            angle = 2 * math.pi * i / num_sides
            x = center.x + radius * math.cos(angle)
            y = center.y + radius * math.sin(angle)
            points.append(Point(x, y))
        return Polygon(points)

    def to_dict(self):
        """!
        @brief Converts the polygon to a dictionary.
        @return dict Dictionary representation.
        """
        return {'points': [p.to_dict() for p in self.points]}

    @staticmethod
    def from_dict(data):
        """!
        @brief Creates a polygon from a dictionary.
        @param data Dictionary representation.
        @return Polygon The reconstructed polygon.
        """
        points = [Point.from_dict(p) for p in data['points']]
        return Polygon(points)


# File I/O Utilities 


def save_to_file(obj, filename):
    """!
    @brief Saves any object (with to_dict method) to a JSON file.
    @param obj The object to save (TreeNode, BinaryTreeNode, Point, Circle, Polygon, etc.)
    @param filename The name of the file to save to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(obj.to_dict(), f, indent=2, ensure_ascii=False)
    print(f"Object saved to {filename}")


def load_from_file(filename, obj_type):
    """!
    @brief Loads an object from a JSON file.
    @param filename The name of the file to load from.
    @param obj_type The class type (TreeNode, BinaryTreeNode, Point, Circle, Polygon, etc.)
    @return The reconstructed object.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return obj_type.from_dict(data)



# Geometric Operations 


class GeometricOperations:
    """!
    @brief Utility class for advanced geometric operations like intersection and union.
    """
    
    @staticmethod
    def circle_union_area(circle1: Circle, circle2: Circle):
        """!
        @brief Calculates the area of the union of two circles.
        @param circle1 First circle.
        @param circle2 Second circle.
        @return float The area of the union.
        """
        d = circle1.center.distance_to(circle2.center)
        r1, r2 = circle1.radius, circle2.radius
        
        if d >= r1 + r2:
            return circle1.area() + circle2.area()
        
        if d <= abs(r1 - r2):
            return max(circle1.area(), circle2.area())
        
        intersection_area = GeometricOperations.circle_intersection_area(circle1, circle2)
        return circle1.area() + circle2.area() - intersection_area
    
    @staticmethod
    def circle_intersection_area(circle1: Circle, circle2: Circle):
        """!
        @brief Calculates the area of intersection between two circles.
        @param circle1 First circle.
        @param circle2 Second circle.
        @return float The area of intersection.
        """
        d = circle1.center.distance_to(circle2.center)
        r1, r2 = circle1.radius, circle2.radius
        
        if d >= r1 + r2:
            return 0.0
        
        if d <= abs(r1 - r2):
            return math.pi * min(r1, r2) ** 2
        
        part1 = r1**2 * math.acos((d**2 + r1**2 - r2**2) / (2 * d * r1))
        part2 = r2**2 * math.acos((d**2 + r2**2 - r1**2) / (2 * d * r2))
        part3 = 0.5 * math.sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2))
        
        return part1 + part2 - part3
    
    @staticmethod
    def polygon_bounding_circle(polygon: Polygon):
        """!
        @brief Calculates an approximate bounding circle for a polygon (circumscribed circle approximation).
        @param polygon The polygon.
        @return Circle A circle that contains the polygon.
        """
        center = polygon.center_of_mass()
        max_distance = max(center.distance_to(p) for p in polygon.points)
        return Circle(center, max_distance)
    
    @staticmethod
    def polygon_inscribed_circle_approximation(polygon: Polygon):
        """!
        @brief Approximates the inscribed circle (largest circle inside polygon).
        @param polygon The polygon (should be convex for accurate results).
        @return Circle An approximate inscribed circle.
        """
        center = polygon.center_of_mass()
        
        min_distance = float('inf')
        n = len(polygon.points)
        
        for i in range(n):
            j = (i + 1) % n
 
            edge_start = polygon.points[i]
            edge_end = polygon.points[j]
            
            line_vec_x = edge_end.x - edge_start.x
            line_vec_y = edge_end.y - edge_start.y
            point_vec_x = center.x - edge_start.x
            point_vec_y = center.y - edge_start.y
            
            line_len_sq = line_vec_x**2 + line_vec_y**2
            if line_len_sq == 0:
                distance = center.distance_to(edge_start)
            else:
                t = max(0, min(1, (point_vec_x * line_vec_x + point_vec_y * line_vec_y) / line_len_sq))
                projection_x = edge_start.x + t * line_vec_x
                projection_y = edge_start.y + t * line_vec_y
                distance = center.distance_to(Point(projection_x, projection_y))
            
            min_distance = min(min_distance, distance)
        
        return Circle(center, min_distance)


# ============================================================================
# Demonstration Functions
# ============================================================================

def demonstrate_trees():
    """!
    @brief Demonstrates tree structures with various data types.
    """
    print("\n" + "="*70)
    print("DEMONSTRATION: TREE STRUCTURES")
    print("="*70)
    
    # General Tree with integers
    print("\n--- General Tree (N-ary) with integers ---")
    root = TreeNode(1)
    root.add_child(TreeNode(2))
    root.add_child(TreeNode(3))
    root.children[0].add_child(TreeNode(4))
    root.children[0].add_child(TreeNode(5))
    root.children[1].add_child(TreeNode(6))
    
    print("Tree Structure:")
    print(root)
    print(f"DFS Traversal: {root.traverse_dfs()}")
    print(f"BFS Traversal: {root.traverse_bfs()}")
    
    # Random tree
    print("\n--- Randomly Generated Tree ---")
    random_tree = TreeNode.generate_random(max_depth=3, max_children=3, value_range=(1, 50))
    print("Random Tree Structure:")
    print(random_tree)
    print(f"DFS: {random_tree.traverse_dfs()}")
    
    # Binary Search Tree
    print("\n--- Binary Search Tree with integers ---")
    bst = BinaryTreeNode(50)
    for val in [30, 70, 20, 40, 60, 80]:
        bst.insert_bst(val)
    
    print("BST Structure:")
    print(bst)
    print(f"Inorder (sorted): {bst.inorder()}")
    print(f"Preorder: {bst.preorder()}")
    print(f"Postorder: {bst.postorder()}")
    print(f"Search for 40: {'Found' if bst.search(40) else 'Not found'}")
    print(f"Search for 100: {'Found' if bst.search(100) else 'Not found'}")
    
    # Random BST
    print("\n--- Randomly Generated BST ---")
    random_bst = BinaryTreeNode.generate_random(size=10, value_range=(1, 100))
    print(f"Inorder: {random_bst.inorder()}")


def demonstrate_geometry():
    """!
    @brief Demonstrates geometric shapes and operations.
    """
    print("\n" + "="*70)
    print("DEMONSTRATION: GEOMETRIC SHAPES")
    print("="*70)
    
    # Points
    print("\n--- Points ---")
    p1 = Point(3, 4)
    p2 = Point(0, 0)
    print(f"Point 1: {p1}")
    print(f"Point 2: {p2}")
    print(f"Distance: {p1.distance_to(p2):.2f}")
    print(f"P1 moved by (1, 1): {p1.move(1, 1)}")
    print(f"P1 scaled by 2: {p1.scale(2)}")
    print(f"P1 inverted: {p1.invert()}")
    
    # Random points
    print("\n--- Random Points ---")
    for i in range(3):
        rp = Point.generate_random()
        print(f"Random point {i+1}: {rp}")
    
    # Line Segment
    print("\n--- Line Segment ---")
    line = LineSegment(Point(0, 0), Point(3, 4))
    print(f"Line: {line}")
    print(f"Length: {line.length():.2f}")
    
    # Circle
    print("\n--- Circle ---")
    circle = Circle(Point(0, 0), 5)
    print(f"Circle: {circle}")
    print(f"Area: {circle.area():.2f}")
    print(f"Perimeter: {circle.perimeter():.2f}")
    print(f"Contains (3, 3): {circle.contains_point(Point(3, 3))}")
    print(f"Contains (10, 10): {circle.contains_point(Point(10, 10))}")
    
    # Random circle
    print("\n--- Random Circle ---")
    rc = Circle.generate_random()
    print(f"{rc}")
    print(f"Area: {rc.area():.2f}")
    
    # Polygon
    print("\n--- Polygon (Triangle) ---")
    triangle = Polygon([Point(0, 0), Point(4, 0), Point(2, 3)])
    print(f"Triangle: {triangle}")
    print(f"Area: {triangle.area():.2f}")
    print(f"Perimeter: {triangle.perimeter():.2f}")
    print(f"Center of mass: {triangle.center_of_mass()}")
    print(f"Bounding box: {triangle.bounding_box()}")
    print(f"Contains (2, 1): {triangle.contains_point(Point(2, 1))}")
    
    # Regular polygon
    print("\n--- Regular Hexagon ---")
    hexagon = Polygon.generate_regular_polygon(6, radius=10)
    print(f"Hexagon: {hexagon}")
    print(f"Area: {hexagon.area():.2f}")
    print(f"Perimeter: {hexagon.perimeter():.2f}")
    print(f"Center of mass: {hexagon.center_of_mass()}")
    
    # Random polygon
    print("\n--- Random Polygon ---")
    rpoly = Polygon.generate_random(num_vertices=5)
    print(f"{rpoly}")
    print(f"Area: {rpoly.area():.2f}")


def demonstrate_geometric_operations():
    """!
    @brief Demonstrates advanced geometric operations (union, intersection).
    """
    print("\n" + "="*70)
    print("DEMONSTRATION: GEOMETRIC OPERATIONS")
    print("="*70)
    
    # Circle intersection and union
    print("\n--- Circle Intersection and Union ---")
    c1 = Circle(Point(0, 0), 5)
    c2 = Circle(Point(6, 0), 5)
    
    print(f"Circle 1: {c1}")
    print(f"Circle 2: {c2}")
    print(f"Circle 1 area: {c1.area():.2f}")
    print(f"Circle 2 area: {c2.area():.2f}")
    print(f"Circles intersect: {c1.intersects_circle(c2)}")
    print(f"Intersection area: {GeometricOperations.circle_intersection_area(c1, c2):.2f}")
    print(f"Union area: {GeometricOperations.circle_union_area(c1, c2):.2f}")
    
    # Overlapping circles
    print("\n--- Overlapping Circles ---")
    c3 = Circle(Point(0, 0), 5)
    c4 = Circle(Point(3, 0), 5)
    print(f"Circle 3: {c3}")
    print(f"Circle 4: {c4}")
    print(f"Intersection area: {GeometricOperations.circle_intersection_area(c3, c4):.2f}")
    print(f"Union area: {GeometricOperations.circle_union_area(c3, c4):.2f}")
    
    # Polygon special circles
    print("\n--- Polygon Special Circles ---")
    square = Polygon.generate_regular_polygon(4, radius=10)
    print(f"Square: {square}")
    
    bounding = GeometricOperations.polygon_bounding_circle(square)
    print(f"Bounding (circumscribed) circle: {bounding}")
    print(f"Bounding circle area: {bounding.area():.2f}")
    
    inscribed = GeometricOperations.polygon_inscribed_circle_approximation(square)
    print(f"Inscribed circle (approximation): {inscribed}")
    print(f"Inscribed circle area: {inscribed.area():.2f}")


def demonstrate_file_io():
    """!
    @brief Demonstrates file I/O capabilities (save/load).
    """
    print("\n" + "="*70)
    print("DEMONSTRATION: FILE I/O (Bonus Feature)")
    print("="*70)
    
    # Save and load tree
    print("\n--- Saving and Loading Tree ---")
    tree = TreeNode.generate_random(max_depth=2, max_children=2, value_range=(1, 20))
    print("Original tree:")
    print(tree)
    
    save_to_file(tree, "tree_data.json")
    loaded_tree = load_from_file("tree_data.json", TreeNode)
    print("Loaded tree:")
    print(loaded_tree)
    print(f"Original DFS: {tree.traverse_dfs()}")
    print(f"Loaded DFS: {loaded_tree.traverse_dfs()}")
    
    # Save and load polygon
    print("\n--- Saving and Loading Polygon ---")
    pentagon = Polygon.generate_regular_polygon(5, radius=20)
    print(f"Original polygon: {pentagon}")
    print(f"Original area: {pentagon.area():.2f}")
    
    save_to_file(pentagon, "polygon_data.json")
    loaded_polygon = load_from_file("polygon_data.json", Polygon)
    print(f"Loaded polygon: {loaded_polygon}")
    print(f"Loaded area: {loaded_polygon.area():.2f}")
    
    # Save and load circle
    print("\n--- Saving and Loading Circle ---")
    circle = Circle(Point(10, 20), 15)
    print(f"Original: {circle}")
    save_to_file(circle, "circle_data.json")
    loaded_circle = load_from_file("circle_data.json", Circle)
    print(f"Loaded: {loaded_circle}")


def main():
    """!
    @brief Main function to run all demonstrations.
    """
    print("\n" + "="*70)
    print(" LAB 1: OBJECT-ORIENTED PROGRAMMING - DATA STRUCTURES & GEOMETRY")
    print("="*70)
    
    demonstrate_trees()
    demonstrate_geometry()
    demonstrate_geometric_operations()
    
    try:
        demonstrate_file_io()
    except Exception as e:
        print(f"\nFile I/O demonstration skipped: {e}")
    
    print("\n" + "="*70)
    print(" ALL DEMONSTRATIONS COMPLETED")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()