import random

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
        while True:
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
    def search(self, value):
        self.currentNode = self.head
        while self.currentNode:
            if self.currentNode.value == value:
                return True
            elif self.currentNode.value > value:
                self.currentNode = self.currentNode.right
            else:
                self.currentNode = self.currentNode.left
        return False
    def delete(self, value):
        searched = False
        self.currentNode = self.head
        self.parentNode = self.head
        while self.currentNode:
            if self.currentNode.value == value:
                searched = True
                break
            elif value < self.currentNode.value:
                self.parentNode = self.currentNode
                self.currentNode = self.currentNode.left
            else:
                self.parentNode = self.currentNode
                self.currentNode = self.currentNode.right
        
        if searched == False:
            return False
        
        # leaf node
        if self.currentNode.left == None and self.currentNode.right == None:
            if self.parentNode.value > value:
                self.parentNode.left = None
            else:
                self.parentNode.right = None
            del self.currentNode
        
        # current node 의 자식 노드 1개
        if self.currentNode.left != None and self.currentNode.right == None:
            if self.parentNode.value > value:
                self.parentNode.left = self.currentNode.left
            else:
                self.parentNode.right = self.currentNode.right
        elif self.currentNode.left == None and self.currentNode.right != None:
            if self.parentNode.value > value:
                self.parentNode.left = self.currentNode.right
            else:
                self.parentNode.right = self.currentNode.right
        
        # current node 의 자식 노드 2개
        if self.currentNode.left != None and self.currentNode.right != None:
            if self.parentNode.value > value: # 왼쪽 자식
                self.changeNode = self.currentNode.right
                self.changeNodeParent = self.currentNode.right
                while self.changeNode.left != None: # 
                    self.changeNodeParent = self.changeNode
                    self.changeNode = self.changeNode.left
                if self.changeNode.right != None:
                    self.changeNodeParent.left = self.changeNode.right
                else:
                    self.changeNodeParent = None
                self.parentNode.left = self.changeNode
                self.changeNode.left = self.currentNode.left
                self.changeNode.right = self.currentNode.right
            else: # 오른쪽 자식
                self.changeNode = self.currentNode.right
                self.changeNodeParent = self.currentNode.right
                while self.currentNode.left != None:
                    self.changeNodeParent = self.changeNode
                    self.changeNode = self.changeNode.left
                if self.changeNode.right != None:
                    self.changeNodeParent.left = self.changeNode.right
                else:
                    self.changeNodeParent.left = None
                self.parentNode.right = self.changeNode
                self.changeNode.left = self.currentNode.left
                self.changeNode.right = self.currentNode.right