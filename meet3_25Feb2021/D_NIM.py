'''

DESKRIPSI SOAL

Anda tahu bahwa NIM lengkap di UGM mempunyai format: angkatan/NIU/fakultas/NIF.
Sebagai contoh, jika seorang mahasiswa memiliki NIM 09/123456/SV/98760, maka dia
adalah angkatan 09, memiliki NIU 123456, kuliah di fakultas SV, dan memiliki NIF
98760. Anggap bahwa NIM di UGM pasti memiliki format: 2 karakter angkatan, 6
karakter NIU, 2 karakter fakultas, dan 5 karakter NIF, serta masing-masing
dipisahkan oleh tanda /.

Tugas Anda adalah mencari angkatan, NIU, fakultas, atau NIF dari NIM yang
diberikan. PETUNJUK MASUKAN

Input terdiri atas dua baris. Baris pertama berisi NIM lengkap. Baris kedua
adalah pertanyaan. Pertanyaan adalah salah satu dari "angkatan", "NIU",
"fakultas", atau "NIF". PETUNJUK KELUARAN

Outputkan jawaban dari pertanyaan pada input. CONTOH MASUKAN 1

09/123456/SV/98760 angkatan

CONTOH KELUARAN 1

09

CONTOH MASUKAN 2

09/123456/SV/98760 NIU

CONTOH KELUARAN 2

123456

CONTOH MASUKAN 3

09/123456/SV/98760 fakultas

CONTOH KELUARAN 3

SV

CONTOH MASUKAN 4

09/123456/SV/98760 NIF

CONTOH KELUARAN 4

98760
'''

nim_str_list = input().split('/')
what_to_extract = input()

if what_to_extract == 'angkatan':
    print(nim_str_list[0])
elif what_to_extract == 'NIU':
    print(nim_str_list[1])
elif what_to_extract == 'fakultas':
    print(nim_str_list[2])
elif what_to_extract == 'NIF':
    print(nim_str_list[3])
