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
