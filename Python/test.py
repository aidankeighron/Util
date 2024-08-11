def climbing_stairs(num_steps: int) -> int:
    if num_steps == 1:
        return 1
    prev, cur = 1, 1
    for _ in range(num_steps-1):
        prev, cur = cur, cur + prev
    return cur

print(climbing_stairs(1))
print(climbing_stairs(2))
print(climbing_stairs(3))