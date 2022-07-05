#dalam python, cukup gunakan fungsi input
nama = input("Nama kamu siapa : ")
umur = input("Umur kamu berapa : ")
print(f"Namaku adalah {nama}, umurku {umur}")

#inputan akan selalu bernilai String
#jadi semisal ingin melakukan proses hitung dari umur, maka harus di konversi

umur = int(umur)
print("20 tahun lagi saya akan berumur " + str(umur + 20))