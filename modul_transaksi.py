import csv
import datetime
import os

FILENAME = 'data_transaksi.csv'

# Pastikan file ada
def init_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file_transaksi:
            writer = csv.writer(file_transaksi)
            writer.writerow(['id_transaksi', 'tanggal', 'id_pengunjung', 'id_paket', 'jenis_paket', 'jumlah_orang', 'item_menu', 'total'])

# lookup paket berdasarkan id_paket
def lookup_paket(id_paket):
    with open('data_paket.csv', mode='r') as file_paket:
        reader = csv.reader(file_paket)
        for row in reader:
            if row[0] == id_paket:
                return row
    return None

# lookup menu berdasarkan id_menu
def lookup_menu(id_menu):
    with open('data_menu.csv', mode='r') as file_menu:
        reader = csv.reader(file_menu)
        for row in reader:
            if row[0] == id_menu:
                return int(row[2])
    return 0

# Transaksi Kunjungan
def transaksi_kunjungan():
    init_file()
    id_transaksi = datetime.datetime.now().strftime('T%y%m%d%H%M%S')
    tanggal = datetime.date.today().isoformat()
    id_pengunjung = input('Masukkan ID Pengunjung : ').upper()
    id_paket = input('Masukkan ID Paket : ').upper()
    jumlah_orang = int(input('Masukkan Jumlah Orang : '))

    paket = lookup_paket(id_paket)
    if not paket:
        print('Paket tidak ditemukan!')
        return
    jenis_paket = paket[2]
    total = 0
    item_menu = ''

    if jenis_paket == 'non sewa' :
        min_per_orang = int(paket[3])
        min_total = min_per_orang * jumlah_orang
        print(f'Minimum Pesanan : Rp {min_total:,}')
        items = input('Masukkan ID Menu yang dipesan (pisahkan dengan koma) : ').strip().upper()
        item_ids = [x.strip() for x in items.split(',') if x.strip()]
        item_menu = ';'.join(item_ids)
        for mid in item_ids:
            total += lookup_menu(mid)
        if total < min_total:
            print(f'Total Rp {total:,} kurang dari minimum pesanan Rp {min_total:,}. Transaksi dibatalkan.')
            return
    else:
        total = int(paket[6])

    # Simpan data transaksi ke file CSV
    with open(FILENAME, mode='a', newline='') as file_transaksi:
        writer = csv.writer(file_transaksi)
        writer.writerow([id_transaksi, tanggal, id_pengunjung, id_paket, jenis_paket, jumlah_orang, item_menu, total])
    print(f'Transaksi berhasi! Total yang harus dibayar : Rp {total:,}')


transaksi_kunjungan()