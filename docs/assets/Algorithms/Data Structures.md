---
layout: script
language: Algorithms
---

# Permutations

Using a depth first search this algorithm creates a list of all possible reordering of a list. It does this by recursively testing all options.

```python
def permutations(collection: list) -> list:
    res = []
    collection.sort()
    cur = []
    def dfs(i):
        if cur not in res:
            res.append(cur.copy())
        if i >= len(collection):
            return
        cur.append(collection[i])
        dfs(i+1) # find all permutations with i

        cur.pop()
        dfs(i+1) # find all permutations without i
    dfs(0)

    return res
```

# Equilibrium Index in Array

Find the index where the right and left sections of an array are equal in sum.

```python
def equilibrium_index(arr: list) -> int:
    total_sum = sum(arr)
    left_sum = 0
    for i, value in enumerate(arr):
        total_sum -= value
        if left_sum == total_sum:
            return i
        left_sum += value
    return -1
```

# Product Sum

Product sum of an array is the sum of the array multiplied by their depths

```python
def product_sum(arr: list, depth: int) -> int:
    res = 0
    for x in arr:
        res += product_sum(x, depth+1) if isinstance(x, list) else x
    return res * depth
```

# Find Triplets with 0 Sum

Finds three numbers that add up to zero by finding two and seeing if there exists a number that when added to them results in zero

```python
def find_triplets_with_0_sum(arr: list) -> set:
    res = set()
    for i, item in enumerate(arr[:-2]):
        seen = set()
        for other in arr[i+1:]:
            to_find = -other-item
            if to_find in seen:
                res.add(tuple(sorted([item, other, to_find])))
            seen.add(other)
    return res
```

# Kth Largest Element

Finds the `position` largest element in `arr`.

```python
def kth_largest_element(arr: list, position: int) -> int:
    low, high = 0, len(arr) - 1

    def pivot_index():
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] >= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    while low <= high:
        if low > len(arr) - 1 or high < 0:
            return -1
        index = pivot_index()
        if index == position - 1:
            return arr[index]
        elif index > position - 1:
            high = index - 1
        else:
            low = index + 1
```

# Binary Tree Node Sum

Sums up all nodes in a binary tree

```python
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None

def binary_tree_sum(tree: Node) -> int:
    def dfs(node):
        if node is None:
            return 0
        return node.value + dfs(node.left) + dfs(node.right)
    return dfs(tree)
```

# Binary Tree Path Sum

Given a root and a target sum find the number of paths that sum up to the target

```python
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
```

# Diameter Of Binary Tree

Finds the diameter of a binary tree where the diameter is defined as the number of nodes on the longest path between two end nodes

```python
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None

def dimeter_of_binary_tree(root: Node) -> int:
    def depth(node):
        if not node:
            return 0
        return max(depth(node.left), depth(node.right)) + 1
    res = 0
    if root.left:
        res += depth(root.left)
    if root.right:
        res += depth(root.right)
    return res + 1
```

# Prime

Lists all prime numbers < n

```python
def list_primes(n: int) -> list:
    primes = []
    if n > 1:
        primes.append(1)
    if n > 2:
        primes.append(2)
    numbers = (i for i in range(1, (n+1), 2))
    for i in (n for n in numbers if n > 1):
        bound = int(i**0.5) + 1
        for j in range(3, bound, 2):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes
```

# Binary Tree Mirror

Return the mirror of a binary tree, flipping it around the root node.

```python
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None

def mirror_binary_tree(root: Node) -> Node:
    def mirror(node):
        if not node:
            return
        node.left, node.right = node.right, node.left
        mirror(node.left)
        mirror(node.right)
    mirror(root)
    return root
```

# Different Views of a Binary Tree

If you were to look at the binary tree from a certain perspective what would you see

```python
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
```

# Distribute Coins

Finds number of moves it would take for each node if the binary tree to have a value of one if you can only move one coin at a time

```python
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
```

# Flatten Binary Tree to LinkedList

Takes a binary tree and compresses it in-place into a linked list

```python
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None

def binary_tree_to_linked_list(root: Node) -> None:
    def flatten(node):
        if node is None:
            return
        flatten(node.left)
        right = node.right
        node.right = node.left
        node.left = None
        cur = node
        while cur.right:
            cur = cur.right
        
        cur.right = right
        flatten(right)
    flatten(root)
```

# Is Binary Tree Sorted

Checks if a binary tree is sorted, i.e. is it a valid BST, binary search tree.

```python
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None

def is_sorted(root: Node) -> bool:
    if root.left and (root.value < root.left.value or not is_sorted(root.left)):
        return False
    if root.right and (root.value > root.right.value or not is_sorted(root.right)):
        return False
    return True
```

# Is Sum Tree

Checks if a binary tree is a sum tree.

```python
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None

    def __iter__(self):
        if self.left:
            yield from self.left
        yield self.value
        if self.right:
            yield from self.right

def is_sum_tree(root: Node) -> bool:
    if not root.left and not root.right:
        return True
    left = sum(root.left) if root.left else 0
    right = sum(root.right) if root.right else 0
    return all((root.value == left+right, 
                is_sum_tree(root.left) if root.left else True, 
                is_sum_tree(root.right) if root.right else True))
```

# Merge Two Binary Trees

Combines two binary trees, if two node overlap the value is set to their sum otherwise it is set to the non null node.

```python
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
```

# Number Of Possible Binary Trees

Finds number of possible binary trees given a number of nodes. 

```python
def number_of_binary_trees(nodes: int) -> int:
    def factorial(n):
        out = 1
        for i in range(1, n+1):
            out *= i
        return out
    
    def catalan_number(n):
        out = 1
        for i in range(n):
            out *= 2*n-i
            out //= i+1
        return out // (n+1)
        

    return factorial(nodes) * catalan_number(nodes)
```

# Floyds Cycle Detection

Detects cycles in a list using a two pointer system (fast and slow pointer), if a linked list has a cycle then the fast pointer will loop back around and catch up to the slow pointer. 

```python
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Any, Self

@dataclass
class Node:
    data: Any
    next_node: Self | None = None

def detect_cycle(head: Node) -> bool:
    if not head
        return False

    slow = head
    fast = head
    while fast and fast.next_node:
        slow = slow.next_node if slow else None
        slow = slow.next_node.next_node
        if slow == fast:
            return True

    return False
```