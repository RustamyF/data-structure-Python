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
#### 1. Accessing an element in Array
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
#### 2. Adding an element to Array 
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

#### 3. Deleting an element from Array 
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
#### 4. Searching an element in Array 
Speed of searching is one of the most important  operation that makes the programmers decide what data structure to use for the problem to be solved with.
Searching means to find an occurrence of a particular element in the Array and return its position. We might need to search an Array to find out whether or not 
an element is present in the Array. We might also want to search an Array that is arranged in a specific fashion to determine which index to insert a new element at.
1. Linear search: In this method we look every element of an array one by one until we find that element and return its index. The following code snippet will perform linear search 
and return the index of the element that is equal to the value we are searching and prints "this element does not exist" when there is not such element in the array.
```python
def search(value):
    for index, val in enumerate(array):
        if val==value:
            return index
    return "this element does not exist"
```

* Binary Search
This method reduces time complexity of search to log(n) when the elements in the array are sorted. This algorithm will not work if the array is not sorted.
Binary search divides the array into half and checks if the middle element is bigger than the target value or smaller. If it was bigger, it will take the ride side of the mid point and repeats this process untill
the values is found.
```python
array=[1,3,5,7,9,10]
def binary_search(value):
    # initiate left and right pointers
    left, right=0, len(array)-1
    while left<=right:
        # find the mid-point index
        mid=(left+right)//2
        # check if the mid-point index is equal to the target value
        if value==array[mid]:
            return mid
        # If target value is bigger than the mid-point element, change the left index to mid+1
        elif value>array[mid]:
            left=mid+1
        # Otherwise, bring the right pointer to the mid-1
        else:
            right=mid-1
    # if the element does not exist, print the following
    return "this element does not exist"
```
## Examples problems with Arrays
#### 1. Max Consecutive Ones
Given a binary array nums, return the maximum number of consecutive 1's in the array.
Test case 1
```
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
```
Test case 2
```
Input: nums = [1,0,1,1,0,1]
Output: 2
```
##### Solution [Code](code/max_conse_ones.py)
We can solve this problem by passing through every element in the array and keeping track of the
maximum number of consecutive ones. The following sinpit shows the python solution.
```python
class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        # initiate a current max and maximum of the maximum values
        curmax, maximum=0, 0
        for i in range(len(nums)):
            # when the element is 1, increase the current max by one
            if nums[i]==1:
                curmax+=1
            # When the element is not 1, make the current max 0
            else:
                curmax=0
            # keep track of the maximum of them
            maximum=max(maximum,curmax)
        return maximum

result=Solution()
array=[1,1,0,1,1,1]
print(result.findMaxConsecutiveOnes(array))
```
