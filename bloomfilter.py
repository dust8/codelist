import math
import hashlib


class BloomFilter:
    hash_algorithms = [hashlib.md5, hashlib.sha1,
                       hashlib.sha224, hashlib.sha256]

    def __init__(self, m):
        self.m = m
        self.filter = bytearray(math.ceil(m / 8))

    def _hash(self, value):
        for hash_algorithm in self.hash_algorithms:
            digest = int(hash_algorithm(str(value).encode()).hexdigest(), 16)
            # 进行and运算来保证值在存储范围内
<<<<<<< HEAD
            yield digest & self.m
=======
            yield digest & (self.m - 1)
>>>>>>> 2c271d92e4f9cf8d38160c56032f10851e0e1d50

    def add(self, value):
        for digest in self._hash(value):
            # 把对应的bit设置为1
            self.filter[int(digest / 8)] |= 2 ** (digest % 8)

    def __contains__(self, item):
        return all(self.filter[int(digest / 8)] & (2 ** (digest % 8))
                   for digest in self._hash(item))


if __name__ == '__main__':
    bf = BloomFilter(200)
<<<<<<< HEAD
    bf.add(2)
    bf.add(1)
    print(1 in bf, '2' in bf)  # True False
=======
    bf.add('2')
    bf.add(1)
    print(1 in bf, '20' in bf)  # True False
>>>>>>> 2c271d92e4f9cf8d38160c56032f10851e0e1d50
