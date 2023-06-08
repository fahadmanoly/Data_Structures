class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        
        if self.key == data:
            print('it has already that value and duplicate not supported')
            return
        
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)

    def search(self,data):
        if self.key == data:
            print('Node found ')
            return
        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print('Node not found')
                return
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print('Node not found')

    def preorder(self):
        print(self.key, end=' ')
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=' ')
        if self.rchild:
            self.rchild.inorder()


    def InOrder_2(self):
        root = self.key
        if root is not None:
            self.InOrder(root.lchild)
            print(root.key)
            self.InOrder(root.rchild)

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end=' ')

    def delete(self,data,current):
        if self.key is None:
            print('Tree is empty')
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data,current)
            else:
                print('node in the tree')
        
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data,current)
            else:
                print('node not in the tree')
        else:
            if self.lchild is None:
                temp=self.rchild
                #for deleting root node
                if data == current:
                    self.key=temp.key
                    self.lchild = temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return
                #deleting root node condition finshes
                self=None
                return temp
            if self.rchild is None:
                temp=self.rchild
                # for deleting root node
                if data ==current:
                    self.key = temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return
                # deleting root node condition finishes
                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key = node.key
            self.rchild=self.rchild.delete(node.key,current)
        return self
    
    def minimum(self):
        if self.lchild:
            node=self.lchild
            while node.lchild:
                node=node.lchild
            print('minimum is',node.key)
        else:
            print('minimum is',self.key)

    def maximum(self):
        if self.rchild:
            node=self.rchild
            while node.rchild:
                node=node.rchild
            print('maximum is',node.key)
        else:
            print('maximum is',self.key)

    def prime(self,num):
        c=int(num**.5)+1
        for i in range(2,c):
            if num%i ==0:
                break
        else:
            print(c,' as prime')


                
root=BST(10)
in1=[4,1,58,3,9]
for i in in1:
    root.insert(i)
root.search(4)
print('preorder')
root.preorder()
print('\n')
print('post order')
root.postorder()
print('\n')
print('inorder')
root.inorder()
print('\n')
def counting(node):
    if node is None:
        return 0
    return 1+counting(node.lchild)+counting(node.rchild)

print('the count is',counting(root))
if counting(root)>1:
    root.delete(10,root.key)
else:
    print('cant perform deletion operation since it has only root node')
print('after deleting')
root.inorder()
print('\n')
root.minimum()
root.maximum()


