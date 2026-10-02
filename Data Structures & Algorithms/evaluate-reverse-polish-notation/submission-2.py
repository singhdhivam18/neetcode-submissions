import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul
        }

        for token in tokens:

            # If token is a number
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))

            # If token is an operator
            else:
                b = stack.pop()
                a = stack.pop()

                if token == '/':
                    result = int(a / b)
                else:
                    result = operations[token](a, b)

                stack.append(result)

        return stack[0]