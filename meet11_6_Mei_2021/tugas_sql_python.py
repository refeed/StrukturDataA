import mysql.connector

CONFIG = {
    'user': 'refeed',
    'password': 'wikimedia',
    'host': '127.0.0.1',
    # 'database': 'Tugas_2_Rafid_Aslam'
}

cnx = mysql.connector.connect(**CONFIG)

cursor = cnx.cursor()

def print_wishlist_table():
    print('========================')
    print('Isi dari tabel Wishlist:')
    print('========================')
    cursor.execute('SELECT * FROM Wishlist')
    for row in cursor:
        print(row)
    print()

# Membuat database
cursor.execute('CREATE DATABASE IF NOT EXISTS Tugas_2_Rafid_Aslam')
cursor.execute('USE Tugas_2_Rafid_Aslam')

# Membuat table Wishlist
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS Wishlist (
        id INT PRIMARY KEY AUTO_INCREMENT,
        nama_produk VARCHAR(250) NOT NULL,
        jumlah INT NOT NULL,
        total_harga INT NOT NULL,
        link_produk VARCHAR(500) NOT NULL
    )
    '''
)

products = (
    {
        'nama_produk': 'Logitech MK240 / MK 240 Wireless Combo Mouse & Keyboard - Putih',
        'jumlah': 1,
        'total_harga': 247500,
        'link_produk': 'https://www.tokopedia.com/suryaecomm/logitech-mk240-mk-240-wireless-combo-mouse-keyboard-putih',
    },
    {
        'nama_produk': 'Trickle Filter Kolam ikan KOI - 3 Susun Small Hijau - Dakron Super',
        'jumlah': 1,
        'total_harga': 745000,
        'link_produk': 'https://www.tokopedia.com/ottenfilterkolam/trickle-filter-kolam-ikan-koi-3-susun-small-hijau-dakron-super',
    },
    {
        'nama_produk': 'Si Cacing dan Kotoran Kesayangannya 123',
        'jumlah': 2,
        'total_harga': 136000 * 2,
        'link_produk': 'https://www.tokopedia.com/waroengjuandos/si-cacing-dan-kotoran-kesayangannya-123?whid=0',
    },
    {
        'nama_produk': 'Cougar MG120 MG120-G Casing PC micro ATX',
        'jumlah': 1,
        'total_harga': 485000,
        'link_produk': 'https://www.tokopedia.com/zcompbandung/cougar-mg120-mg120-g-casing-pc-micro-atx?whid=0',
    },
    {
        'nama_produk': 'Xiaomi Mi Band 6 Original Miband 6 Smartband Amoled SpO2 Garansi Resmi - Garansi Distrib, China Version',
        'jumlah': 2,
        'total_harga': 628000 * 2,
        'link_produk': 'https://www.tokopedia.com/miofficialonline/xiaomi-mi-band-6-original-miband-6-smartband-amoled-spo2-garansi-resmi-garansi-distrib-china-version?whid=0',
    },
)

for product in products:
    cursor.execute('''
        INSERT INTO Wishlist (nama_produk, jumlah, total_harga, link_produk)
        VALUES (%s, %s, %s, %s)
    ''',
    (product['nama_produk'], product['jumlah'],
    product['total_harga'], product['link_produk'])
    )
    cnx.commit()

print('Setelah INSERT')
print_wishlist_table()

price_rows = []
cursor.execute('SELECT id, jumlah, total_harga FROM Wishlist')
for row in cursor:
    price_rows.append(row)

# Mengupdate jumlah dan total harga masing-masing harga menjadi dua kali lipat
for price_row in price_rows:
    cursor.execute(
        'UPDATE Wishlist SET jumlah=%s, total_harga=%s WHERE id=%s',
        (price_row[1]*2, price_row[2]*2, price_row[0]))
    cnx.commit()

print('Setelah UPDATE')
print_wishlist_table()

# Menghapus item yang memiliki total_harga lebih dari 750 ribu
cursor.execute('DELETE FROM Wishlist WHERE total_harga > 750000')
cnx.commit()

print('Setelah DELETE')
print_wishlist_table()

cnx.close()
