class Heap:
    def __init__(self):
        self.array = []

    def __str__(self):
        return str(self.array)

    def insertelement(self, data):
        self.array.append(data)
        length = len(self.array)
        if length >1:
            node_num = length-1
            while True:
                next_node_num = int(node_num/2)
                if self.array[next_node_num] < self.array[node_num]:
                    temp = self.array[node_num]
                    self.array[node_num] = self.array[next_node_num]
                    self.array[next_node_num] = temp
                else:
                    break
                node_num = int(node_num/2)
                if(node_num == 0):
                    break

if __name__  == '__main__':
    L = [2, 1, 5, 3, 4, 7, 9, 2, 3, 6]

    m_heap = Heap()
    for n in L:
        m_heap.insertelement(n)
    print('Heap : ', m_heap)