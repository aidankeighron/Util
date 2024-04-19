from __future__ import annotations
from collections import defaultdict, deque
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None

def binary_tree_side_view(root: Node, right: bool) -> list:
    res = []
    def dfs(node, depth):
        if not node:
            return
        if depth == len(res):
            res.append(node.value)
        if right:
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
        else:
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
    dfs(root, 0)
    return res

def binary_tree_top_and_bottom_view(root: Node, top: bool) -> list:
    queue = deque([(root, 0)])
    seen = defaultdict(list)
    res = []
    while queue:
        node, order = queue.pop()

        seen[order].append(node.value)

        if node.left:
            queue.append((node.left, order-1))
        if node.right:
            queue.append((node.right, order+1))

    for _, values in sorted(seen.items(), key=lambda x: x[0]):
        if top:
            res.append(values[0])
        else:
            res.append(values[-1])

    return res

root =  Node(3, Node(9), Node(20, Node(15), Node(7)))

print(binary_tree_top_and_bottom_view(root, False))