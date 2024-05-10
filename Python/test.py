def are_balanced_parentheses(parentheses: str) -> bool:
    stack = []
    bracket_pairs = {"(": ")", "[": "]", "{": "}"}
    for bracket in parentheses:
        if bracket in bracket_pairs.keys():
            stack.append(bracket)
        elif bracket in bracket_pairs.values() and (len(stack) == 0 or
            bracket_pairs[stack.pop()] != bracket):
            return False
    return len(stack) == 0

print(are_balanced_parentheses("[(])"))