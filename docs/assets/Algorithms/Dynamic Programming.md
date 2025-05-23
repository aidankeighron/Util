---
layout: script
language: Algorithms
---

## Fibonacci Numbers

Calculates the first `n` fibonacci numbers.

```python
def fibonacci(n: int) -> list:

    if n == 0:
        return [0]
    fib = [0, 1]
    for _ in range(n-1):
        fib.append(fib[-1]+fib[-2])
    return fib
```

## Longest Common Substring

Finds the longest common substring between two strings.

```python
def longest_common_substring(string1: str, string2: str) -> str:
    string1_len = len(string1)
    string2_len = len(string2)

    dp = [[0] * (string2_len+1) for _ in range(string1_len+1)]
    ans_index = 0
    ans_length = 0

    for i in range(1, string1_len+1):
        for j in range(1, string2_len+1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                if dp[i][j] > ans_length:
                    ans_index = i
                    ans_length = dp[i][j]
    
    return string1[ans_index - ans_length:ans_index]
```

Explanation:

Using the 2d array `dp` the program keeps track of the number of same characters in a row:

```python
longest_common_substring("abc", "abc")

dp = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 2, 0],
    [0, 0, 0, 3]
]

output = "abc"
```

## Knapsack

Finds the max value that can be put into the knapsack taking into account the capacity and weights of the objects. I uses recursion to find if an object can be put in the knapsack optimally or if it needs to be omitted.

```python
def knapsack(capacity: int, weights: list, values: list, counter: int) -> int:

    if capacity == 0 or counter == 0:
        return 0

    if weights[counter - 1] > capacity:
        return knapsack(capacity, weights, values, counter - 1)
    else:
        left_capacity = capacity - weights[counter - 1]
        new_value = values[counter - 1] + knapsack(left_capacity, weights, values, counter - 1)
        without_value = knapsack(capacity, weights, values, counter - 1)
        return max(new_value, without_value)
```

## Minimum Cost Path

Find the lowest "cost" from top left of a matrix to the bottom right. This works by choosing to either move down or right depending on the lowest cost.

```python
def minimum_cost_path(matrix: list[list]) -> int:
    ## first row
    for i in range(1, len(matrix[0])):
        matrix[i][i] += matrix[0][i-1]

    ## first column
    for i in range(1, len(matrix)):
        matrix[i][0] += matrix[i - 1][0]

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])

    return matrix[-1][-1]
```

## Longest Palindrome Sequence

Finds the longest palindrome sequence in a string. Using a dp matrix to keep track of matching characters.

```python
def longest_palindrome_sequence(string: str) -> int:
    n = len(string)
    reverse = string[::-1]
    dp = [[-1] * (n+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
        dp[0][i] = 0

    for i in range(1, n+1):
        for j in range(1, n+1):
            if string[i-1] == reverse[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][n]
```

## Abbreviation

Check if a string is a valid abbreviation

```python
def abbreviation(string: str, abbreviation: str) -> bool:
    dp = [[False for _ in range(len(abbreviation)+1)] for _ in range(len(string)+1)]
    dp[0][0] = True

    for i in range(len(string)):
        for j in range(len(abbreviation)+1):
            if dp[i][j]:
                if j < len(abbreviation) and string[i].upper() == abbreviation[j]:
                    dp[i+1][j+1] = True
                if string[i].islower():
                    dp[i+1][j] = True
    
    return dp[len(string)][len(abbreviation)]
```

## All Construct

Return a list of all ways to make the target word using the word bank.

```python
def all_construct(target: str, bank: list) -> list:
    table = [[] for _ in range(len(target)+1)]

    table[0] = [[]]

    for i in range(len(target)+1):
        if table[i] != []:
            for word in bank:
                if target[i:i+len(word)] == word:
                    new_combinations = [[word, *way] for way in table[i]]

                    table[i+len(word)] += new_combinations

    for combination in table[len(target)]:
        combination.reverse()

    return table[len(target)]
```

## Catalan Numbers

Calculates all Catalan Numbers from 0 to n

```python
def catalan_numbers(n: int) -> list:
    catalan = [0] * (n+1)
    catalan[0] = 1
    
    if n > 0:
        catalan[1] = 1

    for i in range(2, n+1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i-j-1]

    return catalan 
```

## Climbing Stairs

Number of ways to climb n stairs when you can more 1 or 2 stairs at a time

```python
def climbing_stairs(num_steps: int) -> int:
    if num_steps == 1:
        return 1
    prev, cur = 1, 1
    for _ in range(num_steps-1):
        prev, cur = cur, cur + prev
    return cur
```

## Combination Sum IV

Find the number of ways you can make the target number using the elements of an array.

```python
def combination__sum_iv(target: int, array: list) -> int:
    def recursion(target, dp):
        if target < 0:
            return 0
        if target == 0:
            return 1
        if dp[target] != -1:
            return dp[target]
        answer = sum(recursion(target - item, dp) for item in array)
        dp[target] = answer
        return answer

    dp = [-1] * (target+1)
    return recursion(target, dp)
```

## Edit Distance

Find how many edits needed to make two strings equal each other

```python
def edit_distance(source: str, target: str) -> int:
    if not len(source):
        return len(target)
    elif not len(target):
        return len(source)

    delta = int(source[-1] != target [-1])

    return min(edit_distance(source[:-1], target[:-1])+delta, edit_distance(source, target[:-1])+1, edit_distance(source[:-1], target)+1)
```

## Factorial

Calculates the factorial of a number

```python
def factorial(n: int) -> int:
    value = 1
    for i in range(1, n+1):
        value *= i
    return value
```

## Iterating Through Submasks

List all numbers that can be made with the bits of the initial number

```python
def iterating_through_submasks(mask: int) -> list:
    all_submasks = []
    submask = mask
    while submask:
        all_submasks.append(submask)
        submask = (submask - 1) & mask

    return all_submasks
```

## Largest Divisible Subset

Algorithm to find the biggest subset in the array so any a and d divide into each other

```python
def largest_divisible_subset(array: list) -> list:
    array.sort()

    memo = [1] * len(array)
    hash_array = list(range(len(array)))

    for i, item in enumerate(array):
        for prev in range(i):
            if array[prev] != 0 and item % array[prev] == 0 and 1 + memo[prev] > memo[i]:
                memo[i] = 1 + memo[prev]
                hash_array[i] = prev

    largest = -1
    largest_index = -1

    for i, item in enumerate(memo):
        if item > largest:
            largest = item
            largest_index = i
    
    if largest_index == -1:
        return []
    result = [array[largest_index]]
    while hash_array[largest_index] != largest_index:
        largest_index = hash_array[largest_index]
        result.append(array[largest_index])

    return result
```

## Longest Common Subsequence

Finds the longest common subsequence between two strings

```python
def longest_common_subsequence(x: str, y: str) -> str:
    m = len(x)
    n = len(y)

    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            match = 1 if x[i-1] == y[j-1] else 0

            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+match)

    seq = ""
    i, j = m, n
    while i > 0 and j > 0:
        match = 1 if x[i-1] == y[j-1] else 0

        if dp[i][j] == dp[i-1][j-1] + match:
            if match:
                seq = x[i-1] + seq
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            j -= 1

    return seq
```

## Longest Common Substring

Finds the longest common substring between two strings

```python
def longest_common_substring(a: str, b: str) -> str:
    n = len(a)
    m = len(b)
    
    dp = [[0]*(m+1) for _ in range(n+1)]
    ans_index = 0 
    ans_len = 0

    for i in range(1, n+1): 
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                if dp[i][j] > ans_len:
                    ans_index = i
                    ans_len = dp[i][j]
    
    return a[ans_index-ans_len:ans_index]
```

## Longest Increasing Subsequence

Finds the longest increasing subsequence in a list

```python
def longest_increasing_subsequence(array: list) -> list:
    n = len(array)

    if n <= 1:
        return array
    
    pivot = array[0]
    is_found = False
    i = 1
    longest_subseq = []
    while not is_found and i < n:
        if array[i] < pivot:
            is_found = True
            a += len(array[i:])
            temp_array = [element for element in array[i:] if element >= array[i]]
            temp_array = longest_increasing_subsequence(temp_array)
            if len(temp_array) > len(longest_subseq):
                longest_subseq = temp_array
        else:
            i += 1

    temp_array = [element for element in array[1:] if element >= pivot]
    temp_array = [pivot, *longest_increasing_subsequence(temp_array)]
    if len(temp_array) > len(longest_subseq):
        return temp_array
    else:
        return longest_subseq
```

## Longest Palindromic Subsequence

Find the longest palindrome sequence in a string

```python
def longest_palindromic_subsequence(string: str) -> int:
    n = len(string)
    rev = string[::-1]
    dp = [[-1]*(n+1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 0
        dp[0][i] = 0

    for i in range(1, n+1):
        for j in range(1, n+1):
            if string[i-1] == rev[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[n][n]
```

## Max Non Adjacent Sum

Find the maximum non-adjacent sum of numbers in the input list

```python
def maximum_non_adjacent_sum(nums: list) -> int:
    max_including = nums[0]
    max_excluding = 0

    for num in nums[1:]:
        max_including, max_excluding = max_excluding + num, max(max_including, max_excluding)

    return max(max_excluding, max_including) 
```

## Max Product Subarray

Finds the maximum product subarray

```python
def max_product_subarray(nums: list) -> int:
    
    current_max = current_min = res = nums[0]
    for i in range(1, len(nums)):
        n = nums[i]

        if n  < 0:
            current_max, current_min = current_min, current_max
        current_max = max(n, current_max * n)
        current_min = min(n, current_min * n)

        res = max(res, current_max)
    return res
```

## Max Subarray Sum

Subarray with the largest sum

```python
def max_subarray_sum(nums: list) -> int:
    max_sum = 0
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum
```

## Min Distance Up Bottom

Using a bottom up approach find the minimum edit distance between two words to get them to match.

```python
import functools

def min_edit_distance(word1: str, word2: str) -> int:
    @functools.cache
    def min_distance(index1, index2):
        if index1 >= len(word1):
            return len(word2) - index2
        if index2 >= len(word2):
            return len(word1) - index1
        diff = int(word1[index1] != word2[index2])
        return min(1+min_distance(index1+1, index2), 1+min_distance(index1, index2+1), diff+min_distance(index1+1, index2+1))

    return min_distance(0, 0)
```