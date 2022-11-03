array=[1, 'dog', 'cat', 5, 6, 'sky']
def insert(index, value):
    # First, we will have to create space for a new element.
    array.append(0)
    # then shift all the elements to the right from the index location
    for i in range(index,len(array)-1,-1):
        array[i+1]=array[i]
    # Finally assign the value of index
    array[index]=value
# insert(0,'hi')
# print(array)



def search(value):
    for index, val in enumerate(array):
        if val==value:
            return index
    return "this element does not exist"

# print(search('skd'))
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
# print(binary_search(3))

class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        curmax, maximum=0, 0
        for i in range(len(nums)):
            if nums[i]==1:
                curmax+=1
            else:
                curmax=0
            maximum=max(maximum,curmax)
        return maximum
result=Solution()
array=[1,1,0,1,1,1]
print(result.findMaxConsecutiveOnes(array))