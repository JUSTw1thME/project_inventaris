# project_inventaris
class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

inventaris = []

while True:
    print("===== Manajemen Inventaris =====")
    print('1. Tambah Produk Baru')
    print('2. Lihat Semua produk')
    print('3. Update Stok')
    print('4. keluar')

    menu = int(input('Masukan No Menu :'))
    if menu == 1:
        print('==== Menu Tambah Produk ====')
        nama_produk = input('Masukan nama produk :')
        harga_produk = int(input('Masukan harga produk :'))
        stok_produk = int(input('Masukan stok produk :'))
        data_produk = Produk(nama_produk, harga_produk, stok_produk)
        inventaris.append(data_produk)
    elif menu == 2:
        print('==== Menu List Produk ====')
        if not inventaris:
            print('Produk Kosong')
        else:
            no = 1
            for produk in inventaris:
                print(f"{no}. {produk.nama} - Rp{produk.harga} - stok: {produk.stok}")
                no += 1
    elif menu == 3:
        print("==== Menu Update Stok Produk ====")
        print('1. Menambah Stok')
        print('2. Mengurangi stok')
        update_stok = int(input('Pilih menu apa :'))
        if update_stok == 1:
            while True:
                no = 1
                for produk in inventaris:
                    print(f"{no}. {produk.nama} - stok: {produk.stok}")
                    no += 1
                try:
                    menambah_stok = int(input("Masukan nomer produk :"))
                except ValueError:
                    print('Masukan no produk yang tersedia')
                    continue
                no_produk = menambah_stok - 1
                produk_dipilih = inventaris[no_produk]
                try:
                    tambah_stok = int(input(f"Masukan jumlah stok {produk_dipilih.nama} ditambah :"))
                except ValueError:
                    print('Input tidak valid')
                    continue
                produk_dipilih.stok += tambah_stok
                print(f"Produk {produk_dipilih.nama} telah ditambahkan sebanyak {tambah_stok}")
                print(f"Jumlah stok {produk_dipilih.nama} : {produk_dipilih.stok}")
                break
        elif update_stok == 2:
            while True:
                no = 1
                for produk in inventaris:
                    print(f"{no}. {produk.nama} - stok: {produk.stok}")
                    no += 1
                try:
                    mengurangi_stok = int(input("Masukan nomer produk :"))
                except ValueError:
                    print('Masukan no produk yang tersedia')
                    continue
                no_produk = mengurangi_stok - 1
                produk_dipilih = inventaris[no_produk]
                try:
                    kurangi_stok = int(input(f"Masukan jumlah stok {produk_dipilih.nama} dikurangi :"))
                except ValueError:
                    print('Input tidak valid')
                    continue
                produk_dipilih.stok -= kurangi_stok
                print(f"Produk {produk_dipilih.nama} telah dikurangi sebanyak {kurangi_stok}")
                print(f"Jumlah stok {produk_dipilih.nama} : {produk_dipilih.stok}")
                break
        else:
            print("Masukan Nomor 1 atau 2")
    elif menu == 4:
        print("Anda telah keluar")
        break
    else:
        print('Nomer tidak valid')
