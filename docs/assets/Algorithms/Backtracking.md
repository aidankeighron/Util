---
layout: script
language: Algorithms
---

# Combination Sum

Using backtracking we find all possible combinations of the collection that sum up to target.

```python
def combination_sum(collection: list, target: int) -> list:
    result = []
    current = []
    def backtrack(target, previous):
        if target == 0:
            result.append(current.copy())
            return
        for i in range(previous, len(collection)):
            if target >= collection[i]:
                current.append(collection[i])
                backtrack(target-collection[i], i)
                current.pop()
    backtrack(target, 0)
    return result
```

# All Subsequences

Finds all posable unique subsequence within `sequence` using backtracking.

```python
def all_subsequences(sequence: list) -> list:
    result = []
    def backtrack(current, index):

        if index == len(sequence):
            result.append(current.copy())
            return

        backtrack(current, index+1)
        current.append(sequence[index])
        backtrack(current, index+1)
        current.pop(0)

    backtrack([], 0)
    return result
```

# All Permutations

This loops through all possible combinations making sure to keep the length the same as the input. It keeps track of the indexes used so it does not repeat indexes and it gets every possible combination. 

```python
def all_permutations(sequence: list) -> list:
    result = []

    seen = [0 for _ in range(len(sequence))]
    def backtrack(i, current):
        if i == len(sequence):
            result.append(current.copy())
            return

        for j in range(len(sequence)):
            if not seen[j]:
                current.append(sequence[j])
                seen[j] = True
                backtrack(i+1, current)
                current.pop()
                seen[j] = False
    backtrack(0, [])

    return result
```

# Generate Parentheses

Generate `n` number of parentheses pairs.

```python
def generate_parentheses(n: int) -> list:
    result = []

    def backtrack(num_open, num_closed, current):
        if len(current) == 2 * n:
            result.append(current)
            return

        if num_open < n:
            backtrack(num_open + 1, num_closed, current + "(")
        
        if num_closed < num_open:
            backtrack(num_open, num_closed + 1, current + ")")

    backtrack(0, 0, "")
    return result
```

# Sum of Subsets

Using backtracking it tests all combinations of number to get to the target sum.

```python
def sum_of_subsets(numbers: list, target_sum: int) -> list:
    result = []

    def backtrack(i, path, remaining_sum):
        if sum(path) > target_sum or (remaining_sum + sum(path)) < target_sum:
            return
        if sum(path) == target_sum:
            result.append(path.copy())
            return
        for j in range(i, len(numbers)):
            backtrack(j+1, [*path, numbers[j]], remaining_sum - numbers[j])

    backtrack(0, [], sum(numbers))
    return result
```

# Power Sum

Finds the number of ways that `needed_sum` can be expressed as the sum of number to the nth `power`. Example: If `needed_sum = 13` and `power = 2` there is 1 way to get 13, `2^2 + 3^2 = 4 + 9 = 13`.

```python
def power_sum(needed_sum: int, power: int) -> int:
    result = 0

    def backtrack(current_sum, current_num):
        nonlocal result
        if current_sum == needed_sum:
            result += 1
            return

        next_num = current_num ** power
        if current_sum + next_num <= needed_sum:
            current_sum += next_num
            backtrack(current_sum, current_num+1)
            current_sum -= next_num
        if next_num < needed_sum:
            backtrack(current_sum, current_num+1)

    backtrack(0, 1)
    return result
```

# Match Word Pattern

Checks to see if the input string matches the provided the word pattern.

```python
def match_word_pattern(pattern: str, input_string: str) -> bool:
    pattern_map = {}
    string_map = {}
    
    def backtrack(pattern_index: int, string_index: int) -> bool:
        if pattern_index == len(pattern) and string_index == len(input_string):
            return True
        if pattern_index == len(pattern) or string_index == len(input_string):
            return False
        
        char = pattern[pattern_index]
        if char in pattern_map:
            mapped_str = pattern_map[char]
            if input_string.startswith(mapped_str, string_index):
                return backtrack(pattern_index + 1, string_index + len(mapped_str))
            else:
                return False
            
        for end in range(string_index + 1, len(input_string) + 1):
            sub_string = input_string[string_index:end]
            if sub_string in string_map:
                continue
            pattern_map[char] = sub_string
            string_map[sub_string] = char
            if backtrack(pattern_index + 1, end):
                return True
            del pattern_map[char]
            del string_map[sub_string]
        return False

    return backtrack(0, 0)
```