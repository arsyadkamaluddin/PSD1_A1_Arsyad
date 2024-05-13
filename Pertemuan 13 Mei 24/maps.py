def convert(a):
    if a.isupper():
        return a.lower()
    return a.upper()
kalimat = "Indonesia Tanah Air beta"
kalimat = list(kalimat)
kalimat = list(map(convert,kalimat))
print("".join(kalimat))

