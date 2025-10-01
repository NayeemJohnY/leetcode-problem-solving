# https://leetcode.com/problems/symmetric-tree
from typing import Optional
from tree.treeNode import TreeNode


class Solution:

    def isMirror(self, left: TreeNode, right: TreeNode):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left, root.right)
