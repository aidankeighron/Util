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
