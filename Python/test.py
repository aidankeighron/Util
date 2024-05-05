from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    data: any
    next_node: Node | None = None

def find_middle_element(head: Node) -> int:
    slow = head
    fast = head

    while fast and fast.next_node:
        fast = fast.next_node.next_node
        slow = slow.next_node
    return slow.data

head = Node(1)
head.next_node = Node(2)
head.next_node.next_node = Node(3)
head.next_node.next_node.next_node = Node(4)
head.next_node.next_node.next_node.next_node = Node(5)
# head.next_node.next_node.next_node.next_node.next_node = Node(6)

print(find_middle_element(head))