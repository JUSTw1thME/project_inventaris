print("-----------KALKULATOR-------------")
nomor_pertama = int(input('masukan huruf pertama :'))
nomor_kedua = int(input('masukan huruf kedua :'))
print('1. tambah +')
print('2. kurang -')
print('3. kali x')
print('4. bagi /')
pilih_operasi = int(input('Pilih operasi yang tersedia :'))
if pilih_operasi == 1:
  print(f"Hasil dari penjumlahan {nomor_pertama} + {nomor_kedua} = {nomor_pertama + nomor_kedua}")
if pilih_operasi == 2:
  print(f"Hasil dari pengurangan {nomor_pertama} - {nomor_kedua} = {nomor_pertama - nomor_kedua}")
if pilih_operasi == 3:
  print(f"Hasil dari perkalian {nomor_pertama} x {nomor_kedua} = {nomor_pertama * nomor_kedua}")
if pilih_operasi == 4:
  print(f"Hasil dari pembagian {nomor_pertama} / {nomor_kedua} = {nomor_pertama / nomor_kedua}")
