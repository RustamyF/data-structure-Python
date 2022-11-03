nums=[4,5,6,7,0,1,2]
target=0
def find_minIndex(nums):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            return mid + 1
        if nums[mid] > nums[left]:
            left = mid + 1
        else:
            right = mid - 1
index = find_minIndex(nums)
# print(index)


def bst(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        print(left,right)
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        else:
            if target > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
print(nums[index:])
print(bst(nums[index:], 0))