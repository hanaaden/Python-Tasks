# Linked List 
linked is type of linear data structure similar to arrays so what is 
linear data structure is type of DS that elements are  collected and arranged as squeence one after another

- you can transvere elements one by one 

so linked list is collection of nodes linked to each other and node is basic  unit of storage think like a box that holds 2 things 
- data : the actual information like datatypes 
- refences / pointer : a way to connect this node to another node 
nodes are not just a value its value plus connection 

linked list is good implementing a linear data structure 
so they dont need to have fixed size due to 
their like chain structure 
some cons are operations on linked list is 
slow 
so let we create a node class 
```py
# creating node 
class Node :
    def __init__ (self , data):
        self.data = data
        self.next = None
        
Node1 = Node(10)
print(Node1.data)
 
```

__init__ is a special method in Python called a constructor.

It runs automatically whenever a new object of the class is created.

data is a parameter that allows us to store any value in the node (like a number, string, or object).

self.data creates an instance variable called data.

Each node has its own data that remembers the value passed.

self.next is the pointer/reference to the next node in the list.

Initially, we set it to None because when the node is created, it’s not connected to anything yet.

## Insertion of linked list

so when we need to add a new node any where in the list
so we need insertion of linked list 

to insert a new node at the front we create 
the new node and piont to his next reference to 
current head 
then we update the head to be this new node 

