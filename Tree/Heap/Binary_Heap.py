class Heap:
    def __init__(self):
        self.heap_list=[None]
        self.heap_size=0

    def heapify_up(self,i):
        while i//2 >0:
            if self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i],self.heap_list[i//2]=self.heap_list[i//2],self.heap_list[i]
            i=i//2

    def insert(self,value):
        self.heap_list.append(value)
        self.heap_size += 1
        self.heapify_up(self.heap_size)

    def minimum_child(self,i):
        if (i*2)+1 > self.heap_size:
            return i*2
        else:
            if self.heap_list[i*2] < self.heap_list[(i*2)+1]:
                return i*2
            else:
                return (i*2)+1
            
    def heapify_down(self,i):
        while i*2 <= self.heap_size:
            mc=self.minimum_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i],self.heap_list[mc]=self.heap_list[mc],self.heap_list[i]
            i=mc

    def delete(self):
        min_value=self.heap_list[1]
        self.heap_list[1]=self.heap_list[self.heap_size]
        self.heap_size = self.heap_size - 1
        self.heap_list.pop()
        self.heapify_down(1)
        return min_value
    
    def display(self):
        print(self.heap_list)
        for i in range(len(self.heap_list)):
            print(self.heap_list[i])

    
heap=Heap()
heap.insert(10)
heap.insert(15)
heap.insert(5)
heap.insert(25)
heap.insert(35)
heap.insert(2)


heap.display()




    
        