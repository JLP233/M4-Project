from __future__ import annotations
from typing import Tuple
from singly_linked_list import SinglyLinkedList
from node import Node

class SplitEvensOdds(SinglyLinkedList):
    def split_even_odd(self) -> Tuple[SinglyLinkedList, SinglyLinkedList]:
        evens = SinglyLinkedList()
        odds = SinglyLinkedList()
        
        cur = self.head
        self.head = self.tail = None
        self.count = 0

        while cur:
            nxt = cur.next
            cur.next = None
            target = evens if (isinstance(cur.data, int) and cur.data % 2 == 0) else odds
            if target.tail is None:
                target.head = target.tail = cur
                target.count = 1
            else:
                target.tail.next = cur
                target.tail = cur
                target.count += 1
            cur = nxt

        return evens, odds




