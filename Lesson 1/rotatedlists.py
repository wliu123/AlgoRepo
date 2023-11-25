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
        'cards':[2, 3, 10, 11]
    },
    'output':0
})
tests.append({'input': {
        'cards':[24, 3, 6, 7, 10]
    },
    'output':1
})
tests.append({'input': {
        'cards':[7, 23, 25, 28, 3]
    },
    'output':4
})
tests.append({'input': {
        'cards':[4, 5, 7, 10, 11, 13]
    },
    'output':0
})
tests.append({'input': {
        'cards':[]
    },
    'output':-1
})
tests.append({'input': {
        'cards':[2]
    },
    'output':0
})

def count_rotations(nums):
    pass