class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

def add(data):
    node=head
    print(id(node))
    while node.next:
        node=node.next
        print("n2",id(node))
    node.next=Node(data)

head=Node(1)
node=head
print(id(node))

for index in range(2,10):
    add(index)

while node.next:
    print(node.data)
    node=node.next
