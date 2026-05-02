class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:

    def __init__(self):
        self.my_map = [None] * 1000

    def _hash(self, key):
        return key % 1000
        

    def put(self, key: int, value: int) -> None:
        index = self._hash(key) # now index gives us the bucket, where to store the key
        if self.my_map[index] is None:
            self.my_map[index] = Node(key, value) # set the new node to the key
        else:
            current = self.my_map[index] # start at the head
            while current is not None:
                if current.key == key:
                    current.value = value
                    return
                
                if current.next is None:
                    current.next = Node(key, value)
                    return 

                current = current.next # move to the next node

    def get(self, key: int) -> int:
        index = self._hash(key)
        current = self.my_map[index]
        while current is not None:
            if current.key == key:
                return current.value
            else:
                current = current.next
        return -1
        

    def remove(self, key: int) -> None:
        index = self._hash(key)
        current = self.my_map[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None: # removing the head
                    self.my_map[index] = current.next # set the current.next as a head
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next
        