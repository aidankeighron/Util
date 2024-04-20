from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None

def distribute_coins(root: Node):

    def distribute(node):
        if node is None:
            return (0, 1)

        left_moves, left_excess = distribute(node.left)
        right_moves, right_excess = distribute(node.right)

        coins_to_left = 1 - left_excess
        coins_to_right = 1 - right_excess

        new_moves = left_moves + right_moves + abs(coins_to_left) + abs(coins_to_right)

        return (new_moves, node.value - coins_to_left - coins_to_right)

    return distribute(root)[0]

print(distribute_coins(Node(3, Node(0), Node(0))))
    # 2
print(distribute_coins(Node(0, Node(3), Node(0))))
    # 3
print(distribute_coins(Node(0, Node(0), Node(3))))
    # 3