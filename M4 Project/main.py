#M4 Projects Singly Linked List

from singly_linked_list import SinglyLinkedList

def run_tests():
    print("Build a Forward List")
    ll = SinglyLinkedList()
    ll.build_list_forward([10, 20, 30, 40, 50])
    print(ll.display())

    ll.delete_first()
    print("Delete the First Node:", ll.display())

    ll.delete_last()
    print("Delete the Last Node:", ll.display())

    ll.delete_value(30)
    print("Delete the Interior Node:", ll.display())

    
