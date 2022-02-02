class Node:
    def __init__(self, data, prev=None, next=None):
        self.data=data
        self.prev=prev
        self.next=next

class DoubleLinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            newNode = Node(data)
            node.next = newNode
            newNode.prev = node
            self.tail = newNode
    def descHead(self):
        if self.head == None:
            print("No data")
        else:
            node = self.head
            while node:
                print(node.data)
                node = node.next
    def descTail(self):
        if self.tail == None:
            print("No data")
        else:
            node = self.tail
            while node:
                print(node.data)
                node = node.prev
    def insertBefore(self, data): # 오름차순으로 정렬됨, 특
        if self.head == None:
            print("No data")
        else:
            if data < self.head.data: # data가 head의 데이터보다 작음
                prevHead = self.head
                newHead = Node(data)
                newHead.next = prevHead
                prevHead.prev = newHead
                self.head = newHead
            elif data > self.tail.data: # data가 tail의 데이터보다 큼
                prevTail = self.tail
                newTail = Node(data)
                prevTail.next = newTail
                newTail.prev = prevTail
                self.tail = newTail
            else:                       # 중간에 삽입
                node = self.head
                while node.next.data < data:
                    node = node.next   
                newNode = Node(data)
                prevNextNode = node.next
                node.next = newNode # next 연결
                newNode.next = prevNextNode
                prevNextNode.prev = newNode
                newNode.prev = node

doubleLinkedList = DoubleLinkedList(0)
for i in range(1, 10):
    doubleLinkedList.insert(i)

doubleLinkedList.insertBefore(15)
doubleLinkedList.descHead()
doubleLinkedList.descTail()