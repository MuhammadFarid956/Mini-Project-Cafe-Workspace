import profil
import master_data
import modul_transaksi

def main_menu():
    while True:
        print('\n=== Cafe and Workspace ===')
        print('1. Profil Mahasiswa')
        print('2. Master Data')
        print('3. Transaksi')
        print('4. Keluar')
        pilih = input('Silahkan Pilih (1/2/3) : ')

        if pilih == '1':
            profil.profil_mahasiswa()
        elif pilih == '2':
            master_data.master_data()
        elif pilih == '3':
            modul_transaksi.transaksi_kunjungan()
        elif pilih == '4':
            print('Terimakasih, Sampai Jumpa.')
            break
        else:
            print('Input Tidak Valid!')

main_menu()
