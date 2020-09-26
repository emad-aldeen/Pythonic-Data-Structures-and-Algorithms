class hash_table():
    def __init__(self, size):
        self.map = [None] * size
        self.size = size
    
    def hash(self, key):
        hashed_total = 0
        for char in key:
            hashed_total += ord(char)
        return hashed_total*77 % self.size

    def add(self,key,value):
        pass