import csv
import os

FILENAME = 'data_paket.csv'

# Pastikan file ada
def load_data_paket():
    data_paket = []

    try:
        with open(FILENAME, mode='r') as paket_file:
            reader = csv.reader(paket_file)
            for row in reader:
                id_paket = row[0]
                nama_paket = row[1]
                jenis = row[2]
                min_per_orang = row[3]
                kapasitas = row[4]
                durasi = row[5]
                harga_sewa = row[6]

                # Simpan data paket dalam bentuk dictionary
                data_paket[id_paket] = {
                    'nama' : nama_paket,
                    'jenis' : jenis,
                    'min_per_orang' : min_per_orang,
                    'kapasitas' : kapasitas,
                    'durasi' : durasi,
                    'harga_sewa'  : harga_sewa
                }
    except FileNotFoundError:
        print(f'File {FILENAME} tidak ditemukan.')
    return data_paket 

# Tampilkan Daftar Paket
def tampilkan_paket():
    print('\n============== Daftar Paket ==============')
    if not os.path.exists(FILENAME):
        print('Paket Kosong')
        return 
    with open(FILENAME, mode='r') as paket_file:
        reader = csv.reader(paket_file)
        print(f'{"ID":<5} | {"Nama Paket":<20} | {"Jenis":<10} | {"Min Pesanan/Orang":<12} | {"Kapasitas":<10} | {"Durasi (jam)":<12} | {"Harga Sewa":>12}')
        print('=' * 95)
        for row in reader:
            print(f'{row[0]:<5} | {row[1]:<20} | {row[2]:<10} | Rp {int(row[3]):<14,} | {row[4]:<10} | {row[5]:<12} | Rp {int(row[6]):,}')

# Tambah Paket Baru
def tambah_paket():
    print('\n===== Tambah Paket Baru =====')
    id_paket = input('Masukkan ID Paket : ').upper()
    nama_paket = input('Masukkan Nama Paket : ')
    jenis = input('Masukkan jenis Paket (sewa/non sewa) : ')
    min_per_orang = input('Minimum / Orang (isi 0 jika sewa): ')
    kapasitas = input('Masukkan Kapasitas Paket : ')
    durasi = input('Masukkan Durasi Paket (jam) : ')
    harga_sewa = int(input('Masukkan Harga Sewa Paket (Masukkan 0 jika non sewa): '))

    # Tulis data paket ke file CSV
    with open(FILENAME, mode='a', newline='') as paket_file:
        writer = csv.writer(paket_file)
        writer.writerow([id_paket, nama_paket, jenis, min_per_orang, kapasitas, durasi, harga_sewa])
        print('Paket Berhasil Ditambahkan!\n')

# Update Paket
def update_paket():
    print('\n===== Update Paket =====')
    tampilkan_paket()

    kode_paket = input('Masukkan ID Paket yang ingin diupdate : ').upper()

    # Baca semua data ke memory
    data_sementara = []
    ketemu = False

    try: 
        with open(FILENAME, mode='r') as paket_file:
            reader = csv.reader(paket_file)
            for row in reader:
                if row[0] == kode_paket:
                    print(f'Data Lama => Nama Paket : {row[1]}, Jenis : {row[2]}, Min Pesanan/Orang : {row[3]}, Kapasitas : {row[4]}, Durasi (jam) : {row[5]}, Harga Sewa : {row[6]}')
                    print('Silahkan masukkan data baru (tekan enter jika tidak ingin mengubah data lama) : ')

                    nama_baru = input('Masukkan Nama Paket Baru : ')
                    jenis_baru = input('Masukkkan Jenis Paket Baru (sewa/non sewa) : ')
                    min_per_orang_baru = input('Masukkan Minimum Pesanan/Orang Baru : ')
                    kapasitas_baru = input('Masukkan Kapasitas Paket Baru : ')
                    durasi_baru = input('Masukkan Durasi Paket Baru (jam) : ')
                    harga_baru = input('Masukkan Harga Sewa Paket Baru : ')


                    # Logika jika input kosong, maka data lama  dipertahankan
                    if len(nama_baru) > 0:
                        row[1] = nama_baru
                    if len(jenis_baru) > 0:
                        row[2] = jenis_baru
                    if len(min_per_orang_baru) > 0:
                        row[3] = min_per_orang_baru
                    if len(kapasitas_baru) > 0:
                        row[4] = kapasitas_baru
                    if len(durasi_baru) > 0:
                        row[5] = durasi_baru
                    if len(harga_baru) > 0:
                        row[6] = harga_baru
                    
                    ketemu = True
                    print('Paket Berhasil Diupdate!\n')
                    
                # Memasukkan row baik yang diupdate maupun yang tidak ke data sementara
                data_sementara.append(row)
    except FileNotFoundError:
        print('File tidak ditemukan.')
        return
    
    # Tulis ulang semua data dari memory ke file CSV
    if ketemu:
        with open(FILENAME, mode='w', newline='') as paket_file:
            writer = csv.writer(paket_file)
            writer.writerows(data_sementara)
        print('File CSV berhasil diupdate.\n')
    else:
        print('ID Paket tidak ditemukan.\n')

# Hapus Paket
def hapus_paket():
    print('\n===== Hapus Paket =====')
    tampilkan_paket()

    kode_paket = input('Masukkan ID Paket yang ingin dihapus : ').upper()

    data_sementara = []
    ketemu = False

    try:
        with open(FILENAME, mode='r') as paket_file:
            reader = csv.reader(paket_file)
            for row in reader:
                if row[0] == kode_paket:
                    ketemu = True
                    print(f'Paket dengan ID {kode_paket} berhasil dihapus!\n')
                    continue # Lewatkan baris yang akan dihapus
                data_sementara.append(row)
    except FileNotFoundError:
        print('File tidak ditemukan.')
        return
    
# Tulis ulang semua data dari memory ke file CSV
    if ketemu:
        konfirmasi = input('Apakah Anda yakin ingin menghapus paket ini? (y/n) : ').lower()
        if konfirmasi == 'y':
            with open(FILENAME, mode='w', newline='') as paket_file:
                writer = csv.writer(paket_file)
                writer.writerows(data_sementara)
                print('Data berhasil dihapus permanen!\n')
    else:
        print('ID Paket tidak ditemukan.\n')


           