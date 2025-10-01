class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right

    @classmethod
    def build_tree(cls, values):
        from collections import deque
        root = TreeNode(values[0])
        queue = deque([root])
        i = 1
        while i < len(values):
            current = queue.popleft()
            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1
        return root

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right.left = TreeNode(6)
node.right.right = TreeNode(7)

root = TreeNode.build_tree([1,2,3,4,5,None,8,None,None,6,7,9])

# 🔁 Inorder Traversal (Left → Root → Right) DFS

print("Inorder Traversal==>")


def inorder(node: TreeNode):
    if node:
        inorder(node.left)
        print(node.val, end=' ')
        inorder(node.right)

inorder(root)
print("==============================================================")
# inorder(node)

print("\nPreorder Traversal")

# 🔁 Preorder Traversal (Root → Left → Right)


def preorder(node: TreeNode):
    if node:
        print(node.val, end=' ')
        preorder(node.left)
        preorder(node.right)


preorder(node)

print("\nPostorder Traversal")


# 🔁 Postorder Traversal (Left → Right → Root)
def postorder(node: TreeNode):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val, end=' ')


postorder(node)

# 🔄 Level Order Traversal (Breadth-First Search)

print("\nLevelorder Traversal")


def levelorder(node: TreeNode):
    if not node:
        return
    from collections import deque
    queue = deque([node])

    while queue:
        current = queue.popleft()
        print(current.val,  end=' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


levelorder(node)

# Insert into BST


def insert(root: TreeNode, key: int):
    if root is None:
        return TreeNode(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


root = None
values = [50, 30, 70, 20, 40, 60, 80]
for val in values:
    root = insert(root, val)

print("\nInorder traversal of BST:")
inorder(root)

# Search in BST


def search(root: TreeNode, key: int) -> bool:
    if root is None:
        return False
    if root.val == key:
        return True

    if key < root.val:
        return search(root.left, key)
    else:
        return search(root.right, key)


print("\nSearch for 60:", search(root, 60))  # True
print("Search for 90:", search(root, 90))     # False


def find_min(node: TreeNode, key) -> TreeNode:
    while node.left:
        node = node.left
    return node


def delete(root: TreeNode, key: int) -> TreeNode:
    if root is None:
        return False

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        # Case 1 & 2: node with 0 or 1 child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Case 3: node with 2 children
        right_min_node = find_min(root.right, key)
        root.val = right_min_node.val
        root.right = delete(root.right, right_min_node.val)

    return root


print("\nDelete 20 (leaf):")
root = delete(root, 20)
inorder(root)

print("\nDelete 30 (has one child):")
root = delete(root, 30)
inorder(root)

print("\nDelete 50 (has two children):")
root = delete(root, 50)
inorder(root)

# ✅ Part B: Tree Properties
# 1. Height of Tree


def height(node: TreeNode) -> int:
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1


print("\nHeight of BST:", height(root))

#  Count Total Nodes


def count_nodes(node: TreeNode) -> int:
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


print("Count Nodes of BST:", count_nodes(root))

# Count Leaf Nodes


def count_leaves(node: TreeNode) -> int:
    if node is None:
        return 0
    if not node.left and not node.right:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)


print("Count Leaves of BST:", count_leaves(root))


#  1. Check if a Tree is a BST
def is_bst(node: TreeNode, min_val=float('-inf'), max_val=float('inf')) -> bool:
    if node is None:
        return True
    if not (min_val < max_val):
        return False
    return is_bst(node.left, min_val, node.val) and is_bst(node.right, node.val, max_val)


print("Is valid BST:", is_bst(root))

# 2. Lowest Common Ancestor (LCA) in BST


def lca(node: TreeNode, n1: int, n2: int) -> TreeNode:
    if node is None:
        return None
    if n1 < node.val and n2 < node.val:
        return lca(node.left, n1, n2)

    if n1 > node.val and n2 > node.val:
        return lca(node.right, n1, n2)

    return root


ancestor = lca(root, 40, 80)
print("LCA of 40 and 80:", ancestor.val)

#  3. Print All Nodes in Range [L, R]


def print_range(node: TreeNode, L: int, R: int):
    if node is None:
        return
    if node.val > L:
        print_range(node.left, L, R)
    if L <= node.val <= R:
        print(node.val, end=' ')
    if node.val < R:
        print_range(node.right, L, R)


print("Nodes in range [40, 75]:", end=' ')
print_range(root, 40, 75)
