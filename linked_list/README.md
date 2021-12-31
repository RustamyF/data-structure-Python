# Linked List

## Introduction
Linked list is another powerful data structure that can be used to store a collection in a linear order. It allows
for smaller memory allocation without requiring the element shifts for insertion and deletion operations. It still requires
linear time complixity to search an item just like arrays. There are multiple types of linked-lists:
* Singly linked-list
* Doubly linked-list
* circular singly and doubly linked-list

we will first explain the concept of linked-list using a singly linked-list structure which is the easiest to understand.
Suppose we have a basic calss containing a single value a next point to None:

```python
class ListNode :
    def __init__( self, data ) :
        self.data = data
        sef.next = None
```

This is a single node and we can create several instances of this node and each containing an integer value.
```python
a = ListNode( 11 )
b = ListNode( 52 )
c = ListNode( 18 )
```
This is how the nodes will look like. 

![App Screenshot](utils/LL_three_nodes.JPG)

Finally, we can point each node to each other where a points to b and b points to c.
```python
a.next = b
b.next = c
```
![App Screenshot](utils/linked_three_nodes.JPG)
once all nodes are connected, we do not need to have b and c references. All we need is the value at the begining of the list
which in this case is a. We can find the values in the other nodes as:

```python
print( a.data )
print( a.next.data )
print( a.next.next.data )
```

The first node in the linked-list, must be named
or referenced by an external variable as it provides an entry point into the linked
list. This variable is commonly known as the head pointer, or head reference. A
linked list can also be empty, which is indicated when the head reference is null.
![App Screenshot](utils/LL_head.JPG)

Since Array is a data structure, we should be comfortable to know how perform these operations in the linkedList:
- Printing the list
- Insert
- Search
- get
- Delete 
- Update


#### 1. Printing the list


```python
def print_list(self):
    # start from the head of linked-list
    temp=self.head
    # loop over each element until the temp.next is None
    while temp is not None:
        # at each node, print the data
        print(temp.data)
        # got to the next node
        temp=temp.next
```
#### 2. - Insert

```python
def insert_tail(self,data):
    # initiate the new node using the new data
    new_node = ListNode(data)
    # if there is not head, create the head node
    if self.head is None:
        self.head=new_node
        self.tail=new_node
    # if it is not the head node, point the tail to the new node and change tail
    else:
        self.tail.next=new_node
        self.tail=new_node
def insert_head(self,data):
    # initiate the new node using the new data
    new_node=ListNode(data)
    # if there is no head, create the head node
    if self.head is None:
        self.head=new_node
        self.tail=new_node
    # if it is not the head node, point the new node to head and change the head to new node
    else:
        new_node.next=self.head
        self.head=new_node
```

#### 3. Search


![App Screenshot](utils/search.JPG
```python
def search(self, data):
    # start from the head of linked-list
    temp=self.head
    # loop until the end of linked-list
    while temp is not None:
        # if the node values is equal to data, return True
        if temp.data==data:
            return True
        # go to the next node
        temp=temp.next
    # if the values is not there, return False
    return False
```
#### 4. get
```python
def get(self, index):
    # check if head is None or index is below zero
    if self.head is None and index<0:
        return False
    # start from the head of linked-list
    temp=self.head
    # loop over each element until the index
    for _ in range(index):
        # check if the index is more than the length of linked_list
        if temp is None:
            return False
        temp=temp.next
    # return the node value
    return temp
    
```
#### 5. Delete

![App Screenshot](utils/search.JPG)
```python
def delete(self, index):
    # check if head is None or index is below zero
    if self.head is None and index<0:
        return False
    # check if it is the head node
    if index==0:
        self.head=self.head.next
    # get the node before using the get() method
    temp=self.get(index-1)
    # check to see if it is a tail node
    if temp.next==self.tail:
        temp.next=None
        self.tail=temp
    else:
        temp.next=temp.next.next
        
```
#### 6. Update

```python
def update(self, index, data):
    # get the element using its index and get() method
    temp=self.get(index)
    # change its data
    temp.data=data
    
```
## Examples problems with linked-list


#### 1. Design a linked-list data structure

##### Solution [Code](code/linked_list.py)


#### 2. 

##### Solution [Code](code/find_number_of_evens.py)

#### 3.

##### Solution [Code](code/duplicate_zeros.py)

#### 4.

##### Solution [Code](code/merge_sorted_array.py)


#### 5. 

##### Solution [Code](code/valid_mountain.py)

## Next Steps

This file will continuously be updated.

