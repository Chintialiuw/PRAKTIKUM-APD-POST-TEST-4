#Program Menu Cafe Sederhana
def intro():
    print ("=======================================")
    print ("          Program Cafe ABC123          ")
    print ("=======================================")
    print ("Silahkan Pilih Menu")
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

def menu_makanan():
    for menu_makanan in list_menu_makanan:
        for makanan in menu_makanan:
            print(makanan)
    print ("=======================================")

def menu_minuman():
    for menu_minuman in list_menu_minuman:
        for minuman in menu_minuman:
            print(minuman)
    print ("=======================================")

jawab = "y"
while jawab == "y":
    print ("A. Menu Makanan")
    print ("B. Menu Minuman")
    pilihan = str(input("Masukkan Pilihan Menu [A/B] : "))
    print ("=======================================")
    if pilihan == "A":
        menu_makanan()
    elif pilihan == "B":
        menu_minuman()
    jawab = input("Apakah Anda Ingin Melihat Menu Kembali [y/t] ? ")