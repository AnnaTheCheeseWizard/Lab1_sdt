import math

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child_by_value(self, value):
        self.children = [child for child in self.children if child.value != value]

    def find(self, value):
        if self.value == value:
            return self
        for child in self.children:
            found = child.find(value)
            if found:
                return found
        return None

    def traverse_dfs(self):
        result = [self.value]
        for child in self.children:
            result.extend(child.traverse_dfs())
        return result

    def traverse_bfs(self):
        result = []
        queue = [self]
        while queue:
            current = queue.pop(0)
            result.append(current.value)
            queue.extend(current.children)
        return result

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_bst(self, value):
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
        if self.value == value:
            return self
        elif value < self.value and self.left:
            return self.left.search(value)
        elif value > self.value and self.right:
            return self.right.search(value)
        return None

    def inorder(self):
        result = []
        if self.left:
            result.extend(self.left.inorder())
        result.append(self.value)
        if self.right:
            result.extend(self.right.inorder())
        return result

    def preorder(self):
        result = [self.value]
        if self.left:
            result.extend(self.left.preorder())
        if self.right:
            result.extend(self.right.preorder())
        return result

    def postorder(self):
        result = []
        if self.left:
            result.extend(self.left.postorder())
        if self.right:
            result.extend(self.right.postorder())
        result.append(self.value)
        return result


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        return Point(self.x + dx, self.y + dy)

    def scale(self, factor):
        return Point(self.x * factor, self.y * factor)

    def invert(self):
        return Point(-self.x, -self.y)

class LineSegment:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def move(self, dx, dy):
        return Circle(self.center.move(dx, dy), self.radius)

    def scale(self, factor):
        return Circle(self.center.scale(factor), self.radius * factor)

    def invert(self):
        return Circle(self.center.invert(), self.radius)

class Polygon:
    def __init__(self, points):
        self.points = points

    def move(self, dx, dy):
        return Polygon([p.move(dx, dy) for p in self.points])

    def scale(self, factor):
        return Polygon([p.scale(factor) for p in self.points])

    def invert(self):
        return Polygon([p.invert() for p in self.points])