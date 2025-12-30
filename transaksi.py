import csv
import datetime

FILENAME = 'laporan_transaksi.csv'

# pastikan file ada
def load_data_transaksi():
    data_transaksi = {}

    try:
        with open(FILENAME, mode='r') as transaksi_file:
            reader = csv.reader(transaksi_file)
            for row in reader:
                id_transaksi = row[0]
                tanggal = row[1]
                id_pengunjung = row[2]
                id_paket = row[3]
                jenis_paket = row[4]
                jumlah_orang = row[5]
                menu_item = row[6]
                total = row[7]

                # simpan data transaksi dalam bentuk dictionary
                data_transaksi[id_transaksi] = {
                    'tanggal' : tanggal,
                    'id_pengunjung' : id_pengunjung,
                    'id_paket' : id_paket,
                    'jenis_paket' : jenis_paket,
                    'jumlah_orang' : jumlah_orang,
                    'menu_item' : menu_item,
                    'total' : total
                }
    except FileNotFoundError:
        print(f'File {FILENAME} tidak ditemukan.')
    return 

# lookup paket
def lookup_paket(id_paket):
    with open('data_paket.csv', mode='r') as paket_file:
        reader = csv.reader(paket_file)
        for row in reader:
            if row[0] == id_paket:
                return row
    return None

# Lookup menu 
def lookup_menu(id_menu):
    with open('data_menu.csv', mode='r') as menu_file:
        reader = csv.reader(menu_file)
        for row in reader:
            if row[0] == id_menu:
                return row
    return None 

# Transaksi Kunjungan 
def transaksi_kunjungan():
    id_transaksi = datetime.datetime.now().strftime('T%y%m%d%H%M%S')
    tanggal = datetime.date.today().isoformat()
    id_pengungjung = input("ID Pengunjung : ").upper()
    id_paket = input("ID Paket : ").upper()
    jumlah_orang = int(input("Jumlah Orang : "))

    paket = lookup_paket(id_paket)
    if not paket:
        print('Paket tidak ditemukan!')
        return 
    
    jenis = paket[2]
    total = 0
    menu_item = ""
    if jenis == 'non_sewa':
        min_per_orang = int(paket['min_per_orang'])
        min_total = min_per_orang * jumlah_orang
        print(f'Minimum Pesanan untuk {jumlah_orang} orang adalah {min_per_orang}/Orang ')
        items = input('Masukkan ID Menu yang dipesan (pisahkan dengan koma jika lebih dari satu) : ').strip()
        item_ids = [item.strip() for item in items.split(',') if item.strip()]
        item_menu = ','.join(item_ids)
        for mid in item_ids:
            total += int(lookup_menu(mid))
        if total < min_per_orang * jumlah_orang:
            print(f'Total {total} pesanan kurang dari {min_total}. Transaksi dibatalkan.')
            return
    else:
        total = int

    # simpan data transaksi ke file CSV
    with open(FILENAME, mode='a', newline='') as transaksi_file:
        writer = csv.writer(transaksi_file)
        writer.writerow([
        id_transaksi,
        tanggal,
        id_pengungjung,
        id_paket,
        jenis,
        jumlah_orang,
        item_menu,
        total
        ])

transaksi_kunjungan()