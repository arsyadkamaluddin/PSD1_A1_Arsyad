def bisa_bentuk(koin, nilai):
    dp = [False] * (nilai + 1)
    dp[0] = True
    for coin in koin:
        for i in range(coin, nilai + 1):
            if dp[i - coin]:
                dp[i] = True
    
    return dp[nilai]

def minimal(koin, nilai):
    dp = [float('inf')] * (nilai + 1)
    dp[0] = 0
    for coin in koin:
        for i in range(coin, nilai + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[nilai] if dp[nilai] != float('inf') else -1

def cari_kombinasi(koin, nilai):
    dp = [[] for _ in range(nilai + 1)]
    dp[0] = [[]]

    for i in range(1, nilai + 1):
        for coin in koin:
            if i - coin >= 0:
                for combination in dp[i - coin]:
                    dp[i].append(combination + [coin])
    
    return dp[nilai]

def kombinasi(koin,nilai):
    print("=============")
    if bisa_bentuk(koin,nilai):
        print("uang pecahan ",", ".join(list(map(str,koin)))," bisa membentuk nilai ",nilai)
    else:
        print("uang pecahan ",", ".join(list(map(str,koin)))," tidak bisa membentuk nilai ",nilai)
    print("dengan jumlah minimal banyaknya koin adalah ",minimal(koin,nilai)," keping")
    banyak = cari_kombinasi(koin,nilai)
    print("terdapat ",len(banyak)," kombinasi yang bisa dilakukan")
    for i in banyak:
        print("||","-".join(list(map(str,i))))


koin = list(map(int,input("Masukkan pecahan koin ").split()))
nilai = int(input("Masukkan nilai yang dicari "))

kombinasi(koin,nilai)




