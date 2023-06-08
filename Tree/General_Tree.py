class GeneralTree():
    def __init__(self,data,children=[]):
        self.data=data
        self.children=children

    def __str__(self,level=0):
        ret = "  "* level + str(self.data) + '\n'
        for child in self.children:
            ret = ret + child.__str__(level+1)
        return ret

    def addchild(self,GeneralTree):
        self.children.append(GeneralTree)

tree = GeneralTree('drinks',[])
cold = GeneralTree('Cold',[])
hot = GeneralTree('Hot',[])
tree.addchild(cold)
tree.addchild(hot)
cola = GeneralTree('Cola',[])
pepsi = GeneralTree('Pepsi',[])
fanta = GeneralTree('Fanta',[])
tea = GeneralTree('Tea',[])
coffee = GeneralTree('Coffee',[])
boost = GeneralTree('Boost',[])
hot.addchild(tea)
hot.addchild(coffee)
hot.addchild(boost)
cold.addchild(cola)
cold.addchild(pepsi)
cold.addchild(fanta)

print(tree)
