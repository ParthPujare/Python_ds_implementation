class MinHeap:

    def __init__(self):
        self.heap = []

    def __len__(self):
        return(len(self.heap))

    def __repr__(self):
        return(str(self.heap))

    def insert(self,key, val):                                          ##TC---> O(log(n))
        self.heap.append((key,val))
        self._sift_up(len(self.heap)-1)

    def peek_min(self):                                                 ##TC---> O(1)      
        if not self.heap:
            raise KeyError ("Empty heap !")
        else:
            return self.heap[0]

    def extract_min(self):                                              ##TC---> O(log(n))
        if not self.heap:
            raise KeyError("Empty heap !")
        else:
            min_ele = self.heap[0]
            last_ele = self.heap.pop()

            if self.heap:
                self.heap[0] = last_ele
                self._sift_down(0)
        return min_ele

    def heapify(self, elements):                                        ##TC---> O(n)
        self.heap = list(elements)

        for i in reversed(range(self._parent(len(self.heap)-1)+1)):
            self._sift_down(i)

    def meld(self, other_heap):                                         ##TC---> O(n)
        combined_heap = self.heap + other_heap.heap
        self.heapify(combined_heap)

        other_heap.heap = []

    def _parent(self, index):                                           ##TC---> O(1)
        return((index-1)//2) if index != 0 else None
    
    def _left(self,index):                                              ##TC---> O(1)
        left = ((index*2)+1)
        return left if ((index*2)+1) < len(self.heap) else None
    
    def _right(self, index):                                            ##TC---> O(1)
        right = ((index*2)+2)
        return right if ((index*2)+2) < len(self.heap) else None
    
    def _sift_up(self, index):          ##Also called swin operation    ##TC---> O(log(n))
        parent_index = self._parent(index)

        while parent_index is not None and self.heap[index][0] < self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = self._parent(index)
            
    def _sift_down(self, index):        ##Also called sink operation    ##TC---> O(log(n))
        while True:
            smallest = index
            left_index, right_index = self._left(index), self._right(index)
            if left_index is not None and self.heap[left_index][0] < self.heap[smallest][0]:
                smallest = left_index
            if right_index is not None and self.heap[right_index][0] < self.heap[smallest][0]:
                smallest = right_index
            if smallest == index:
                break
            
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

if __name__ == "__main__":
    h = MinHeap()
    h.heapify([[10,'10'],[9,'9'],[8,'8'],[7,'7'],[6,'6'],[5,'5'],[4,'4'],[3,'3'],[2,'2'],[1,'1'],])
    print(h)

    print(h.extract_min())
    print(h.extract_min())
    print(h.extract_min())

    print(h)

    h.insert(2,2)
    print(h)