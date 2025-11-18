import math

import math

class TreeNode:
    """
    Represents a node in a general-purpose tree.

    Attributes:
        value: Stored value of the node.
        children (list[TreeNode]): List of child nodes.
    """

    def __init__(self, value):
        """
        Initializes a TreeNode.

        Args:
            value: The stored value inside the node.
        """
        self.value = value
        self.children = []

    def add_child(self, child_node):
        """
        Adds a child node.

        Args:
            child_node (TreeNode): Node to be added.
        """
        self.children.append(child_node)

    def remove_child_by_value(self, value):
        """
        Removes a child node by its value.

        Args:
            value: Value of the child node to remove.
        """
        self.children = [child for child in self.children if child.value != value]

    def find(self, value):
        """
        Searches for a node with the given value in the subtree.

        Args:
            value: The value to search for.

        Returns:
            TreeNode | None: Found node or None if not found.
        """
        if self.value == value:
            return self
        for child in self.children:
            found = child.find(value)
            if found:
                return found
        return None

    def traverse_dfs(self):
        """
        Performs depth-first traversal of the tree.

        Returns:
            list: A list of node values in DFS order.
        """
        result = [self.value]
        for child in self.children:
            result.extend(child.traverse_dfs())
        return result

    def traverse_bfs(self):
        """
        Performs breadth-first traversal of the tree.

        Returns:
            list: A list of node values in BFS order.
        """
        result = []
        queue = [self]

        while queue:
            current = queue.pop(0)
            result.append(current.value)
            queue.extend(current.children)

        return result



class BinaryTreeNode:
    """
    Represents a node in a binary search tree (BST).

    Attributes:
        value: Stored value.
        left (BinaryTreeNode | None): Left subtree.
        right (BinaryTreeNode | None): Right subtree.
    """

    def __init__(self, value):
        """
        Initializes a BinaryTreeNode.

        Args:
            value: Value stored in the node.
        """
        self.value = value
        self.left = None
        self.right = None

    def insert_bst(self, value):
        """
        Inserts a new value into the BST.

        Args:
            value: Value to insert.
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
        """
        Searches for a value in the BST.

        Args:
            value: The value to search for.

        Returns:
            BinaryTreeNode | None: Found node or None.
        """
        if self.value == value:
            return self
        elif value < self.value and self.left:
            return self.left.search(value)
        elif value > self.value and self.right:
            return self.right.search(value)
        return None

    def inorder(self):
        """
        Returns inorder traversal (Left–Root–Right).

        Returns:
            list: Sorted list of values.
        """
        result = []
        if self.left:
            result.extend(self.left.inorder())
        result.append(self.value)
        if self.right:
            result.extend(self.right.inorder())
        return result

    def preorder(self):
        """
        Returns preorder traversal (Root–Left–Right).

        Returns:
            list: Values in preorder order.
        """
        result = [self.value]
        if self.left:
            result.extend(self.left.preorder())
        if self.right:
            result.extend(self.right.preorder())
        return result

    def postorder(self):
        """
        Returns postorder traversal (Left–Right–Root).

        Returns:
            list: Values in postorder order.
        """
        result = []
        if self.left:
            result.extend(self.left.postorder())
        if self.right:
            result.extend(self.right.postorder())
        result.append(self.value)
        return result



class Point:
    """
    Represents a point in 2D space.

    Attributes:
        x (float): X-coordinate.
        y (float): Y-coordinate.
    """

    def __init__(self, x, y):
        """
        Initializes a point.

        Args:
            x (float): X-coordinate.
            y (float): Y-coordinate.
        """
        self.x = x
        self.y = y

    def move(self, dx, dy):
        """
        Moves the point.

        Args:
            dx (float): Shift along the X-axis.
            dy (float): Shift along the Y-axis.

        Returns:
            Point: New moved point.
        """
        return Point(self.x + dx, self.y + dy)

    def scale(self, factor):
        """
        Scales the point.

        Args:
            factor (float): Scaling factor.

        Returns:
            Point: New scaled point.
        """
        return Point(self.x * factor, self.y * factor)

    def invert(self):
        """
        Inverts the point through the origin.

        Returns:
            Point: New inverted point.
        """
        return Point(-self.x, -self.y)



class LineSegment:
    """
    Represents a line segment defined by two points.

    Attributes:
        p1 (Point): Starting point.
        p2 (Point): Ending point.
    """

    def __init__(self, p1: Point, p2: Point):
        """
        Initializes a line segment.

        Args:
            p1 (Point): First endpoint.
            p2 (Point): Second endpoint.
        """
        self.p1 = p1
        self.p2 = p2



class Circle:
    """
    Represents a circle.

    Attributes:
        center (Point): Center of the circle.
        radius (float): Radius of the circle.
    """

    def __init__(self, center: Point, radius: float):
        """
        Initializes a circle.

        Args:
            center (Point): Center point.
            radius (float): Radius.
        """
        self.center = center
        self.radius = radius

    def move(self, dx, dy):
        """
        Moves the circle.

        Args:
            dx (float): Shift along X-axis.
            dy (float): Shift along Y-axis.

        Returns:
            Circle: New moved circle.
        """
        return Circle(self.center.move(dx, dy), self.radius)

    def scale(self, factor):
        """
        Scales the circle.

        Args:
            factor (float): Scaling factor.

        Returns:
            Circle: New scaled circle.
        """
        return Circle(self.center.scale(factor), self.radius * factor)

    def invert(self):
        """
        Inverts the circle across the origin.

        Returns:
            Circle: New inverted circle.
        """
        return Circle(self.center.invert(), self.radius)



class Polygon:
    """
    Represents a polygon defined by a sequence of points.

    Attributes:
        points (list[Point]): List of vertices.
    """

    def __init__(self, points):
        """
        Initializes a polygon.

        Args:
            points (list[Point]): List of polygon vertices.
        """
        self.points = points

    def move(self, dx, dy):
        """
        Moves the polygon by shifting all vertices.

        Args:
            dx (float): Shift along X.
            dy (float): Shift along Y.

        Returns:
            Polygon: New moved polygon.
        """
        return Polygon([p.move(dx, dy) for p in self.points])

    def scale(self, factor):
        """
        Scales the polygon by scaling all vertex coordinates.

        Args:
            factor (float): Scale multiplier.

        Returns:
            Polygon: New scaled polygon.
        """
        return Polygon([p.scale(factor) for p in self.points])

    def invert(self):
        """
        Inverts the polygon through the origin.

        Returns:
            Polygon: New inverted polygon.
        """
        return Polygon([p.invert() for p in self.points])
