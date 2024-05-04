from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    data: any
    next_node: Node | None = None

def detect_cycle(head: Node) -> bool:
    if not head:
        return False

    slow = head
    fast = head
    while fast and fast.next_node:
        slow = slow.next_node if slow else None
        fast = fast.next_node.next_node
        if slow == fast:
            return True

    return False

head = Node(1)
head.next_node = Node(2)
head.next_node.next_node = Node(3)
head.next_node.next_node.next_node = Node(4)
head.next_node.next_node.next_node.next_node = Node(5)
head.next_node.next_node.next_node.next_node.next_node = head

print(detect_cycle(head))