import sys
import time
cases = int(sys.stdin.readline()[:-1])

class Node:
    def __init__(self):
        self.nexts = [0, 0]

# 将所有的前缀异或和，加入到 NumTrie，并按照前缀树组织
class NumTrie:
    def __init__(self):
        self.root = Node()

    def add(self, num):
        cur = self.root
        # move 向右位移多少位
        for move in range(8, -1, -1):
            # 获取对应位上的数字（0 或者 1）
            path = (num >> move) & 1
            cur.nexts[path] = cur.nexts[path] if cur.nexts[path] != 0 else Node()
            cur = cur.nexts[path]
    
    def max_xor(self, num):
        cur = self.root

        res = 0

        for move in range(8, -1, -1):
            path = (num >> move) & 1
            best = path ^ 1
            best = best if cur.nexts[best] != 0 else best ^ 1
            tmp = 1

            res |= (path ^ best) << move

            cur = cur.nexts[best]

        return res




for abfasdfs in range(cases):
    n = int(sys.stdin.readline()[:-1])
    a = sys.stdin.readline()[:-1].split(" ")
    a = [int(x) for x in a]
    b = [len(bin(x)) - 2 for x in a]
    maxBitSize = max(b)
    maxAns = max(a)
    prefix_sum = [0] * n
    prefix_sum[0] = a[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] ^ a[i]
    
    tries = NumTrie()
    tries.add(0)
    xor = 0
    res = 0
    for i in range(n):
        xor ^= a[i]
        res = max(res, tries.max_xor(xor))
        tries.add(xor)
    print(res)




