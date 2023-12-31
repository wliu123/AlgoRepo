# You are given a list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of O(log N), where N is the length of the list. You can assume that all the numbers in the list are unique.

# Example: List [5, 6, 9, 0 , 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

# Own words: Given a list of numbers that was originally sorted and rotated a certain number of times, write  afunction to determine the minimum number of times its been rotated.

# Test Case
tests = []
tests.append({'input': {
        'nums':[14, 17, 20, 22, 0, 3, 5, 6, 9, 13]
    },
    'output':4
})
tests.append({'input': {
        'nums':[10, 11, 15, 17, 21, 1, 5, 6]
    },
    'output':5
})
tests.append({'input': {
        'nums':[2, 3, 10, 11]
    },
    'output':0
})
tests.append({'input': {
        'nums':[24, 3, 6, 7, 10]
    },
    'output':1
})
tests.append({'input': {
        'nums':[7, 23, 25, 28, 3]
    },
    'output':4
})
tests.append({'input': {
        'nums':[4, 5, 7, 10, 11, 13]
    },
    'output':0
})
tests.append({'input': {
        'nums':[]
    },
    'output':0
})
tests.append({'input': {
        'nums':[2]
    },
    'output':0
})

def count_rotations(nums):
    low, high = 0, len(nums)-1
    
    while low <= high:
        mid = (low+high)//2
        middle_num = nums[mid]
        if mid>0 and middle_num == min(nums):
            return mid
        elif mid>0 and middle_num < nums[high]:
            high = mid - 1
        else:
            low = mid + 1
    return 0

def evaluate_test_cases(function, tests):
    for test in tests:
        result = function(**test['input'])
        print(f"Input: {test['input']['nums']}")
        print(f"Expected Result: {test['output']}")
        print(f"Actual Result: {result}")
        print(result == test['output'])
evaluate_test_cases(count_rotations, tests)

tests.clear()

#Bonus Question

# Search in rotated sorted array:
# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

tests.append({'input': {
        'nums':[4,5,6,7,0,1,2],
        'target':0
    },
    'output':4
})
tests.append({'input': {
        'nums':[4,5,6,7,0,1,2],
        'target':-1
    },
    'output':-1
})
tests.append({'input': {
        'nums':[1],
        'target':0
    },
    'output':-1
})
tests.append({'input': {
        'nums':[1],
        'target':1
    },
    'output':0
})

def count_rotate_sort(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:
            if target > nums[mid] or target < nums[low]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if target < nums[mid] or target > nums[high]:
                low = mid - 1
            else:
                high = mid + 1
    return -1

evaluate_test_cases(count_rotate_sort, tests)