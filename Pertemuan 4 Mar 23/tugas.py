jumlah_mhs = int(input("Masukkan jumlah mahasiswa : "))
nilai = [[0]]*jumlah_mhs
nim = []
nama = []
for i in range(jumlah_mhs):
    nama.append(input(f"Nama mahasiswa ke-{i+1} : "))
    nim.append(input(f"NIM mahasiswa ke-{i+1} : "))
    jumlah_nilai = int(input(f"Jumlah nilai mahasiswa ke-{i+1} : "))
    print()
    for a in range(jumlah_nilai):
        nilai[i].append(int(input(f"Nilai ujian ke-{a+1} : ")))
    print()

rata = [sum(i)/(len(i)-1) for i in nilai]

for i in range(jumlah_mhs):
    print(f"Nama : {nama[i]}")
    print(f"NIM : {nim[i]}")
    print(f"Rata-rata nilai ujian : {rata[i]}")
    print()
