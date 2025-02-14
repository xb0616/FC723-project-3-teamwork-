import math

class Calculator:
    def __init__(self):
        self.functions = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "sqrt": math.sqrt
        }

    def evaluate(self, expression):
        """Evaluates a mathematical expression including basic and scientific operations"""
        try:
            # Replace "^2" with "**2" for exponentiation
            expression = expression.replace("^", "**")


            # Replace math functions (sin, cos, tan, sqrt)
            expression = self.replace_functions(expression)

            # Tokenize the expression (split into numbers and operators)
            tokens = self.tokenize(expression)

            # Compute the result using a stack-based approach
            result = self.compute(tokens)

            return round(result, 6)  # Round to 6 decimal places

        except ZeroDivisionError:
            return "Error: Cannot divide by zero"
        except Exception:
            return "Error: Invalid expression"

    def replace_functions(self, expression):
        """Manually find and replace sin(x), cos(x), tan(x), sqrt(x) with computed values"""
        for func in self.functions:
            while func in expression:
                start = expression.find(func)  # Find function name
                open_bracket = expression.find("(", start)  # Find '('
                close_bracket = expression.find(")", open_bracket)  # Find ')'

                if open_bracket == -1 or close_bracket == -1:
                    return "Error: Invalid function syntax"

                # Extract number inside the parentheses
                num_str = expression[open_bracket + 1:close_bracket].strip()
                # strip() to cancel anything unnessary (like space)

                try:
                    num = float(num_str)  # Convert to float

                    # Compute result (convert to radians for sin, cos, tan)
                    if func in ["sin", "cos", "tan"]:
                        result = self.functions[func](math.radians(num))
                    else:
                        result = self.functions[func](num)

                    # Replace "func(x)" with computed result
                    expression = expression[:start] + str(result) + expression[close_bracket + 1:]

                except ValueError:
                    return "Error: Invalid function input"
                
        return expression


    def tokenize(self, expression):
        """Tokenizes the mathematical expression into numbers and operators"""
        tokens = []
        number = ""
        i = 0

        while i < len(expression):
            char = expression[i]

            if char.isdigit() or char == ".":
                number += char  # 继续构建数字
            else:
                if number:
                    tokens.append(number)
                    number = ""

                if char in "+-*/()":
                    # 处理 `**` (指数运算)
                    if char == "*" and i + 1 < len(expression) and expression[i + 1] == "*":
                        tokens.append("**")
                        i += 1  # 跳过下一个 `*`
                    else:
                            tokens.append(char)

            i += 1

        if number:
            tokens.append(number)

        return tokens


    def compute(self, tokens):
        """Computes the mathematical expression using a stack"""
        def apply_operator(operators, values):
            """Applies the operator to the top values in the stack"""
            op = operators.pop()
            right = values.pop()
            left = values.pop()

            if op == '+':
                values.append(left + right)
            elif op == '-':
                values.append(left - right)
            elif op == '*':
                values.append(left * right)
            elif op == '/':
                if right == 0:
                    raise ZeroDivisionError()
                    #raise will directly end the all function rather than apply_operator() function
                values.append(left / right)
            elif op == '**':
                values.append(left ** right)

        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 3}
        values, operators = [], []

        i = 0
        while i < len(tokens):
            token = tokens[i]

            if token.isnumeric() or '.' in token:
                values.append(float(token))  # Convert numbers to float
            elif token in precedence:
                while (operators and precedence.get(operators[-1], 0) >= precedence[token]):
                    apply_operator(operators, values)
                operators.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    apply_operator(operators, values)
                operators.pop()  # Remove '('
            i += 1

        while operators:
            apply_operator(operators, values)

        return values[0]

# Testing the Calculator
if __name__ == "__main__":
    calc = Calculator()
    print(calc.evaluate("2+3*4"))       # 14
    print(calc.evaluate("10/2"))        # 5.0
    print(calc.evaluate("sin(0)"))      # 0.0
    print(calc.evaluate("cos(0)"))      # 1.0
    print(calc.evaluate("tan(45)"))     # 1.619775
    print(calc.evaluate("sqrt(16)"))    # 4.0
    print(calc.evaluate("5^2"))         # 25
    print(calc.evaluate("(2+3)*4"))     # 20
