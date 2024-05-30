---
layout: script
language: Algorithms
---

## Closest Pair of Points

Finds the distance between the closest pair of points

```python
def closest_pair(points: list) -> float:
    points_sorted_x = sorted(points, key=lambda x: x[0])
    points_sorted_y = sorted(points, key=lambda x: x[1])

    def euclidean_distance_sqr(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    
    def distance_between_closest_pair(points_, min_distance):
        for i in range(len(points_)-1):
            for j in range(i+1, len(points_)):
                current_distance = euclidean_distance_sqr(points_[i], points_[j])
                if current_distance < min_distance:
                    min_distance = current_distance
        return min_distance

    def distance_between_closest_in_strip(points_, min_distance):
        for i in range(min(6, len(points_)-1), len(points_)):
            for j in range(max(0, i-6), i):
                current_distance = euclidean_distance_sqr(points_[i], points_[j])
                if current_distance < min_distance:
                    min_distance = current_distance
        return min_distance
    
    def closest_pair_of_points(points_x, points_y, point_counts):
        if point_counts <= 3:
            return distance_between_closest_pair(points_sorted_x, float("inf"))

        mid = point_counts // 2
        closest_in_left = closest_pair_of_points(points_x, points_y[:mid], mid)
        closest_in_right = closest_pair_of_points(points_y, points_y[mid:], point_counts-mid)
        closest_pair_distance = min(closest_in_left, closest_in_right)

        cross_strip = []
        for point in points_x:
            if abs(point[0] - points_x[mid][0]) < closest_pair_distance:
                cross_strip.append(point)

        closest_in_strip = distance_between_closest_in_strip(cross_strip, closest_pair_distance)
        
        return min(closest_pair_distance, closest_in_strip)

    return closest_pair_of_points(points_sorted_x, points_sorted_y, len(points)) ** 0.5
```

## Heaps Algorithm

Finds all permutations of an input list

```python
def heaps(arr: list) -> list:
    res = []

    def generate(k, subset):
        if k == 1:
            res.append(subset[:])
            return

        generate(k-1, subset)

        for i in range(k-1):
            if k % 2 == 0:
                subset[i], subset[k-1] = subset[k-1], subset[i]
            else:
                subset[0], subset[k-1] = subset[k-1], subset[0]
            generate(k-1, subset)
    
    generate(len(arr), arr)
    return res
```

## Inversions

Count the number of inversions in an array.

```python
def count_inversions(arr: list) -> int:

    def cross_inversions(p, q):
        r = []
        i = j = num_inversion = 0
        while i < len(p) and j < len(q):
            if p[i] > q[j]:
                num_inversion += len(p) - i
                r.append(q[j])
                j += 1
            else:
                r.append(p[i])
                i += 1
        if i < len(p):
            r.extend(p[i:])
        else:
            r.extend(q[j:])
        
        return r, num_inversion

    def inversions(subset):
        if len(subset) <= 1:
            return subset, 0
        mid = len(subset) // 2

        a, inversion_p = inversions(subset[0:mid])
        b, inversion_q = inversions(subset[mid:])
        c, cross_inversion = cross_inversions(a, b)
        
        return c, inversion_p + inversion_q + cross_inversion

    return inversions(arr)[1]
```

## Kth Order Statistic

Finds the kth smallest number in a list

```python
from random import choice

def kth_number(arr: list, k: int) -> int:
    pivot = choice(arr)

    smaller = [i for i in arr if i < pivot]
    bigger = [i for i in arr if i > pivot]

    if len(smaller) == k -1:
        return pivot
    elif len(smaller) < k - 1:
        return kth_number(bigger, k - len(smaller) - 1)
    else:
        return kth_number(smaller, k)
```