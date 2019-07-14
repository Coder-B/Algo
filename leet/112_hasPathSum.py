# https://leetcode.com/problems/path-sum/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == sum
        else:
            if root.left is not None:
                if self.hasPathSum(root.left,sum-root.val):
                    return True
            if root.right is not None:
                if self.hasPathSum(root.right,sum-root.val):
                    return True
            return False
            

s=Solution()
a = TreeNode(1)
b = TreeNode(2)
a.left = b
print(s.hasPathSum(a,1))