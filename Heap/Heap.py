class Heap:
    def __init__(self):
        self.arr = []
    
    def insert(self, val):
        self.arr.append(val)
        self.heapify_up(len(self.arr) - 1)
    
    def remove(self, val):
        index = self.arr.index(val)
        self.swap(index, len(self.arr) - 1)
        self.arr.pop()
        self.heapify_down(index)
    
    def getMin(self):
        if len(self.arr) > 0:
            print(self.arr[0])
    
    def heapify_up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.arr[parent] > self.arr[index]:
            self.swap(parent, index)
            self.heapify_up(parent)
    
    def heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.arr) and self.arr[left] < self.arr[smallest]:
            smallest = left

        if right < len(self.arr) and self.arr[right] < self.arr[smallest]:
            smallest = right

        if smallest != index:
            self.swap(smallest, index)
            self.heapify_down(smallest)
    
    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

heap = Heap()
N = int(input())
for i in range(N):
    inp = input()
    inp = inp.split(" ")
    func = int(inp[0])
    val = int(inp[1]) if len(inp)>1 else -1
    if func == 1:
        heap.insert(val)
    elif func == 2:
        heap.remove(val)
    elif func == 3:
        heap.getMin()
