# Linked Lists

[Back to Welcome page](/welcome.md)

You likely have previously used lists in python or other languages, so that knowledge will be very useful in understanding linked lists. If you haven't I would suggest this guide [Lists and arrays in python](https://www.w3schools.com/python/python_lists.asp)

Queues, stacks, sets and map all base their storage using "contiguous" memory. This means that each item in them is set immediately after the previous item. You can think of this as a 1 by 1 increasing method. 

Linked lists on the other hand store data at random within the list. Each element has a particular and specific position within the array without specific order. 

These elements, known as "nodes" have the value of the element and are linked to the next node in the list. The links to the next node are referred to as "pointers". Each list has both a head and a tail, meaning that the node in first position is it's head, and the node last in position is the tail. 

Single Linked lists contain this structure and are only connected one way from node to node. Each node only having one pointer forward to the next node. 

![Linked Lists Image](/pictures/linkedlists2.jpeg)

Double Linked Lists on the other hand are connected by two pointers on each node. One pointing forward to the next node, the other pointing backwards to the previous node. 

Using a single or double linked list, it has the same complexity for their operation. Accessing, or getting a particular value from a linked list requires O(n) complexity to find the node. This is because you need to find the particular value within the list. This means the insert() operation when not at the head or tail and the remove() operation when not at the head or tail both are O(n) complexity. 

However, when inserting at the head or tail, or deleting from the head or tail is only O(1) time. Obtaining the size of the link as well as checking if the list contains values also is O(1) complexity. 

## Purposes and usage

One of the most applicable examples of a linked list data structure is a Music player. 

Each song in the list has both a previous and a next song, and you can start listening anywhere in the list. If it is a playlist structure you can insert and remove songs from your playlist as well. 

## Examples

```
# initializing a linked list as a class

class exampleLinkList:
    """
        after creating the core structure we need to define the structure of a linked list. Lets start with a Node. 
    """
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None
    def __init__(self):
        #start an empty list
        self.head = None
        self.tail = None
    
```

After initializing the list you can then move on to using specific operations to insert into the list at the head, tail, or middle. 

```
# inserts node at front of the Linked-List
def insert_head(self, value):

    new_node = exampleLinkList.Node(value)

    if self.head is None:
        self.head = new_node
        self.tail = new_node

    else:
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

# you can also use this method to insert a node at the tail of the linked-list
def insert_tail(self, value):
    new_node = exampleLinkList.Node(value)

    if self.tail is None:
        self.head = new_node
        self.tail = new_node
    
    else:
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

```

The last example we will show for this tutorial is how to remove a node that contains a specific value. This is because this it is a more complex operation done in a linked list. 

```
def replace(self, old_value, new_value):

    current = self.head
    while current is not None:
        if current.data == old_value:
            current.data == new_value
            current = current.next

            if current.data == old_value:
            current.data = new_value

            return
            current == current.next

```

## Problem: 

Implement the insert_head() function so that the following code runs and can be output. 


```
example.insert_head(1)
example.insert_head(2)
example.insert_head(3)
example.insert_head(4)
```
output should appear as:

linkedlist[1, 2, 3, 4]

[Problem File](/py%20files/linkedlistproblem.py)

If you are struggling to complete the problem then proceed to use the solution file

[Solution File](/py%20files/linkedListSolution.py)



## Operations used with linked lists

insertAtHead(value): Inserts new node at the head of the linked list. Performance O(1)
```
exampleLinkList.appendleft(value);
```
insertAtTail(value) Inserts new node at the tail of the linked list. Performance O(1)
```
exampleLinkList.append(value);
```
insert(i,value): Inserts value after i, Performance O(n) depending on how large your linked list is. 
```
exampleLinkList.insert(i,value);
```
deleteHead(): Deletes the head from the linked list. Performance of O(1)
```
exampleLinkList.popleft();
```
deleteTail(): Deletes the tail from the linked list. Performance of O(1)
```
exampleLinkList.pop();
```
delete(i): Deletes specific index at value "i". This performance is more complex as it takes O(n) time to look through linked list one item at a time.
```
del exampleLinkList[i]
```
size()/ Length: Used to find length of the linked list. Performance is in O(n) time. 
```
len(exampleLinkList);
```

## References

[Lists and arrays in python](https://www.w3schools.com/python/python_lists.asp)

[Images found](https://kodr.me/en/linked-list-intro)

[Codebasic's tutorial on Youtube it is Excellent](https://youtu.be/qp8u-frRAnU)


## [Back to Welcome page](/welcome.md)
