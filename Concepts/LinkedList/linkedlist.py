class Node:
    def __init__(self, data:int):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0 

    
    def append(self, n:Node) -> None:
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n
        self.length += 1


    def prepend(self, n:Node) -> None:
        if self.head is None:
            self.head =  n
            self.tail =  n
        else:
            n.next = self.head
            self.head = n

    def print_list(self) -> None:
        to_print = self.head
        while to_print is not None:
            print(to_print.data, end=" ")
            to_print = to_print.next
        print()



    def delete_with_value(self, value:int) -> None:
        if self.head is None:
            print("No linked list found")
            return

        if self.head.data == value:
            self.head = self.head.next
            self.length -= 1
            return

        prev_to_delete = self.head

        while prev_to_delete.next is not None and prev_to_delete.next.data != value:
            prev_to_delete = prev_to_delete.next

        if prev_to_delete.next is None:
            print(f"No node found with data {value}")
            return

        prev_to_delete.next = prev_to_delete.next.next
        self.length -= 1


def main():
    list1 = LinkedList()

    node1 = Node(10)
    node2 = Node(11)
    node3 = Node(12)

    list1.prepend(node1)
    list1.prepend(node2)
    list1.prepend(node3)

    node4 = Node(13)
    node5 = Node(14)
    node6 = Node(15)

    list1.append(node4)
    list1.append(node5)
    list1.append(node6)

    list1.print_list()  # Expected: 12 11 10 13 14 15

    list1.delete_with_value(12)
    list1.print_list()  # Expected: 11 10 13 14 15

    list1.delete_with_value(120)
    list1.print_list()  # Expected: 11 10 13 14 15


if __name__ == "__main__":
    main()        