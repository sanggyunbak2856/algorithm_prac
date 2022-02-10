class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, head):
        self.head = head
    def insert(self, value):
        self.currentNode = self.head
        while true:
            if value < self.currentNode.value:
                if self.currentNode.left != None:
                    self.currentNode = self.currentNode.left
                else:
                    self.currentNode.left = Node(value)
                    break
            else:
                if self.currentNode.right != None:
                    self.currentNode = self.currentNode.right
                else:
                    self.currentNode.right = Node(value)
                    break
                    