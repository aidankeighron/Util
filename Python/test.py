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
val = [60, 100, 120]
w = [10, 20, 30]
c = len(val)
print(knapsack(50, w, val, c))