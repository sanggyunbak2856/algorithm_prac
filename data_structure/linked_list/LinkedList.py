class Node:
    def __init__ (self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__ (self, data):
        self.head = Node(data)
    def add (self, data): # 뒤에 삽입
        if self.head == None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)  
    def desc (self): # 데이터 출력
        node = self.head
        while node:
            print(node.data)
            node = node.next
    def find (self, data): # 데이터 찾기
        node = self.head
        while node:
            if node.data == data:
                print(node.data)
                return
            else:
                node = node.next
        print("not found")
    def delete (self, data): # 데이터 삭제
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                else:
                    node = node.next

linkedList = LinkedList(1)

for i in range(2, 11):
    linkedList.add(i)

linkedList.delete(10)
linkedList.desc()
linkedList.find(33)
