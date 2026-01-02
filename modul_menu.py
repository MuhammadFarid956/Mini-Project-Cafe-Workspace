import csv
import os

FILENAME = 'data_menu.csv'

def load_data_menu():
    data_menu = {}

    try:
        with open(FILENAME, mode='r',) as menu_file:
            reader = csv.reader(menu_file)
            for row in reader:
                id_menu = row[0]
                nama_menu = row[1]
                harga_menu = row[2]

                # Simpan data menu dalam bentuk dictionary
                data_menu[id_menu] = { 'nama' : nama_menu, 'harga' : harga_menu}
    except FileNotFoundError:
        print(f'File {FILENAME} tidak ditemukan.')
    return data_menu

# Generate ID Menu 
def next_id_menu():
    last_num = 0
    try:
        with open(FILENAME, mode='r') as menu_file:
            reader = csv.reader(menu_file)
            next(reader, None) #Skip Heade
            for row in reader:
                kode = row[0]
                if kode.startswith('M'):
                    num = int(kode.replace('M',''))
                    if num > last_num:
                        last_num = num
    except FileNotFoundError:
        pass
    return f'M{last_num+1:03d}'

# Tampilkan Menu
def tampilkan_menu():
    print('\n============== Daftar Menu ==============')
    if not os.path.exists(FILENAME):
        print('Menu Kosong')
        return
    with open(FILENAME, mode='r') as menu_file:
        reader = csv.reader(menu_file)
        print(f'{"ID":<5} | {"Nama Menu":<20} | {"Harga":>10}')
        print('-' * 41)
        for row in reader:
            print(f'{row[0]:<5} | {row[1]:<20} | Rp {int(row[2]):,}')

# Tambah Menu
def tambah_menu():
    while True:
        print('\n===== Tambah Menu Baru =====')
        id_menu = next_id_menu()
        nama_menu = input('Masukkan Nama Menu : ')
        if not nama_menu:
            print('Nama menu tidak boleh kosong')
            continue
        harga_menu = int(input('Masukkan Harga Menu : '))
        if len(harga_menu <0):
            print('harga tidak boleh kosong')

        # Tulis data menu ke file CSV
        with open(FILENAME, mode='a', newline='') as menu_file:
            writer = csv.writer(menu_file)
            writer.writerow([id_menu, nama_menu, harga_menu])
        print('Menu Berhasil Ditambahkan!\n')

def update_menu():
    print('\n===== Update Menu =====')
    tampilkan_menu()
    
    kode_menu = input('Masukkan ID Menu yang ingin diupadete : ').upper()

    # Baca semua data ke memory
    data_sementara = []
    ketemu = False

    try:
        with open(FILENAME, mode='r') as menu_file:
            reader = csv.reader(menu_file)
            for row in reader:
                # validasi kode_menu
                if row[0] == kode_menu:
                    print(f'Data Lama => Nama Menu : {row[1]}, Harga : {row[2]}')
                    print('Silahkan masukkan data baru (tekan enter jika tidak ingin mengubah data lama) : ')

                    nama_baru = input('Masukkan Nama Menu Baru : ')
                    harga_baru = input('Masukkan Harga Menu Baru : ')

                    # Logika jika input kosong, maka data lama  dipertahankan
                    if len(nama_baru) > 0:
                        row[1] = nama_baru
                    if len(harga_baru) > 0:
                        row[2] = harga_baru

                    ketemu = True
                    print('Menu Berhasil Diupdate!\n')
                    
                # Memasukkan row baik yang diupdate maupun yang tidak ke data sementara
                data_sementara.append(row)
    except FileNotFoundError:
        print('File tidak ditemukan.')
        return

    # Tulis ulang semua data dari memory ke file CSV
    if ketemu:
        with open(FILENAME, mode='w', newline='') as menu_file:
            writer = csv.writer(menu_file)
            writer.writerows(data_sementara)
        print('File CSV berhasil diupdate.\n')
    else:
        print('ID Menu tidak ditemukan.\n')
        

def hapus_menu():
    print('\n===== Hapus Menu =====')
    tampilkan_menu()

    kode_menu = input('Masukkan ID Menu yang ingin dihapus : ').upper()

    data_sementara = []
    ketemu = False

    try:
        with open(FILENAME, mode='r') as menu_file:
            reader =csv.reader(menu_file)
            for row in reader:
                if row[0] == kode_menu:
                    # Jika ID Menu ditemukan, tandai sebagai ketemu dan lewati penambahan ke data_sementara
                    ketemu = True
                    print(f'Menu dengan ID {kode_menu} berhasil dihapus.\n')
                    continue
                data_sementara.append(row)
    except FileNotFoundError:
        print('File tidak ditemukan.')
        return

# Tulis ulang semua data dari memory ke file CSV
    if ketemu:
        konfirmasi = input('Apakah Anda yakin ingin menghapus menu ini? (y/n) : ').lower()
        if konfirmasi == 'y':
            with open(FILENAME, mode='w', newline='') as menu_file:
                writer = csv.writer(menu_file)
                writer.writerows(data_sementara)
            print('Data berhasil dihapus permanen!\n')
        else:
            print('Penghapusan dibatalkan.\n')
    else:
        print('ID Menu tidak ditemukan.\n')

tambah_menu()