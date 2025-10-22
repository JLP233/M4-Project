#Stack Class
from typing import Generic, TypeVar, List
T = TypeVar("T")

class Stack(Generic[T]):
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




