def evaluate(expressions: list[str]) -> float:
    stack = []

    operators = {
        "^": lambda a, b: a**b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
    }
    for expression in expressions:
        if expression not in operators:
            stack.append(float(expression))
            continue
        if expression in ["-","+"] and len(stack) < 2:
            x = stack.pop()
            if expression == "-":
                x *= -1
            stack.append(float(x))
            continue
        b = stack.pop()
        a = stack.pop()
        stack.append(operators[expression](a,b))
    return float(stack[0])

print(evaluate(["2", "-1.9", "+", "3", "*"]))