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

print(generate_parentheses(2))