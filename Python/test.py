import operator as op

def solve_equation(equation: str) -> float:
    operators = {"*": op.mul, "/": op.truediv, "+": op.add, "-": op.sub}

    operand_stack = []
    operator_stack = []

    for ch in equation:
        if ch.isdigit():
            operand_stack.append(int(ch))
        elif ch in operators:
            operator_stack.append(ch)
        elif ch == ")":
            operator = operator_stack.pop()
            number_1 = operand_stack.pop()
            number_2 = operand_stack.pop()

            total = operators[operator](number_1, number_2)
            operand_stack.append(total)
            
    return operand_stack.pop()

print(solve_equation("(5 + ((4 * 2) * (2 + 3)))"))