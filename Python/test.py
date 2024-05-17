def next_greatest_element(arr: list) -> list:
    stack = []
    result = [-1] * len(arr)
    for i in reversed(range(len(arr))):
        if stack:
            while stack[-1] <= arr[i]:
                stack.pop()
                if not stack:
                    break
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    return result

print(next_greatest_element([-10, -5, 0, 5, 5.1, 11, 13, 21, 3, 4, -21, -10, -5, -1, 0]))