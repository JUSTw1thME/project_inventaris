'''MEMBUAT PROGRAM PENGHITUNG PYTHAGORAS OTOMATIS'''
import math


def pythagoras(sudut_a,sudut_b,sudut_c):
    if sudut_c == None:
        return math.sqrt(sudut_a**2 + sudut_b**2)
    elif sudut_a == None:
        return math.sqrt(sudut_c**2 - sudut_b**2)
    elif sudut_b == None:
        return math.sqrt(sudut_c**2 -sudut_a**2)
        

def input_sisi(nama_sisi):
    nilai = input(f'Masukan ukuran {nama_sisi} (kosongkan jika tidak diketahui): ')
    if nilai.strip() == '':
        return None
    return int(nilai)

while True:
    print('Selamat Datang di operasi pythagoras otomatis\n')
    sisi_depan = input_sisi('sisi depan segitiga')
    sisi_samping = input_sisi('sisi samping segitiga')
    sisi_miring = input_sisi('sisi miring segitiga')

    jumlah_kosong = [sisi_samping,sisi_miring,sisi_depan].count(None)

    if jumlah_kosong == 0:
        print('Semua sisi terisi, tidak ada yang perlu dihitung')
    elif jumlah_kosong > 1:
        print('Data yang diberikan kurang untuk dihitung')
    else:
        hasil_p = pythagoras(sisi_depan, sisi_samping, sisi_miring)
        print(f"Hasil dari perhitungan pythagoras adalah = {hasil_p:.1f}")

    lanjut = input("Apakah anda masih ingin melanjutkan program y/n :")
    if lanjut == "y":
        continue
    elif lanjut == "n":
        break    
