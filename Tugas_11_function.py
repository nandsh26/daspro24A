def reverse_per_kata(kalimat):
    kata = kalimat.split()      # Split digunakan untuk memecah kalimat menjadi list kata
    hasil = []                  # Variabel kosong untuk menyimpan list
    for i in kata:              # Melakukan perulangan pada setiap kata pada variabel kata
        hasil.append(i[::-1])   # Membalikkan urutan huruf pada setiap kata lalu menyimpannya ke dalam variabel hasil
    return ' '.join(hasil)      # Menggabungkan kata-kata pada variabel hasil menjadi satu kalimat dengan menambahkan spasi sebagai pemisah

print(reverse_per_kata("AKU CINTA KAMU"))
# Output: "UKA ATNIC UMAK"

def urutkan_kalimat(kalimat, urutan):
    kata = kalimat.split()          # Split digunakan untuk memecah kalimat menjadi list kata
    terurut = []                    # Variabel kosong untuk menyimpan list
    for i in urutan:                # Melakukan perulangan pada setiap kata parameter urutan
        terurut.append(kata[i - 1]) # Mengambil kata sesuai indeks, yaitu dari indeks ke 1 karena dalam kodenya ditambah -1 dan menambahkannya ke variabel terurut
    return ' '.join(terurut)        # Menggabungkan kata-kata pada variabel terurut menjadi satu kalimat dengan menambahkan spasi sebagai pemisah

print(urutkan_kalimat("HARI INI SEDANG BELAJAR PYTHON", [5, 1, 4, 3, 2]))
# Output: "PYTHON HARI BELAJAR SEDANG INI"

def ganti_vokal(kalimat, opsi):
    vokal_kecil = {'a' : '4', 'i' : '1', 'u' : '|_|', 'e' : '3', 'o' : '0'}  # Digunakan untuk mengubah huruf vokal kecil dengan simbol tertentu
    vokal_besar = {'A' : '4', 'I' : '1', 'U' : '|_|', 'E' : '3', 'O' : '0'}  # Digunakan untuk mengubah huruf vokal besar dengan simbol tertentu
    
    hasil = ""                                     # Variabel kosong untuk menyimpan hasil akhir
    for huruf in kalimat:                          # Melakukan perulangan pada setiap huruf dalam parameter kalimat
        if opsi == 1 and huruf in vokal_kecil:     # Jika opsi 1 dan huruf termasuk ke dalam daftar vokal_kecil
            hasil += vokal_kecil[huruf]            # Maka, gantikan huruf tersebut dengan simbol dari vokal_kecil
        elif opsi == 2 and huruf in vokal_besar:   # Jika opsi 2 dan huruf termasuk dalam daftar vokal_besar
            hasil += vokal_besar[huruf]            # Maka, gantikan huruf tersebut dengan simbol dari vokal_besar
        else:                                      
            hasil += huruf                         # Jika huruf tidak ada dalam opsi, maka tambahkan apa adanya saja
    return hasil                                   # Mengembalikan kalimat akhir setelah huruf vokal diganti sesuai opsi
    
print(ganti_vokal("Aku Cinta Kamu", 1))
# Output: "Ak|_| C1nt4 K4m|_|"
print(ganti_vokal("Aku Cinta Kamu", 2))
# Output: "4ku Cinta Kamu"