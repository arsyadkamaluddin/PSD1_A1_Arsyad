import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_tree(teks):
    freq = Counter(teks)
    heap = [Node(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    return heap[0]

def konversi(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}
    if node.char is not None:
        codebook[node.char] = prefix
    if node.left is not None:
        konversi(node.left, prefix + "0", codebook)
    if node.right is not None:
        konversi(node.right, prefix + "1", codebook)
    return codebook

def kompres(teks):
    root = huffman_tree(teks)
    codebook = konversi(root)
    encoded_text = ''.join(codebook[char] for char in teks)
    return encoded_text, codebook

teks = "Ini adalah contoh kata yang akan dikompres menggunakan huffman"
print("Teks asli:", teks)
encoded_text, codebook = kompres(teks)
print("Teks terkompress :", encoded_text)
print("Susunan kode")
[print(x+" | "+codebook[x]) for x in codebook]
