import heapq

class HeapWithDel():
    def __init__(self, isMulti=True) -> None:
        self.heap = []
        self.values = {}
        self.isMulti = isMulti

    def push(self, value):
        if value not in self.values:
            self.values[value] = 1
            heapq.heappush(self.heap, value)
        elif self.isMulti:
                self.values[value] += 1

    def pop(self):
        result = self.heap[0]
        self.delete(result)

        return result

    def clean_heap(self):
        while (len(self.heap) > 0) and (self.values[self.heap[0]] == 0):
            del self.values[self.heap[0]]
            heapq.heappop(self.heap)

    def delete(self, value):
        if value not in self.values: return False

        if self.values[value] > 0:
            self.values[value] -= 1
        else:
            return False
        
        self.clean_heap()
        return True

    def get_first(self):
        return self.heap[0]
    
    def __bool__(self):
        return bool(self.heap)
    
    def __str__(self) -> str:
        return str(self.heap)

class MyHeap():
    def __init__(self) -> None:
        self.heap = []

    def push(self, val):
        self.heap.append(val)

        curr_index = len(self.heap)-1
        prev_index = (curr_index-1)//2
        
        while (curr_index > 0) and self.heap[prev_index] > self.heap[curr_index]:
            self.heap[prev_index], self.heap[curr_index] = self.heap[curr_index], self.heap[prev_index]
            curr_index = prev_index
            prev_index = (curr_index-1)//2

    def pop(self):
        if len(self.heap) == 0: raise IndexError('pop from empty heap')
        if len(self.heap) == 1: return self.heap.pop()
        
        length = len(self.heap)
        if length % 2 == 0: self.heap.append(self.heap[-1])

        res = self.heap[0]
        self.heap[0] = self.heap[-1]
        
        curr_index = 0
        while (2*curr_index+2 < len(self.heap)):
            if self.heap[2*curr_index+1] > self.heap[2*curr_index+2]:
                next_index = 2*curr_index+2
            else:
                next_index = 2*curr_index+1

            if self.heap[next_index] < self.heap[curr_index]:
                self.heap[curr_index], self.heap[next_index] = self.heap[next_index], self.heap[curr_index]
                curr_index = next_index
            else:
                break

        while len(self.heap) >= length:
            self.heap.pop()

        return res
    
    def __str__(self) -> str:
        return str(self.heap)
    
    def __bool__(self):
        return bool(self.heap)
   

if __name__ == '__main__': 
    import heapq
    import time, random

    numbers = [1, 10, 2, 4, 8, 6, 3, 9, 5, 7, 0]
    print('='*50)
    print('Sorting with heap')
    print(f'Source:\n{numbers}\n')
    
    print('MyHeap')
    heap_min = MyHeap()
    for num in numbers:
        heap_min.push(num)

    temp_lst = []
    while heap_min:
        temp_lst.append(heap_min.pop())
    print(temp_lst)

    print('heapq')
    heap = []
    for num in numbers:
        heapq.heappush(heap, num)

    temp_lst = []
    while heap:
        temp_lst.append(heapq.heappop(heap))
    print(temp_lst)

    print('Heap with Del')
    heap_min = HeapWithDel()
    for num in numbers:
        heap_min.push(num)

    temp_lst = []
    while heap_min:
        temp_lst.append(heap_min.pop())
    print(temp_lst)

    print('-'*50)
    print('Speed test')
    test_case = []
    for i in range(1000000):
        test_case.append(random.randint(0, 2**32-1))      

    # MyHeap
    time0 = time.time()
    heap = MyHeap()
    for num in test_case:
        heap.push(num)

    while heap:
        heap.pop()
    time1 = time.time()

    print(f'MyHeap: {time1-time0}')

    # heapq
    time0 = time.time()
    heap = []
    for num in test_case:
        heapq.heappush(heap, num)

    while heap:
        heapq.heappop(heap)
    time1 = time.time()

    print(f'  heapq: {time1-time0}')

    # Heap with Del
    temp_case = []
    for i in range(len(test_case)):
        temp_case.append((test_case[i], i))

    delorder = temp_case.copy()
    random.shuffle(delorder)

    time0 = time.time()
    heap = HeapWithDel()
    for num in temp_case:
        heap.push(num)

    for num in delorder:
        heap.delete(num)
    time1 = time.time()

    print(f'HeapWithDel: {time1-time0}')     
    print('='*50)   