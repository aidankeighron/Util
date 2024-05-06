from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    data: any
    next_node: Node | None = None

def rotate(head: Node, places: int) -> Node:
    if not head.next_node:
        return head

    length = 1
    temp = head
    while temp.next_node:
        length += 1
        temp = temp.next_node

    new_head_index = length-places

    temp = head
    for _ in range(new_head_index-1):
        temp = temp.next_node
    
    new_head = temp.next_node
    temp.next_node = None
    temp = new_head
    while temp.next_node:
        temp = temp.next_node
    temp.next_node = head

    return new_head
head = Node(1)
head.next_node = Node(2)
head.next_node.next_node = Node(3)
head.next_node.next_node.next_node = Node(4)
head.next_node.next_node.next_node.next_node = Node(5)
# head.next_node.next_node.next_node.next_node.next_node = Node(6)

print(rotate(head, 3))