class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def remove(self):
        self = self.next

class LinkedList:
    def __init__(self, head):
        self.head = head
        self.tail = head

    def append(self, val):
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def iterate(self):
        currentNode = self.head.next
        count = 0
        while currentNode:
            count += 1
            yield currentNode
            currentNode = currentNode.next

    def remove_all(self):
        currentNode = self.head.next
        self.head.next = None
        self.tail = self.head
        while currentNode:
            tmp = currentNode.next
            del currentNode
            currentNode = tmp

