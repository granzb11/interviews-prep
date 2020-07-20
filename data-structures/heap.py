class Heap:
    def __init__(self, old_list: list = []):
        """Heap Constructor"""
        self.heap = old_list
        #clearing index 0 with empty object
        self.heap.insert(0, None)
        self.heap_size = len(self.heap)

    #def build_heap(self,):

    def percolate_down(self, index: int):
        """Percolate Down"""
        #online algorithm
        # tmp = self.heap[index]
        #
        # while (2 * index) <= self.heap.size:
        #     child = 2 * index
        #
        #     if child != size and self.heap[child] > self.heap[child+1]:
        #         child += 1
        #
        #     if tmp > self.heap[child]:
        #         self.heap[k] = heap[child]
        #     else:
        #         break
        #
        #     k = child
        #
        # self.heap[k] = tmp

        temp = self.heap[index]
        # get children indexes
        if index * 2 > self.heap_size - 1:
            left_child_index = index
        else:
            left_child_index = index * 2

        if (index * 2) + 1 > self.heap_size - 1:
            right_child_index = index
        else:
            right_child_index = (index * 2) + 1

        #check which child node is smaller
        if self.heap[left_child_index] < self.heap[right_child_index]:
            min_child_index = left_child_index
        else:
            min_child_index = right_child_index

        #check if min child is smaller than parent
        if self.heap[min_child_index] < self.heap[index]:
            #swap values in heap
            self.heap[index] = self.heap[min_child_index]
            self.heap[min_child_index] = temp
            #call percolate down again
            self.percolate_down(min_child_index)
        else:
            return

    def percolate_up(self, index: int):
        temp = self.heap[index]
        parent_index: int = index//2

        if parent_index < 1:
            return
        else:
            if self.heap[parent_index] > temp:
                #swap values
                self.heap[index] = self.heap[parent_index]
                self.heap[parent_index] = temp
                self.percolate_up(parent_index)
            else:
                return

    def insert(self, value: int):
        self.heap.append(value)
        self.heap_size += 1
        self.percolate_up(self.heap_size - 1)

    def delete_min(self) -> int:
        min = self.heap[1]
        temp = self.heap.pop()
        self.heap_size -= 1

        if(self.heap_size > 1):
            self.heap[1] = temp
            self.percolate_down(1)
            return min
        return min

    def heap_sort(self) -> list:
        sorted_list = []
        for item in range(0, self.heap_size-1):
            min = self.delete_min()
            print(f'min: {min}, heap: {self.heap}, heap_size: {self.heap_size}')
            sorted_list.append(min)
        return sorted_list

def main():
    temp = Heap()
    temp.insert(1)
    temp.insert(7)
    temp.insert(20)
    temp.insert(13)
    temp.insert(25)
    temp.insert(9)
    temp.insert(15)
    print(temp.heap)
    temp.insert(6)
    print(temp.heap)
    min = temp.delete_min()
    print(f'min: {min}')
    print(temp.heap)
    # min = temp.delete_min()
    # print(f'min: {min}')
    # print(temp.heap)
    # min = temp.delete_min()
    # print(f'min: {min}')
    # print(temp.heap)
    # min = temp.delete_min()
    # print(f'min: {min}')
    # print(temp.heap)
    sorted_list = temp.heap_sort()
    print(f'sorted_list: {sorted_list}')

if __name__ == '__main__':
    main()
