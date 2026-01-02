# Master data menu, paket, dan pengunjung
import modul_menu
import modul_paket
import modul_pengunjung

def master_data():
    try:
        while True:
            print('\n===== Master Data =====')
            print('1. Menu\n2. Paket\n3. Pengunjung\n4. Kembali ke Menu Utama')
            pilihan = input('Pilih Master Data yang ingin diakses (1-4) : ')
            if pilihan == '1':
                print('\n===== Master Menu =====')
                print('1. Tampilkan Menu\n2. Tambah Menu\n3. Update Menu\n4. Hapus Menu\n5. Kembali\n')
                pilih = input('Pilih Master Menu (1/2/3/4/5) : ')
                if pilih == '1':
                    modul_menu.tampilkan_menu()
                elif pilih == '2':
                    modul_menu.tambah_menu()
                elif pilih == '3':
                    modul_menu.update_menu()
                elif pilih == '4':
                    modul_menu.hapus_menu()
                elif pilih == '5':
                    continue
                else:
                    print('Input tidak valid, silahkan input (1/2/3/4/5)!')
            if pilihan == '2':
                print('\n===== Master Paket =====')
                print('1.Tampilkan Paket\n2. Tambah Paket\n3. Update Paket\n4. Hapus Paket\n5. Kembali')
                pilih = input('Pilih Master Paket (1/2/3/4/5) : ')

                if pilih == '1':
                    modul_paket.tampilkan_paket()
                elif pilih == '2':
                    modul_paket.tambah_paket()
                elif pilih == '3':
                    modul_paket.update_paket()
                elif pilih == '4':
                    modul_paket.hapus_paket()
                elif pilih == '5':
                    continue
                else:
                    print('Input tidak valid, silahkan input (1/2/3/4/5) : ')
            if pilihan == '3':
                print('\n===== Master Pengunjung =====')
                print('1. Tampilkan Pengunjung\n2. Tambah Pengunjung\n3. Hapus Pengunjung\n4. Kembali')
                pilih = input('Pilih Master Pengunjung (1/2/3/4) : ')
                if pilih == '1':
                    modul_pengunjung.tampilkan_pengunjung()
                elif pilih == '2':
                    modul_pengunjung.tambah_pengunjung()
                elif pilih == '3':
                    modul_pengunjung.hapus_pengunjung()
                elif pilih == '4':
                    continue
                else:
                    print('Input tidak valid, silahkan input (1/2/3/4) : ')
            elif pilihan == '4':
                return
            else:
                print('Input tidak valid, silahkan input (1/2/3/4) : ')                
    except ValueError:
        print('Input tidak valid! tes')
        return

master_data()