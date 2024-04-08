class SegmentTree_Parameters:
    def __init__(self, neutral_calc, neutral_change, calc_op, change_op):
        self.neutral_calc = neutral_calc
        self.neutral_change = neutral_change

        self.calc_op = calc_op
        self.change_op = change_op

class SegmentTree():
    def __init__(self, array: list, st_params: SegmentTree_Parameters):
        def build_tree(array, index):
            if 2*index+1 > len(array)-1: return
            
            build_tree(array, 2*index+1)
            build_tree(array, 2*index+2)
            array[index] = (self.calc_op(array[2*index+1][0], array[2*index+2][0]), self.neutral_change)

        self.source_length = len(array)

        self.neutral_calc = st_params.neutral_calc
        self.neutral_change = st_params.neutral_change
        self.calc_op = st_params.calc_op
        self.change_op = st_params.change_op

        if not array: raise Exception('Array is empty')

        N = 1
        while N < self.source_length:
            N = N*2

        self.tree = [(self.neutral_calc, self.neutral_change)]*(2*N-1)

        for i in range(self.source_length):
            self.tree[N-1+i] = (array[i], self.neutral_change)

        build_tree(self.tree, 0)

    def __propagate(self, index):
        for curr_index in (2*index+1, 2*index+2):
            self.tree[curr_index] = (self.change_op(self.tree[curr_index][0], self.tree[index][1]), self.change_op(self.tree[curr_index][1], self.tree[index][1]))

        self.tree[index] = (self.tree[index][0], self.neutral_change)

    def getSegment(self, left, right):
        def get(l, r, i, li, ri):
            if l > ri or r < li: return self.neutral_calc
            if l <= li and r >= ri: return self.tree[i][0]
                             
            self.__propagate(i)
            
            mi = (li+ri)//2            
            vl = get(l, r, 2*i+1, li, mi)
            vr = get(l, r, 2*i+2, mi+1, ri)

            return self.calc_op(vl, vr)
        
        N = (len(self.tree)+1)//2
        l = N-1+left
        r = N-1+right

        return get(l, r, 0, N-1, 2*N-2)
    
    def setSegment(self, left, right, value):
        def set(l, r, i, li, ri, value):
            if l > ri or r < li: return

            if l <= li and r >= ri:
                self.tree[i] = (self.change_op(self.tree[i][0], value), self.change_op(self.tree[i][1], value))
                return
            
            self.__propagate(i)
                             
            mi = (li+ri)//2            
            set(l, r, 2*i+1, li, mi, value)
            set(l, r, 2*i+2, mi+1, ri, value)

            vl = self.tree[2*i+1][0]
            vr = self.tree[2*i+2][0]

            self.tree[i] = (self.calc_op(vl, vr), self.tree[i][1])

        N = (len(self.tree)+1)//2
        l = N-1+left
        r = N-1+right

        set(l, r, 0, N-1, 2*N-2, value)

if __name__ == '__main__':
    array = [1, 3, 4, 7, 4, 4, 5, 0, 9]

    def calculate(element1, element2):
        return max(element1, element2)
    
    def change(element, value):
        return element+value
    
    st_params = SegmentTree_Parameters(float('-inf'), 0, calculate, change)    
    seg_tree = SegmentTree(array, st_params)
    
    print(array)
    print('='*50)
    print(seg_tree.getSegment(0, 8))
    print(seg_tree.getSegment(2, 6))
    seg_tree.setSegment(4, 5, 2)
    print(seg_tree.getSegment(3, 5))
    print(seg_tree.getSegment(4, 5))
    seg_tree.setSegment(7, 7, 10)
    print(seg_tree.getSegment(7, 7))
    print(seg_tree.getSegment(0, 8))
    print(seg_tree.getSegment(6, 4))