"""
Program Menghitung Luas Segitiga
luas_segitiga = alas * tinggi /2
"""

print('\nMenghitung Luas Segitiga')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi /2
print('segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}')

print('\nMenghitung Luas Segitiga dg Copypaste')
alas = 20
tinggi = 2
luas_segitiga = alas * tinggi /2
print('segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}')

print('\nMembuat fungsi hitung_luas_segitiga')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print('Menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(10, 6)}')
print('Menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(20, 2)}')
print('Menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(100, 2)}')
print('Dengan fungsi, segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas= {hitung_luas_segitiga(alas, tinggi)}')


