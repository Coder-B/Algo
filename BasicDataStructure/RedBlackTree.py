# 红黑树
class TreeNode:
    RED = "TreeNode.RED"
    BLACK = "TreeNode.BLACK"
    def __init__(self, val, name):
        self.val = val
        self.name = name
        # 新增节点默认TreeNode.RED，根节点在reblance中调节
        self.color = TreeNode.RED

    def findNode(self, target):
        print(self.name,self.color)
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
                newNode.rebalance()
                return newNode
        elif self.val < newVal:
            if hasattr(self,"right"):
                return self.right.addNode(newVal,newName)
            else:
                newNode = TreeNode(newVal, newName)
                self.right = newNode
                newNode.parent = self
                newNode.rebalance()
                return newNode
        else:
            return self

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


# 算法解释逻辑参见 https://buwenqi.github.io/2018/01/02/%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3%E7%BA%A2%E9%BB%91%E6%A0%91%E5%8E%9F%E7%90%86%E4%B8%8E%E5%AE%9E%E7%8E%B0/
    def rebalance(self):
        # 根节点color设置为TreeNode.BLACK
        if not hasattr(self,"parent"):
            self.color = TreeNode.BLACK
        elif self.parent.color == TreeNode.RED:
            p = self.parent
            # 由于红黑树要求根节点一定是黑，所以如果 self.parent.color == TreeNode.RED，那么一定存在p.parent
            g = p.parent
            # 当p是g的左子树情况
            if p == g.left:
                s = g.right
                if s.color == TreeNode.BLACK:
                    # 新插入的节点是左节点，https://i.imgur.com/gmwg6rv.png
                    if self == p.left:
                        g.rotateRight()
                        p.color = TreeNode.BLACK
                        g.color = TreeNode.RED
                    # 新插入的节点是右节点，https://i.imgur.com/LN7UQMf.png
                    else:
                        p.rotateLeft()
                        g.rotateRight()
                        self.color = TreeNode.BLACK
                        g.color = TreeNode.RED
                # subling 节点和parent节点均为TreeNode.RED的场景，https://i.imgur.com/lPIkMUF.png
                else:
                    p.color = TreeNode.BLACK
                    s.color = TreeNode.BLACK
                    g.color = TreeNode.RED
                    g.rebalance()
            # p是g的右子树情况
            else:
                s = g.left
                if s.color == TreeNode.BLACK:
                    if self == p.right:
                        g.rotateLeft()
                        g.color = TreeNode.RED
                        p.color = TreeNode.BLACK
                    else:
                        p.rotateRight()
                        g.rotateLeft()
                        g.color = TreeNode.RED
                        self.color = TreeNode.BLACK
                else:
                    s.color = TreeNode.BLACK
                    p.color = TreeNode.BLACK
                    g.color = TreeNode.RED
                    g.rebalance()
            


t1 = TreeNode(10,"t1")
t1.rebalance()
t2 = t1.addNode(7, "t2")
t3 = t1.addNode(15,"t3")

t4 = t2.addNode(6,"t4")
t5 = t2.addNode(8,"t5")

t6 = t3.addNode(12,"t6")
t7 = t3.addNode(16,"t7")

t8 = t4.addNode(5,"t8")

t = t1.findNode(5)
print(t.name)
