from __future__ import annotations
from typing import Any, Iterable, Optional, List
from node import Node

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.count: int = 0

    def is_empty(self) -> bool:
        return self.head is None

    def build_list_forward(self, items: Iterable[Any]) -> None:
        for x in items:
            n = Node(x, self.head)
            self.head = n
            if self.tail is None:
                self.tail = n
            self.count += 1

    def insert_at_end(self, items: Iterable[Any]) -> None:
        for x in items:
            n = Node(x)
            if self.tail is None:
                self.head = self.tail = n
            else:
                self.tail.next = n
                self.tail = n
            self.count += 1

    def delete_first(self):
        if self.head is None:
            raise IndexError("Delete First on Empty List")
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.count -= 1
        return data

    def delete_last(self):
        if self.head is None:
            raise IndexError("Delete Last on Empty List")
        if self.head is self.tail:
            data = self.head.data
            self.head = self.tail = None
            self.count = 0
            return data
        prev = self.head
        while prev.next is not self.tail:
            prev = prev.next 
        data = self.tail.data  
        prev.next = None
        self.tail = prev
        self.count -= 1
        return data

    def delete_value(self, value: Any) -> bool:
        if self.head is None:
            return False
        if self.head.data == value:
            self.delete_first()
            return True
        prev = self.head
        cur = self.head.next
        while cur:
            if cur.data == value:
                prev.next = cur.next
                if cur is self.tail:
                    self.tail = prev
                self.count -= 1
                return True
            prev, cur = cur, cur.next
        return False

    def remove_all(self, value: Any) -> int:
        removed = 0
        while self.head and self.head.data == value:
            self.delete_first()
            removed += 1
        prev = self.head
        cur = self.head.next if self.head else None
        while cur:
            if cur.data == value:
                prev.next = cur.next
                if cur is self.tail:
                    self.tail = prev
                self.count -= 1
                removed += 1
                cur = prev.next
            else:
                prev, cur = cur, cur.next
        return removed

    def display(self) -> str:
        parts: List[str] = ["Head"]
        cur = self.head
        while cur:
            parts.append(str(cur.data))
            cur = cur.next
        parts.append("None")
        return " -> ".join(parts)

    def display_reverse_nr(self) -> str:
        stk: List[Any] = []
        cur = self.head
        while cur:
            stk.append(cur.data)
            cur = cur.next
        left = "None"
        while stk:
            left = f"{left} <- {stk.pop()}"
        return f"{left} <- Head"





