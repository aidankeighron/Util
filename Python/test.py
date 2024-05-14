def infix_to_postfix(expression):
    stack = []
    postfix = []

    precedences = ["+","-","*","/","^"]

    for char in expression:
        if char.isalpha() or char.isdigit():
            postfix.append(char)
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                postfix.append(stack.pop())
            stack.pop()
        else:
            while True:
                if not stack:
                    stack.append(char)
                    break

                char_precedence = precedences.index(char)
                tos_precedence = precedences.index(stack[-1]) if stack[-1] in precedences else -1

                if char_precedence > tos_precedence:
                    stack.append(char)
                    break
                if char_precedence < tos_precedence:
                    postfix.append(stack.pop())
                    continue

                if char == "^":
                    stack.append(char)
                    break
                postfix.append(stack.pop())

    postfix.extend(stack)
    return ' '.join(postfix)

print(infix_to_postfix("3+2"))
print(infix_to_postfix("(3+4)*5-6"))
print(infix_to_postfix("a+b*c+(d*e+f)*g"))
print(infix_to_postfix("2^3^2"))