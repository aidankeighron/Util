from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None

def binary_tree_path_sum(root: Node, target: int) -> int:
    res = 0

    def dfs(node, path_sum):
        nonlocal res
        if node is None:
            return
        if path_sum == target:
            res += 1
        if node.left:
            dfs(node.left, path_sum + node.left.value)
        if node.right:
            dfs(node.right, path_sum + node.right.value)

    def path_sum(node):
        if node is None:
            return
        dfs(node, node.value)
        path_sum(node.left)
        path_sum(node.right)

    path_sum(root)

    return res

tree = Node(10)
tree.left = Node(5)
tree.right = Node(-3)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right.right = Node(11)
tree.left.left.left = Node(3)
tree.left.left.right = Node(-2)
tree.left.right.right = Node(1)

print(binary_tree_path_sum(tree, 8))
print(binary_tree_path_sum(tree, 7))
tree.right.right = Node(10)
print(binary_tree_path_sum(tree, 8))