import sys
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BST:
    def __init__(self, value):
        self.head = Node(value)
    def insert(self, value):
        self.currentNode = self.head
        while True:
            if self.currentNode.value > value:
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
                self.currentNode = self.currentNode.left
            else:
                self.currentNode = self.currentNode.right
        return False

numberN = int(sys.stdin.readline())
numberNList = sys.stdin.readline()
numberNList = numberNList.split('\n')[0].split(' ')
bst = BST(numberNList[0])
for i in range(1, len(numberNList)):
    BST.insert(1)

numberM = int(sys.stdin.readline())
numberMList = sys.stdin.readline()
numberMList = numberMList.split('\n')[0].split(' ')

for j in numberMList:
    if BST.search(numberMList[j]):
        print(1)
    else:
        print(0)