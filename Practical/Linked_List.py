# creating node 
class Node :
    def __init__ (self , data):
        self.data = data
        self.next = None
        
Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(30)
Node4 = Node(40)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
head = Node1

current = head
while current:
    print(current.data , end="->")
    current = current.next
print("None")
