class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def add(self, data):
        node = self
        while node.next:
            node = node.next
        node.next = Node(data)

    def print_Top(self):
        node = self
        while node.next:
            node = node.next
        return node.data

    def print_Node(self,index):
        node = self
        for i in range(index):
            node = node.next
        return node.next.data

    def delete_Node(self,index):
        node = self
        for i in range(index):
            node = node.next
        node.next = node.next.next

    def Count_Node(self):
        count=0
        node=self
        while  node.next:
            node=node.next
            count=count+1
        print(count)



head = Node("Head")
head.add(1)
head.add(3)
head.delete_Node(1)
print(head.next.data)

