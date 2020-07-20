class KeyValuePair:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, size: int):
        self.hash_table = [None] * size
        self.size = size

    def hash_code(self, key: int):
        return key % self.size

    def insert(self, key: int, value: int) -> bool:
        new_dict = {key: value}
        my_hash = self.hash_code(key)

        for index in range(my_hash, self.size-1):
            if self.hash_table[index] is None:
                self.hash_table[index] = new_dict
                return True

        return False

    def search(self, key: int) -> int:
        my_hash = self.hash_code(key)

        for index in range(my_hash, self.size-1):
            temp = self.hash_table[index]
            if temp is not None and key in temp.keys():
                return index

        return -1

    def delete(self, key: int) -> object:
        index = self.search(key)
        if index < 0:
            return None
        else:
            temp = self.hash_table[index]
            self.hash_table[index] = None
            return temp

    def print_table(self):
        for index in range(0, self.size):
            print(f'index: {index}: {self.hash_table[index]}')

def main():
    temp = HashTable(20)
    temp.insert(1,20)
    temp.insert(2, 70)
    temp.insert(42, 80)
    temp.insert(4, 25)
    temp.insert(12, 44)
    temp.insert(14, 32)
    temp.insert(17, 11)
    temp.insert(13, 78)
    temp.insert(37, 98)
    temp.print_table()
    print(temp.search(37))
    print(temp.search(55))
    print(temp.search(14))
    temp.delete(14)
    temp.delete(55)
    temp.print_table()


if __name__ == '__main__':
    main()