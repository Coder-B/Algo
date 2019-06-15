# 红黑树
class TreeNode:
    def __init__(self, val, name):
        self.val = val
        self.name = name

    def findNode(self, target):
        print(self.name)
        if self.val == target:
            return self
        # <built-in function hasattr> 内置函数判断某对象是否有attr
        if self.val > target and hasattr(self,"left"):
            return self.left.findNode(target)
        elif self.val < target and hasattr(self,"right"):
            return self.right.findNode(target)
        else:
            return None

    def addNode(self, newVal, newName):
        if self.val > newVal:
            if hasattr(self,"left"):
                return self.left.addNode(newVal,newName)
            else:
                newNode = TreeNode(newVal, newName)
                self.left = newNode
                newNode.parent = self
                return newNode
        elif self.val < newVal:
            if hasattr(self,"right"):
                return self.right.addNode(newVal,newName)
            else:
                newNode = TreeNode(newVal, newName)
                self.right = newNode
                newNode.parent = self
                return newNode
        else:
            return None

    def rotateLeft(self):
        # 仅当存在右子树时，才有左转的可能
        if hasattr(self,"right"):
            rightSon = self.right
            # rightSon 的左子树是否需要挂载
            if hasattr(rightSon,"left"):
                self.right = rightSon.left
                rightSon.left.parent = self
            # 当前节点的parent左右子树变更
            if hasattr(self,"parent"):
                parent = self.parent
                if parent.left == self:
                    parent.left = rightSon
                else:
                    parent.right = rightSon
                # 当前节点的右子树parent变更
                rightSon.parent = parent
            # 最后变更当前节点，挂载到原右子树的左分支
            rightSon.left = self
            self.parent = rightSon

    def rotateRight(self):
        if hasattr(self,"left"):
            leftSon = self.left
            if hasattr(leftSon,"right"):
                self.left = leftSon.right
                leftSon.right.parent = self
            if hasattr(self,"parent"):
                parent = self.parent
                if parent.left == self:
                    parent.left = leftSon
                else:
                    parent.right = leftSon
                leftSon.parent = parent
            leftSon.right = self
            self.parent = leftSon

    def rebalance(self):


t1 = TreeNode(10,"t1")
t2 = t1.addNode(7, "t2")
t3 = t1.addNode(15,"t3")

t4 = t2.addNode(6,"t4")
t5 = t2.addNode(8,"t5")

t6 = t3.addNode(12,"t6")
t7 = t3.addNode(16,"t7")

t3.rotateLeft()

t = t1.findNode(14)
print(t.name)
