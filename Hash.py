class HashTable:
    # 테이블 생성
    def __init__(self, table_size):
        self.size = table_size
        self.hash_table = [0 for a in range(self.size)]

    def getKey(self, data):
        self.key = ord(data[0])
        return self.key

    # 해쉬화
    def hashFunction(self, key):
        return key % self.size

    # key로 value를 불러옴
    def getAddress(self, key):
        myKey = self.getKey(key)
        hash_address = self.hashFunction(myKey)
        return hash_address

    # key, value 등록하기
    def save(self, key, value):
        hash_address = self.getAddress(key)
        self.hash_table[hash_address] = value

    # 데이터 읽기
    def read(self, key):
        hash_address = self.getAddress(key)
        return self.hash_table[hash_address]

    # 데이터 삭제
    def delete(self, key):
        hash_address = self.getAddress(key)

        if self.hash_table[hash_address] != 0:
            self.hash_table[hash_address] = 0
            return True
        else:
            return False


# Test Code
h_table = HashTable(8)
h_table.save('a', '1111')
h_table.save('b', '3333')
h_table.save('c', '5555')
h_table.save('d', '8888')
print(h_table.hash_table)
print(h_table.read('d'))

h_table.delete('d')
print(h_table.hash_table)