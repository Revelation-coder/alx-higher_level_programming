#!/usr/bin/python3
'''this module defines class Node and class SinglyLinkedList'''


class Node:
    '''initialises node class'''
    def __init__(self, data, next_node=None):
        '''Initializes node'''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''function to return data'''
        return self._data

    @data.setter
    def data(self, value):
        '''setter function for node
         Args: value
        '''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        '''Function to get next node'''
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        '''function to set next node'''
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    '''class do define a singlylinkedlist'''
    def __init__(self):
        '''function to initialise list'''
        self.head = None

    def __repr__(self):
        '''function to initialize header'''
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        '''function to sort list'''
        new_node = Node(value)
        if self.head is None or value <= self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current_node = self.head
            while (current_node.next_node is not None and
                   current_node.next_node.data < value):
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node
