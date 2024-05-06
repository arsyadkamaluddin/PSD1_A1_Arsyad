import math
# inti penghitungan cosine similarity 
def cosine_similarity(vektor1, vektor2):
    produk = sum(a * b for a, b in zip(vektor1, vektor2))
    magnA = math.sqrt(sum(a**2 for a in vektor1))
    magnB = math.sqrt(sum(b**2 for b in vektor2))
    
    kesamaan = produk / (magnA * magnB)
    return kesamaan
# pembuatan vektor kalimat
def vektor(kalimat, kosaKata):
    return [kalimat.split().count(kata) for kata in kosaKata]

kalimatA = "Suspendisse sed massa vel felis finibus vestibulum. Donec lobortis placerat risus, id faucibus elit vehicula in. In egestas, nulla a rutrum sodales, dui eros interdum nulla, sit amet cursus ex neque in turpis. Ut pellentesque lorem in est tempor, id lobortis ligula dictum. Phasellus consectetur nisi at nulla cursus, in aliquam sapien aliquam. Sed in lorem vel nisl vestibulum condimentum. Maecenas ac lacus tellus. Nullam eget enim ac lorem tincidunt elementum sit amet vitae magna. Proin faucibus vehicula sapien, nec volutpat nisl. Curabitur suscipit, sem at auctor fermentum, turpis purus faucibus leo, nec vehicula neque leo at libero. Fusce eu fermentum velit. Nullam gravida justo nisl, vel ultricies nisi congue eget. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vivamus eleifend velit vel libero efficitur, id condimentum nunc lobortis. Vivamus sit amet eros ut eros dapibus venenatis."

kalimatB = "Fusce dignissim, quam at varius eleifend, urna tortor ultrices risus, sed dapibus ex leo at sapien. Vivamus dictum, ipsum et efficitur fermentum, elit velit condimentum libero, nec sollicitudin nisl risus eget lacus. Phasellus tincidunt, dolor a lacinia finibus, arcu mi feugiat quam, at tempor risus ipsum id sem. Nulla nec massa vel magna efficitur vestibulum. Ut nec nisi id orci sollicitudin commodo nec nec purus. Phasellus non tortor risus. Nulla facilisi. Nullam vestibulum tortor vitae eros vestibulum, eget luctus est lobortis. Nullam auctor nec orci in venenatis. Fusce scelerisque ligula ac sapien pharetra, id eleifend enim sodales. Sed ultricies augue ut vehicula faucibus. Aliquam erat volutpat. Pellentesque non dolor eget mi facilisis sollicitudin sed sed felis."

# mengambil kata-kata unik dari kalimat
kosaKata = set(kalimatA.split() + kalimatB.split())

vektor1 = vektor(kalimatA, kosaKata)
vektor2 = vektor(kalimatB, kosaKata)

kesamaan = cosine_similarity(vektor1, vektor2)

print("Cosine Similarity antara kalimat A dan B:", kesamaan)