#Infix to Postfix Converter
from stack import Stack

class InfixToPostfixConverter:
    PRECEDENCE = { "+": 1, "-": 1, "*": 2, "/": 2 }

    def convert(self, expr: str) -> str:
        out = []
        ops = Stack[str]()
        for tok in expr.split():
            if tok.isalnum():
                out.append(tok)
            elif tok in self.PRECEDENCE:
                while (not ops.is_empty() and ops.peek() in self.PRECEDENCE
                       and self.PRECEDENCE[ops.peek()] >= self.PRECEDENCE[tok]):
                    out.append(ops.pop())
                ops.push(tok)
            elif tok == "(":
                ops.push(tok)
            elif tok == ")":
                while not ops.is_empty() and ops.peek() != "(":
                    out.append(ops.pop())
                if ops.is_empty():
                    raise ValueError("Mismatched Parentheses")
                ops.pop()  # discard '('
            else:
                raise ValueError(f"Invalid Character Input: {tok}")
        while not ops.is_empty():
            top = ops.pop()
            if top in ("(", ")"):
                raise ValueError("Mismatched Parentheses")
            out.append(top)
        return " ".join(out)




