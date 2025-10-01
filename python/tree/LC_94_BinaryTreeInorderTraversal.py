# https://leetcode.com/problems/binary-tree-inorder-traversal/
from typing import Optional, List
from tree.treeNode import TreeNode


class Solution:
    def traverse_inorder(self, vals, node):
        if node:
            self.traverse_inorder(vals, node.left)
            vals.append(node.val)
            self.traverse_inorder(vals, node.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        vals = []
        self.traverse_inorder(vals, root)
        return vals
