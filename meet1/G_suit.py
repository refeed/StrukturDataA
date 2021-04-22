"""
PETUNJUK MASUKAN

Dua baris simbol yang terdiri dari dua karakter: [] = Kertas, () = Batu, 8< =
Gunting. Baris Pertama adalah simbol yang dipilih Pak Blangkon dan baris kedua
adalah simbol yang dipilih Pak Semar. PETUNJUK KELUARAN

Pemenang suit. "Blangkon" atau "Semar" atau "Seri".

"""

blangkon = input().strip()
semar = input().strip()

BATU_STR = '()'
GUNTING_STR = '8<'
KERTAS_STR = '[]'

BLANKGON_STR = 'Blangkon'
SEMAR_STR = 'Semar'

if semar == blangkon:
    print('Seri')
elif semar == BATU_STR:
    if blangkon == GUNTING_STR:
        print(SEMAR_STR)
    elif blangkon == KERTAS_STR:
        print(BLANKGON_STR)
elif semar == GUNTING_STR:
    if blangkon == KERTAS_STR:
        print(SEMAR_STR)
    elif blangkon == BATU_STR:
        print(BLANKGON_STR)
elif semar == KERTAS_STR:
    if blangkon == BATU_STR:
        print(SEMAR_STR)
    elif blangkon == GUNTING_STR:
        print(BLANKGON_STR)
