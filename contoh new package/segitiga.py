print('\nMenghitung Luas Segitiga dg Copypaste')
alas = 20
tinggi = 2
luas_segitiga = alas * tinggi /2
print(f'segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}')

print('\nMembuat fungsi hitung_luas_segitiga')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print(f'Menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(10, 6)}')
print(f'Menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(20, 2)}')
print(f'Menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(100, 2)}')
print(f'Dengan fungsi, segitiga dengan alas={alas} dan tinggi{tinggi} memiliki luas {hitung_luas_segitiga(alas, tinggi)}')
