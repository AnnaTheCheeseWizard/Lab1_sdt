# Geometry & Tree Structures Library 
 This Python project serves as a comprehensive collection of fundamental **data structures** (Trees, BSTs) and **geometric objects** (Points, Circles, Polygons) with implemented traversal algorithms and transformation methods.

#  Core Modules & Functionality

The codebase is split into two primary areas, implemented in `main.py`:

## Tree Structures (`TreeNode`, `BinaryTreeNode`)
    General Tree:Supports arbitrary number of children, Depth-First Search (DFS), and Breadth-First Search (BFS) traversals.
    Binary Search Tree (BST): Optimized insertion and search operations. Supports Inorder, Preorder, and Postorder traversals.

## Geometry on the Plane (`Point`, `Circle`, `Polygon`)
    Objects: Provides basic geometric primitives.
    Transformations: All objects support operations like translation (`move`), scaling (`scale`), and inversion (`invert`). All transformations return new immutable objects.

#  Setup and Usage

## Prerequisites
You need Python 3.x installed. The project uses standard library modules only (`math`, `unittest`).

## Installation
```bash
# Clone the repository
git clone https://github.com/AnnaTheCheeseWizard/Lab1_sdt.git
cd Lab1_sdt
```
# Running Tests
All structural and geometric implementations are covered by included unit tests in `test_main.py`.

```bash
python3 test_main.py
```
# Documentation (API Reference)
This project uses Doxygen to generate a full API reference. The documentation is automatically built and published by a GitHub Action workflow whenever changes are pushed to the relevant branches. 
The up-to-date technical documentation (API Reference) for all classes and methods is available here:

View Documentation on GitHub Pages,[ View Documentation on GitHub Pages](https://annathecheesewizard.github.io/Lab1_sdt/) 