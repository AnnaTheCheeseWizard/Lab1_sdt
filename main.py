import math

class TreeNode:
    """!
    @brief Represents a node in a general-purpose tree.
    
    This class allows for a variable number of children per node.
    """

    def __init__(self, value):
        """!
        @brief Initializes a TreeNode.

        @param value The stored value inside the node.
        """
        ## @var value
        # Stored value of the node.
        self.value = value
        ## @var children
        # List of child nodes (list[TreeNode]).
        self.children = []

    def add_child(self, child_node):
        """!
        @brief Adds a child node.

        @param child_node The node to be added to the list of children.
        """
        self.children.append(child_node)

    def remove_child_by_value(self, value):
        """!
        @brief Removes a child node by its value.

        Removes all children that match the specified value.

        @param value Value of the child node(s) to remove.
        """
        self.children = [child for child in self.children if child.value != value]

    def find(self, value):
        """!
        @brief Searches for a node with the given value in the subtree.

        Performs a recursive search.

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
        @brief Performs depth-first traversal of the tree.

        @return list A list of node values in DFS order.
        """
        result = [self.value]
        for child in self.children:
            result.extend(child.traverse_dfs())
        return result

    def traverse_bfs(self):
        """!
        @brief Performs breadth-first traversal of the tree.

        @return list A list of node values in BFS order.
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
    @brief Represents a node in a binary search tree (BST).

    Each node has at most two children: left and right.
    """

    def __init__(self, value):
        """!
        @brief Initializes a BinaryTreeNode.

        @param value Value stored in the node.
        """
        ## @var value
        # The value stored in the node.
        self.value = value
        ## @var left
        # Left child node (BinaryTreeNode | None).
        self.left = None
        ## @var right
        # Right child node (BinaryTreeNode | None).
        self.right = None

    def insert_bst(self, value):
        """!
        @brief Inserts a new value into the BST.

        Maintains the BST property: left < root < right.

        @param value Value to insert.
        """
        if value < self.value:
            if self.left:
                self.left.insert_bst(value)
            else:
                self.left = BinaryTreeNode(value)
        else:
            if self.right:
                self.right.insert_bst(value)
            else:
                self.right = BinaryTreeNode(value)

    def search(self, value):
        """!
        @brief Searches for a value in the BST.

        @param value The value to search for.
        @return BinaryTreeNode | None Returns the found node or None.
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
        @brief Returns inorder traversal (Left-Root-Right).

        @return list Sorted list of values.
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
        @brief Returns preorder traversal (Root-Left-Right).

        @return list Values in preorder sequence.
        """
        result = [self.value]
        if self.left:
            result.extend(self.left.preorder())
        if self.right:
            result.extend(self.right.preorder())
        return result

    def postorder(self):
        """!
        @brief Returns postorder traversal (Left-Right-Root).

        @return list Values in postorder sequence.
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
    @brief Represents a point in 2D space.
    """

    def __init__(self, x, y):
        """!
        @brief Initializes a point.

        @param x X-coordinate.
        @param y Y-coordinate.
        """
        ## @var x
        # X-coordinate (float).
        self.x = x
        ## @var y
        # Y-coordinate (float).
        self.y = y

    def move(self, dx, dy):
        """!
        @brief Moves the point by a given offset.

        @param dx Shift along the X-axis.
        @param dy Shift along the Y-axis.
        @return Point A new Point instance at the moved coordinates.
        """
        return Point(self.x + dx, self.y + dy)

    def scale(self, factor):
        """!
        @brief Scales the point coordinates relative to the origin.

        @param factor Scaling factor.
        @return Point A new scaled Point instance.
        """
        return Point(self.x * factor, self.y * factor)

    def invert(self):
        """!
        @brief Inverts the point through the origin.

        @return Point A new Point instance with inverted coordinates.
        """
        return Point(-self.x, -self.y)


class LineSegment:
    """!
    @brief Represents a line segment defined by two points.
    """

    def __init__(self, p1: Point, p2: Point):
        """!
        @brief Initializes a line segment.

        @param p1 The starting Point.
        @param p2 The ending Point.
        """
        ## @var p1
        # Starting point of the segment.
        self.p1 = p1
        ## @var p2
        # Ending point of the segment.
        self.p2 = p2


class Circle:
    """!
    @brief Represents a circle in 2D space.
    """

    def __init__(self, center: Point, radius: float):
        """!
        @brief Initializes a circle.

        @param center The center Point of the circle.
        @param radius The radius of the circle.
        """
        ## @var center
        # Center point of the circle.
        self.center = center
        ## @var radius
        # Radius of the circle.
        self.radius = radius

    def move(self, dx, dy):
        """!
        @brief Moves the circle by shifting its center.

        @param dx Shift along X-axis.
        @param dy Shift along Y-axis.
        @return Circle A new Circle instance at the moved position.
        """
        return Circle(self.center.move(dx, dy), self.radius)

    def scale(self, factor):
        """!
        @brief Scales the circle.

        Scales both the center position (relative to origin) and the radius.

        @param factor Scaling factor.
        @return Circle A new scaled Circle instance.
        """
        return Circle(self.center.scale(factor), self.radius * factor)

    def invert(self):
        """!
        @brief Inverts the circle across the origin.

        Inverts the center point; radius remains unchanged.

        @return Circle A new inverted Circle instance.
        """
        return Circle(self.center.invert(), self.radius)


class Polygon:
    """!
    @brief Represents a polygon defined by a sequence of points.
    """

    def __init__(self, points):
        """!
        @brief Initializes a polygon.

        @param points A list of Point objects representing vertices.
        """
        ## @var points
        # List of vertices (list[Point]).
        self.points = points

    def move(self, dx, dy):
        """!
        @brief Moves the polygon by shifting all vertices.

        @param dx Shift along X-axis.
        @param dy Shift along Y-axis.
        @return Polygon A new Polygon instance with moved vertices.
        """
        return Polygon([p.move(dx, dy) for p in self.points])

    def scale(self, factor):
        """!
        @brief Scales the polygon by scaling all vertex coordinates.

        @param factor Scale multiplier.
        @return Polygon A new Polygon instance with scaled vertices.
        """
        return Polygon([p.scale(factor) for p in self.points])

    def invert(self):
        """!
        @brief Inverts the polygon through the origin.

        @return Polygon A new Polygon instance with inverted vertices.
        """
        return Polygon([p.invert() for p in self.points])