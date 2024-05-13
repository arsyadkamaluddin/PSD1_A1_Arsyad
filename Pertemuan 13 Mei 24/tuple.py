barang = [
    ("Slamet", [("Sepatu", 2), ("Laptop", 1), ("Jeruk", 3)]),
    ("Ani", [("Pisang", 1), ("Ketela", 4), ("Baju", 5)]),
    ("Budi", [("Seterika", 2), ("Buku", 3), ("Kamera", 4)])
]
def count(e):
    jml = 0
    for i in e[1]:
        jml += i[1]
    to_dict = '{"'+e[0]+'":'+str(jml)+'}'
    return eval(to_dict)
namun = list(map(count,barang))
print(namun)
