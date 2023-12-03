#Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# Own words: Given an array that is sorted and has been rotated a certain number of times, find the lowest value in the array.

# Test cases
tests = []

tests.append({
    'input': {
        'nums':[3, 4, 5, 1, 2]
    },
    'output': 1
})

tests.append({
    'input': {
        'nums':[4, 5, 6, 7, 0, 1, 2]
    },
    'output': 0
})

tests.append({
    'input': {
        'nums':[11, 13, 15, 17]
    },
    'output': 11
})

tests.append({
    'input': {
        'nums':[-2, 1, 3, 7, -12, -4, -3]
    },
    'output': -12
})

tests.append({
    'input': {
        'nums':[3]
    },
    'output': 3
})

def findMin(nums):
    if len(nums) == 1: return nums[0]
    low, high = 0, len(nums) - 1
    