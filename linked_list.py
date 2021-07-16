"""
Linked List Implimentation
Using Self Referential Objects (nodes)
"""


class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data) -> None:
        self.data = data

    def __repr__(self) -> str:
        return f'<Node data: {self.data}>'


class LinkedList:
    """
    Singly linked list
    """
    head = None

    def __init__(self) -> None:
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        """
        Returns the number of nodes in the list
        Takes O(n) time
        __len__
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Adds a new Node containing data at the head of the list
        Takes O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        current = self.head

    def __repr__(self) -> str:
        """
        Return a string representation of the list
        Takes O(n) time, n being size of the the list of nodes
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f'[Head: {current.data}]')
            elif current.next_node is None:
                nodes.append(f'[Tail: {current.data}]')
            else:
                nodes.append(f'[{current.data}]')

            current = current.next_node

        return '-> '.join(nodes)
