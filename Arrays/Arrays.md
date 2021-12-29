# Arrays



## Introduction
Arrays are one of the simplest and basic data structure that exists in all programing languages
 which is used for storing similar items in the memory. Arrays can be one-dimensional or multi-dimensional.
 The elements in Arrays are stored in contiguous bytes of memory and allows for random access to the individual elements.
 Each element of an Array is indexed starting from 0 as shown bellow.
 
![App Screenshot](utils/Capture.JPG)

Since Array is a data structure, we should be comfortable to know how perform these operations in the Arrays:
- Accessing elements
- Insert
- Delete 
- Update
- Search
The main operations with arrays are adding elements to them and reading elements from them. Every other operation is built on top of these two methods.
#### Accessing an element in Array
to access and element in the array is quite simple. We just point to the index i of the array and the element will be returned to us.
For example, we have an array with [1, 'dog', 'cat', 5] and we want to to access
the element in index 0 and index 2, we use:

```python
>>> array=[1, 'dog', 'cat', 5]
>>> array[0]
1
>>> array[2]
'dog'
```
#### Adding an element to Array 
There are many ways of inserting an element to an Array:
1. Inserting a new element at the end of the Array.
1. Inserting a new element at the beginning of the Array.
1. Inserting a new element at any given index inside the Array \n

Adding an element at the end of an array is easy. We can use the **append()** method to add new elements at the end of  Array.
We can also just add the new element to the array as a list.
```python
>>> array.append(6)
>>> array
[1, 'dog', 'cat', 5, 6]

>>> array=array+['sky']
>>> array
[1, 'dog', 'cat', 5, 6, 'sky']
```
Adding an element at the start or anywhere in the array is more complicated because all other indexes needs to change as well.
This is one of the flaws of Array data structure that adding and deleting and element is not efficient. The following code sniped shows
the method of adding a new element at a specified index to an array.
```python
array=[1, 'dog', 'cat', 5, 6, 'sky']
def insert(index, value):
    # First, we will have to create space for a new element.
    array.append(0)
    # then shift all the elements to the right from the index location
    for i in range(index,len(array)-1,-1):
        array[i+1]=array[i]
    # Finally assign the value of index
    array[index]=value
insert(0,'hi')
print(array)
```
Python has a built-in function that does this for us using **array.insert(index,value)** method.
```python
>>> array=[1, 'dog', 'cat', 5, 6, 'sky']
>>> array.insert(0,'hi')
>>> array
['hi', 1, 'dog', 'cat', 5, 6, 'sky']
```

#### Deleting an element from Array 
Just like the insert method, deleting an element from an array requires changing the indexes of other elements unless it
is the last element of an array. Python has three built-in methods that can be used to delete an element 
from an array:
- **array.pop(index)**: This method removes the element with a specific index from an array and returns the removed element.
- **array.remove(value)**: This method removes the first matching element (which is passed as an argument) from the list. If there are multiple element of the
same value in an array, this method removes only the first one.
- **del array[index]**: This method deletes an element from an array without return anything.
```python
>>> array=[1, 'dog', 'cat', 5, 6, 'sky']
>>> array.pop(2)
'cat'
>>> array
[1, 'dog', 5, 6, 'sky']

>>> array.remove('sky')
>>> array
[1, 'dog', 5, 6]

>>> del array[0]
>>> array
['dog', 5, 6]
```
## Next Steps
Explanation and examples will be provided later.