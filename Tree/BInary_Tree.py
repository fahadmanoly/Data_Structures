class Node:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

class BinaryTree:
    def __init__(self,root=None):
        self.root=root

    def count(self,node):
        if node is None:
            return 0
        return 1+ self.count(node.lchild)+self.count(node.rchild)

    def insert(self,data):
        if self.root is  None:
            self.root = Node(data)
        else:
            self._insert(self.root,data)
        
    def _insert(self,node,data):
        if node.lchild is None:
            node.lchild = Node(data)
        elif node.rchild is None:
            node.rchild=Node(data)
        else:
            if self.count(node.lchild) <= self.count(node.rchild):
                self._insert(node.lchild,data)
            else:
                self._insert(node.rchild,data)

    def porder(self):
        self._porder(self.root)

    def _porder(self,node):
        if node is not None:
            print(node.key)
            preorder(node.lchild)
            preorder(node.rchild)





def preorder(root):
    if not root:
        return
    print(root.key)
    preorder(root.lchild)
    preorder(root.rchild)

bt=Node('Drinks')
cold=Node('Cold')
hot=Node('Hot')
col=Node('Cola')
pep=Node('Pepsi')
tea=Node('Tea')
coff=Node('Coffee')
bt.lchild=cold
bt.rchild=hot
cold.lchild=pep
cold.rchild=col
hot.lchild=tea
hot.rchild=coff
bt2=BinaryTree()
bt2.insert(10)
bt2.insert(20)
bt2.insert(30)
bt2.insert(40)

preorder(bt)
bt2.porder()


