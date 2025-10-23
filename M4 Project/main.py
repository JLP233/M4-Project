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

    print("\n Build a Backwards List ")
    ll2 = SinglyLinkedList()
    ll2.insert_at_end([50, 40, 30, 20, 10])
    print(ll2.display())

    ll2.delete_first()
    print("Delete the First Node:", ll2.display())

    ll2.delete_last()
    print("Delete the Last Node:", ll2.display())

    ll2.delete_value(30)
    print("Delete the Interior Node:", ll2.display())

    print("\n Non-Recursive Reverse Print Test")
    ll3 = SinglyLinkedList()
    ll3.insert_at_end([10, 20, 30, 40, 50])
    print("Insertion Order:", ll3.display())
    print("Reverse Order:", ll3.display_reverse_nr())

    print("\n Remove all test")
    ll4 = SinglyLinkedList()
    ll4.insert_at_end([1, 2, 4, 6, 1, 3, 6])
    print(ll4.display())
    ll4.remove_all(1)
    print("Removing 1 and All Duplicates:", ll4.display())
    ll4.remove_all(6)
    print("Removing 6 and All Duplicates:", ll4.display())

if __name__ == "__main__":
    run_tests()

    
