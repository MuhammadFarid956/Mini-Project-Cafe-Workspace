import profil
import master_data
import modul_transaksi

def main_menu():
    while True:
        print('\n=== Cafe and Workspace ===')
        print('1. Profil Mahasiswa')
        print('2. Master Data')
        print('3. Menu Transaksi')
        print('4. Keluar')
        pilih = input('Silahkan Pilih (1/2/3) : ')

        if pilih == '1':
            profil.profil_mahasiswa()
        elif pilih == '2':
            master_data.master_data()
        elif pilih == '3':
            print('\n===== Transaksi =====')
            print('\n1. Cashier\n2. Laporan Transaksi\n3. Kembali')
            pilih = input('Silahkan Pilih (1/2/3)')
            if pilih == '1':
                modul_transaksi.transaksi_kunjungan()
            elif pilih == '2':
                modul_transaksi.tampilkan_transaksi()
            elif pilih == '3':
                continue
            else:
                print('Input Salah, silahkan coba lagi!')
                continue  
        elif pilih == '4':
            print('Terimakasih, Sampai Jumpa.')
            break
        else:
            print('Input Tidak Valid!')

main_menu()