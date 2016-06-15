import math
import hashlib
from struct import pack


class BloomFilter:
    def __init__(self, n, p=0.001):
        """
        m: the number of bits in the array
        k: the number of hash functions

        :param n: the number of to insert elements
        :param p: false positive probability
        """
        if not n > 0:
            raise ValueError("n must be > 0")
        if not (0 < p < 1):
            raise ValueError("p must be between 0 and 1.")

        # http://www.cnblogs.com/allensun/archive/2011/02/16/1956532.html
        self.n = n
        self.p = p
        self.m = math.ceil(-n * math.log(p) / (math.log(2) ** 2))
        self.k = math.ceil(self.m * math.log(2) / self.n)

        self.filter = bytearray(math.ceil(self.m / 8))
        self.hashfn = hashlib.sha512
        self.salts = tuple(self.hashfn(pack('I', i)).digest() for i in range(self.k))

    def _hash(self, value):
        for salt in self.salts:
            digest = int(self.hashfn(str(value).encode() + salt).hexdigest(), 16)
            # 进行and运算来保证值在存储范围内
            yield digest & (self.m - 1)

    def add(self, value):
        for digest in self._hash(value):
            # 把对应的bit设置为1
            self.filter[int(digest / 8)] |= 2 ** (digest % 8)

    def __contains__(self, item):
        return all(self.filter[int(digest / 8)] & (2 ** (digest % 8))
                   for digest in self._hash(item))

    def __str__(self):
        return '<n=%s p=%s m=%s k=%s m/n=%s>' % (self.n, self.p, self.m, self.k, self.m / self.n)


if __name__ == '__main__':
    bf = BloomFilter(50000000)
    print(bf)
    bf.add(1)
    bf.add('1')
    bf.add((1))
    print(1 in bf)
    print('1' in bf)
    print((1) in bf)
    print(2 in bf)
