import csv
import os

FILENAME = 'pengunjung.csv'

# Patikan file ada
def load_data_pengunjung():
    data_pengunjung = {}

    try:
        with open(FILENAME, mode='r') as pengunjung_file:
            reader = csv.reader(pengunjung_file)
            for row in reader:
                id_pengunjung = row[0]
                nama_pengunjung = row[1]
                no_hp = row[2]
                instansi = row[3]

                # simpan data pengunjung dalam bentuk dictionary
                data_pengunjung[id_pengunjung] = {
                    'nama' : nama_pengunjung,
                    'no_hp' : no_hp,
                    'instansi' : instansi
                }
    except FileNotFoundError:
        print(f'File {FILENAME} tidak ditemukan.')
    return data_pengunjung 

# Tampilkan Daftar Pengunjung
def tampilkan_pengunjung():
    print('\n============== Daftar Pengunjung ==============')
    if not os.path.exists(FILENAME):
        print('Pengunjung Kosong')
        return
    with open(FILENAME, mode='r') as pengunjung_file:
        reader = csv.reader(pengunjung_file)
        print(f'{"ID":<5} | {"Nama Pengunjung":<20} | {"No HP":<15} | {"Instansi":<20}')
        print('-' * 70)
        for row in reader:
            print(f'{row[0]:<5} | {row[1]:<20} | {row[2]:<15} | {row[3]:<20} ')

# Tambah Pengunjung Baru
def tambah_pengunjung():
    print('\n===== Tambah Pengunjung Baru =====')
    id_pengunjung = input('Masukkan ID Pengunjung : ').upper()
    nama_pengunjung = input('Masukkan Nama Pengunjung : ')
    no_hp = input('Masukkan No HP Pengunjung : ')
    instansi = input('Masukkan Instansi Pengunjung : ')
    
    # Tulis data pengunjung ke file CSV
    with open(FILENAME, mode='a', newline='') as pengunjung_file:
        writer = csv.writer(pengunjung_file)
        writer.writerow([id_pengunjung, nama_pengunjung, no_hp, instansi])
        print('Pengunjung Berhasi Ditambahkan!\n')

# Hapus Pengunjung
def hapus_pengunjung():
    print('\n===== Hapus Pengunjung =====')
    tampilkan_pengunjung()
    kode_pengunjung = input('Masukkan ID Pengunjung yang ingin dihapus : ').upper()

    data_sementara = []
    ketemu = False

    try:
        with open(FILENAME, mode='r') as pengunjung_file:
            reader = csv.reader(pengunjung_file)
            for row in reader:
                if row[0] == kode_pengunjung:
                    ketemu = True
                    print('Pengunjung Berhasil Dihapus!\n')
                    continue # Lewatkan baris yang akan dihapus
                data_sementara.append(row)
    except FileNotFoundError:
        print('File tidak ditemukan.')
        return 

    # Tulis ulang data tanpa pengunjung yang dihapus
    if ketemu:
        konfirmasi = input('Apakah Anda yakin ingin menghapus pengunjung ini? {y/n} : ').lower()
        if konfirmasi == 'y':
            with open(FILENAME, mode='w', newline='') as pengunjung_file:
                writer = csv.writer(pengunjung_file)
                writer.writerows(data_sementara)
                print('Data sudah dihapus permanen!\n')
        else:
            print('Penghapusan dibatalkan.\n')
    else:
        print('ID Pengunjung tidak ditemukan.\n')

