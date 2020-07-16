"""Singly Linked List Implementation"""
class Node:
    """Node Class"""
    def __init__(self, val):
        self.val = val
        self.next = None


class SLinkedList:
    """Single Linked List Class"""
    def __init__(self):
        self.head = None

    def enqueue(self, val)-> bool:
        """Enqueue to end of linked list"""
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return True

        if not self.head.next:
            self.head.next = new_node
            return True

        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next

        curr_node.next = new_node

        return True

    def dequeue(self, val) -> bool:
        """dequeue from head of list implementation"""
        #empty list
        if not self.head:
            return False
        #removing head
        if self.head.val == val:
            self.head = self.head.next
            return True

        curr_node = self.head
        while curr_node.next is not None:
            if curr_node.next.val == val:
                curr_node.next = curr_node.next.next
                return True
            else:
                curr_node = curr_node.next

        #item was not found
        return False

    def search(self, val) -> object:
        """search for value in lined list"""
        #empty list
        if not self.head:
            return None

        if self.head.val == val:
            return self.head

        curr_node = self.head
        while curr_node.next is not None:
            if curr_node.val == val:
                return curr_node
            else:
                curr_node = curr_node.next

        #item was not found
        return None

    def print_list(self):
        """Print contents of linked list"""
        string_list = []
        #empty list
        if not self.head:
            print("Empty list!")
            return

        curr_node = self.head

        while curr_node is not None:
            string_list.append(str(curr_node.val))
            curr_node = curr_node.next

        print(' --> '.join(string_list))


def main():
    my_ll = SLinkedList()
    my_ll.enqueue(1)
    my_ll.enqueue(2)
    my_ll.enqueue(3)
    my_ll.enqueue(4)
    my_ll.enqueue(5)
    my_ll.print_list()
    my_ll.dequeue(1)
    my_ll.print_list()
    my_ll.enqueue(1)
    my_ll.print_list()
    my_ll.dequeue(4)
    my_ll.print_list()
    my_ll.dequeue(3)
    my_ll.dequeue(0)
    my_ll.dequeue(2)
    my_ll.print_list()
    my_ll.dequeue(1)
    my_ll.dequeue(5)
    my_ll.dequeue(1)
    my_ll.print_list()

if __name__ == '__main__':
    main()
