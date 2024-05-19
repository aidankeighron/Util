def calculate_span(prices: list, span: list) -> list:
    stack = [0]
    span[0] = 1
    for price in range(1, len(prices)):
        while stack and prices[stack[0]] <= prices[price]:
            stack.pop()
        
        span[price] = price + (-stack[0] if stack else 1)

        stack.append(price)

    return span

print(evaluate(["2", "-1.9", "+", "3", "*"]))