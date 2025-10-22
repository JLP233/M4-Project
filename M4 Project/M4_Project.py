#M4 Projects
#Stack Class
from typing import TypeVar, List
T = TypeVar("T")

class Stack:
    "Stack ADT (LIFO), Adapter Over Python List."
    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("Pop from Empty Stack")
        return self._items.pop()

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("Peek from Empty Stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

    def __len__(self) -> int:
        return self.size()




#Postfix Evaluator 
from stack import Stack
import operator

class PostfixEvaluator:
    OPS = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv }

    @staticmethod
    def _num(tok: str) -> float:
        try:
            return float(int(tok))
        except ValueError:
            return float(tok)

    def evaluate(self, expr: str) -> float:
        st = Stack[float]()
        if not expr.strip():
            raise ValueError("Empty Postfix Expression")
        for tok in expr.split():
            if tok in self.OPS:
                try:
                    b = st.pop()
                    a = st.pop()
                except IndexError:
                    raise ValueError("Improperly Formed Expression: Insufficient Operands")
                st.push(self.OPS[tok](a, b))
            else:
                st.push(self._num(tok))
        if st.size() != 1:
            raise ValueError("Improperly Formed Expression: Too Many Operands")
        return st.pop()


 
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




#Print Output
from postfix_evaluator import PostfixEvaluator
from infix_converter import InfixToPostfixConverter

print("Postfix Evaluator")
postfix = ["5 3 +","8 2 - 3 +","5 3 8 * +","6 2 / 3 +","5 8 + 3 -","5 3 + 8 *",
           "8 2 3 * + 6 -","5 3 8 * + 2 /","8 2 + 3 6 * -","5 3 + 8 2 / -"]
ev = PostfixEvaluator()
for s in postfix:
    print(f"[{s}] = {ev.evaluate(s)}")

print("\n Infix to Postfix Converter")
infix = ["A + B","A + B * C","( A + B ) * C","A * B + C / D","( A + B ) * ( C - D )",
         "A + B * C - D / E","A * ( B + C ) / D","( A + B * C ) / ( D - E )",
         "A +  ( B - C ) * D","( A + B * ( C - D ) ) / E"]
conv = InfixToPostfixConverter()
for s in infix:
    print(f"[{s}] -> [{conv.convert(s)}]")