from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    data: any
    next_node: Node | None = None

def swap_nodes(head:Node, node_data_1: int, node_data_2: int) -> Node:
    node_1 = head
    while node_1 and node_1.data != node_data_1:
        node_1 = node_1.next_node
    node_2 = head
    while node_2 and node_2.data != node_data_2:
        node_2 = node_2.next_node
    node_1.data, node_2.data = node_2.data, node_1.data
    return head
head = Node(1)
head.next_node = Node(2)
head.next_node.next_node = Node(3)
head.next_node.next_node.next_node = Node(4)
head.next_node.next_node.next_node.next_node = Node(5)
# head.next_node.next_node.next_node.next_node.next_node = Node(6)

print(swap_nodes(head, 2, 4))