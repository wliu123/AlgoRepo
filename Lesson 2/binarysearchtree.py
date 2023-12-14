# Exercise: Define a function tree_to_tuple that converts a binary tree into a tuple representing the same tree. E.g. tree_to_tuple converts the tree created above to the tuple ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))). 

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def parse_tuple(data):
    # print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

tree = parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
def trees_to_tuple(node):
    pass

def display_keys(node, space='\t', level=0):
    # print(node.val if node else None, level)

    if node is None:
        print(space*level + '∅')
        return
    
    if node.left is None and node.right is None:
        print(space*level + str(node.val))
        return
    
    display_keys(node.right, space, level+1)
    print(space*level, str(node.val))
    display_keys(node.left, space, level+1)

display_keys(tree, '  ')

# Traverse tree in these orders: inorder, preorder, postorder

def traverse_inorder(node):
    if node is None:
        return []
    return (traverse_inorder(node.left)+
            [node.val] +
            traverse_inorder(node.right))

print(traverse_inorder(tree))

# height of a binary tree defined as the length of the longest path from root node to leaf. 

def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

print(tree_height(tree))

# count number of nodes in tree

def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)
print(tree_size(tree))

# Binary Search Tree
# Write a function to see if a binary tree is a binary search tree
# Write a function to find the maximum key in a binary tree
# Write a function to find the minimum key in a binary tree

def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True, None, None
    
    is_bst_left, min_left, max_left = is_bst(node.left)
    is_bst_right, min_right, max_right = is_bst(node.right)

    is_bst_node = (is_bst_left and is_bst_right and 
                   (max_left is None or node.val > max_left) and
                   (min_right is None or node.val < min_right))
    
    min_val = min(remove_none([min_left, node.val, min_right]))
    max_val = max(remove_none(max_left, node.val, max_right))

    print(node.key, min_val, max_val, is_bst_node)

    return is_bst_node, min_val, max_val