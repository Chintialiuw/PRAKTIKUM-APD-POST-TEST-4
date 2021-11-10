#Program Cafe untuk Mengedit Menu
def intro():
    print ("=======================================")
    print ("          Program Cafe ABC123          ")
    print ("=======================================")
    print ("          Silahkan Pilih Menu          ")
    print ("=======================================")
intro ()

list_menu_makanan =[
    ["Kentang Goreng  : Rp. 20000"],
    ["Pisang Keju     : Rp. 15000"],
    ["Roti Bakar      : Rp. 15000"], 
    ["Batagor         : Rp. 20000"],
    ["Siomay          : Rp. 15000"]
]

list_menu_minuman =[
    ["Hazzelnut Chocolate  : Rp. 10000"],
    ["Caramel Latte        : Rp. 15000"],
    ["Air Mineral          : Rp. 5000"], 
    ["Cappucino            : Rp. 15000"],
    ["Es Teh               : Rp. 8000"]
]

def menu():
    print ("1. Menambahkan Menu")
    print ("2. Menghapus Menu")
    print ("3. Mengubah Nama Menu")
    print ("4. Melihat Menu")
    print ("5. Keluar")
    pilih = int(input("Masukkan Pilihan Menu [1, 2, 3, 4 atau 5] : "))
    print ("=======================================")
    if pilih == 1:
        print ("Silahkan Pilih Menu yang ingin ditambahkan")
        print ("A. Menu Makanan")
        print ("B. Menu Minuman")
        tambah = str(input("Masukkan Pilihan Menu [A/B] ? "))
        print ("=======================================")
        if tambah == "A":
            print ("Masukkan Nama Menu yang ingin ditambahkan beserta Harganya")
            print ("[Bakso           : Rp. 20000]")
            tambah_menu = input("")
            print ("=======================================")
            letak = input("Letakkan Tambahan Menu di [Belakang/Tengah] : ")
            print ("=======================================")
            if letak == "Belakang":
                list_menu_makanan.append([tambah_menu])
                for menu_makanan in list_menu_makanan:
                    for makanan in menu_makanan:
                        print(makanan)
            if letak == "Tengah":
                print ("Masukkan Index Menu yang ingin ditambahkan")
                print ("Masukkan Angkanya Saja ! [0, 1, 2, 3, atau 4]")
                tambah = int(input("Masukkan Index Menu : "))
                print ("=======================================")
                list_menu_makanan.insert(tambah, [tambah_menu])
                for menu_makanan in list_menu_makanan:
                    for makanan in menu_makanan:
                        print(makanan)
        if tambah == "B":
            print ("Masukkan Nama Menu beserta Harga")
            print ("[Sprite               : Rp. 5000]")
            tambah_menu = input("")
            print ("=======================================")
            letak = input("Letakkan Tambahan Menu di [Belakang/Tengah] : ")
            print ("=======================================")
            if letak == "Belakang":
                list_menu_minuman.append([tambah_menu])
                for menu_minuman in list_menu_minuman:
                    for minuman in menu_minuman:
                        print(minuman)
            if letak == "Tengah":
                print ("Masukkan Index Menu yang ingin ditambahkan")
                print ("Masukkan Angkanya Saja ! [0, 1, 2, 3, atau 4]")
                tambah = int(input("Masukkan Index Menu : "))
                print ("=======================================")
                list_menu_minuman.insert(tambah, [tambah_menu])
                for menu_minuman in list_menu_minuman:
                    for minuman in menu_minuman:
                        print(minuman)
    elif pilih == 2:
        print ("Silahkan Pilih Menu yang ingin dihapus")
        print ("A. Menu Makanan")
        print ("B. Menu Minuman")
        hapus = str(input("Masukkan Pilihan Menu [A/B] ? "))
        print ("=======================================")
        if hapus == "A":
            print ("Silahkan Pilih Metode Penghapusan")
            print ("A. Menuliskan Nama Menu")
            print ("B. Menuliskan Index Menu")
            metode = input("Masukkan Metode yang dipilih [A/B] : ")
            print ("=======================================")
            if metode == "A":
                print ("Masukkan Nama Menu yang ingin dihapus beserta Harganya")
                print ("Tuliskan Sesuai dengan Menu !")
                hapus_menu = input("")
                print ("=======================================")
                list_menu_makanan.remove([hapus_menu])
                for menu_makanan in list_menu_makanan:
                    for makanan in menu_makanan:
                        print(makanan)
            elif metode == "B":
                print ("Masukkan Index Menu yang ingin dihapus")
                print ("Masukkan Angkanya Saja ! [0, 1, 2, 3, atau 4]")
                hapus = int(input("Masukkan Index Menu : "))
                print ("=======================================")
                del list_menu_makanan[hapus]
                for menu_makanan in list_menu_makanan:
                    for makanan in menu_makanan:
                        print(makanan)
        elif hapus == "B":
            print ("Silahkan Pilih Metode Penghapusan")
            print ("A. Menuliskan Nama Menu")
            print ("B. Menuliskan Index Menu")
            metode = input("Masukkan Metode yang dipilih [A/B] : ")
            print ("=======================================")
            if metode == "A":
                print ("Masukkan Nama Menu yang ingin dihapus beserta Harganya")
                print ("Tuliskan Sesuai dengan Menu !")
                hapus_menu = input("")
                print ("=======================================")
                list_menu_minuman.remove([hapus_menu])
                for menu_minuman in list_menu_minuman:
                    for minuman in menu_minuman:
                        print(minuman)
            elif metode == "B":
                print ("Masukkan Index Menu yang ingin dihapus")
                print ("Masukkan Angkanya Saja ! [0, 1, 2, 3, atau 4]")
                hapus = int(input("Masukkan Index Menu : "))
                print ("=======================================")
                del list_menu_minuman[hapus]
                for menu_minuman in list_menu_minuman:
                    for minuman in menu_minuman:
                        print(minuman)
    elif pilih == 3:
        print ("Silahkan Pilih Menu yang ingin dihapus")
        print ("A. Menu Makanan")
        print ("B. Menu Minuman")
        ubah = str(input("Masukkan Pilihan Menu [A/B] ? "))
        print ("=======================================")
        if ubah == "A":
            print ("Masukkan Nama Menu pengganti beserta Harganya")
            print ("[Bakso           : Rp. 20000]")
            ubah_nama_menu = input("")
            print ("=======================================")
            print ("Masukkan Index Menu yang ingin digantikan")
            print ("Masukkan Angkanya Saja ! [0, 1, 2, 3, atau 4]")
            ubah_nama = int(input("Masukkan Index Menu : "))
            print ("=======================================")
            list_menu_makanan[ubah_nama] = [ubah_nama_menu]
            for menu_makanan in list_menu_makanan:
                for makanan in menu_makanan:
                    print(makanan)
        if ubah == "B":
            print ("Masukkan Nama Menu pengganti beserta Harganya")
            print ("[Sprite               : Rp. 5000]")
            ubah_nama_menu = input("")
            print ("=======================================")
            print ("Masukkan Index Menu yang ingin digantikan")
            print ("Masukkan Angkanya Saja ! [0, 1, 2, 3, atau 4]")
            ubah_nama = int(input("Masukkan Index Menu : "))
            print ("=======================================")
            list_menu_minuman[ubah_nama] = [ubah_nama_menu]
            for menu_minuman in list_menu_minuman:
                for minuman in menu_minuman:
                    print(minuman)
    elif pilih == 4:
        print ("Silahkan Pilih Menu yang ingin dilihat")
        print ("A. Menu Makanan")
        print ("B. Menu Minuman")
        lihat = str(input("Masukkan Pilihan Menu [A/B] ? "))
        print ("=======================================")
        if lihat == "A":
            for menu_makanan in list_menu_makanan:
                for makanan in menu_makanan:
                    print(makanan)
            print ("=======================================")
            jawab = str(input("Ingin Kembali ke Menu [y/t] ? "))
            if jawab == "y":
                menu()
            elif jawab == "t":
                exit()
        elif lihat == "B":
            for menu_minuman in list_menu_minuman:
                for minuman in menu_minuman:
                    print(minuman)
            print ("=======================================")
            jawab = str(input("Ingin Kembali ke Menu [y/t] ? "))
            if jawab == "y":
                menu()
            elif jawab == "t":
                exit()
    elif pilih == 5:
        exit()
menu()