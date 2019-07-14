# https://leetcode.com/problems/path-sum-ii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ret = []
        if root is not None:
            self.path(root,[],0,sum,ret)
        return ret
        
    def path(self, node: TreeNode, path: List[int], pathsum:int, target:int, pathList: List[List[int]]) -> None:
        if node.left is None and node.right is None:
            if pathsum+node.val == target:
                path.append(node.val)
                pathList.append(path.copy())
                path.pop()
            return
        if node.left is not None:
            path.append(node.val)
            self.path(node.left,path,pathsum+node.val,target,pathList)
            path.pop()
        if node.right is not None:
            path.append(node.val)
            self.path(node.right,path,pathsum+node.val,target,pathList)
            path.pop()