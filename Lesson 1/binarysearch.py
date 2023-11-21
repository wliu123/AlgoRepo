# QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.

# We need to write a program where we find the position of a target in a given list of numbers arranged in decreasing order while also minimizing the number of times we access elements of the list.

# Test Case
cards = [13, 5, 9, 2, 3, 1, 0, 10]
target = 2
output = 3
tests = []
tests.append({'input': {
        'cards':[13, 10, 9, 5, 3, 2, 1, 0],
        'target':2
    },
    'output':5
})
tests.append({'input': {
        'cards':[4, 2, 1, -1],
        'target':4
    },
    'output':0
})
tests.append({'input': {
        'cards':[3, -1, -9, -127],
        'target':-127
    },
    'output':3
})
tests.append({'input': {
        'cards':[10],
        'target':10
    },
    'output':0
})
tests.append({'input': {
        'cards':[9, 7, 5, 2, -9],
        'target':4
    },
    'output':-1
})
tests.append({'input': {
        'cards':[],
        'target':5
    },
    'output':-1
})
tests.append({'input': {
        'cards':[8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'target':3
    },
    'output':7
})
tests.append({'input': {
        'cards':[8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'target':6
    },
    'output':2
})
def test_location(cards, target, mid):
    mid_number = cards[mid]
    if mid_number == target:
        if mid-1 >= 0 and cards[mid-1]==target:
            return 'left'
        else:
            return 'found'
    elif mid_number < target:
        return 'left'
    else:
        return 'right'

def locate_card(cards, target):
    if len(cards) == 0: return -1
    low, high = 0, len(cards) - 1

    while low <= high:
        mid = (low+high)//2
        loc = test_location(cards, target, mid)

        if loc == 'found':
            return mid
        elif loc == 'left':
            high = mid - 1
        elif loc == 'right':
            low = mid + 1
    return -1

def evaluate_test_cases(function, tests):
    for test in tests:
        result = function(**test['input'])
        print(f"Input: {test['input']['cards']}, {test['input']['target']}")
        print(f"Expected Result: {test['output']}")
        print(f"Actual Result: {result}")
        print(result == test['output'])
evaluate_test_cases(locate_card, tests)
