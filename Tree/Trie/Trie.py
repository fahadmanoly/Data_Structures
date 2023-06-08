class TrieNode:
    def __init__(self):
        self.children={}
        self.endofstring=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        current=self.root
        for i in word:
            ch=i
            node=current.children.get(ch)
            if node==None:
                node=TrieNode()
                current.children.update({ch:node})
            current=node
        current.endofstring=True
        print('inserted successfully')

    def search(self,word):
        current=self.root
        for i in word:
            node=current.children.get(i)
            if node==None:
                print('not present')
                return False
            current=node
        if current.endofstring ==True:
            print('present')
            return True
        else:
            print('its the prefix')
            return False


tr=Trie()
tr.insert('fahad')
print(tr.root.children)
tr.search('fahad')
tr.search('fah')
tr.search('fahads')
