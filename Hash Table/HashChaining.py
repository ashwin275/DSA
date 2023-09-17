class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]

    def get_hash(self, key):
        total_asci = 0
        for i in key:
            total_asci += ord(i)

        return total_asci % self.max

    def __setitem__(self, key, value):
        hash_index = self.get_hash(key)
        found = False
        for index, elements in enumerate(self.arr[hash_index]):
            if elements[0] == key:
                found = True
                self.arr[hash_index][index] = (key, value)
        if not found:
            self.arr[hash_index].append((key, value))

    def __getitem__(self, item):

        hash_index = self.get_hash(item)

        if self.arr[hash_index]:
            for index, element in enumerate(self.arr[hash_index]):
                if element[0] == item:
                    return self.arr[hash_index][index][1]
        else:
            raise KeyError(f'{item} not found in the table')

    def __delitem__(self, key):
        hash_index = self.get_hash(key)
        found = False

        for index , elements in enumerate(self.arr[hash_index]):
            if elements[0] == key:
                found = True
                del self.arr[hash_index][index]
        if not found:
            raise KeyError(f'{key} not found in the table')



