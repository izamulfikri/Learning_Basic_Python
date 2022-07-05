#dalam python, isi dari sebuah variable dapat dipanggil berdasarkan indeks,
makanan = "sate soto bakso"
print(f"Makanan favoritku adalah {makanan[0:4]}") # maksudnya, kita memanggil isi dari variable makanan range 0 sampai 4 disini adalah sate

#dalam string juga memiliki banyak fungsi atau method untuk melakukan proses unik lainnya, misal
#menjadikan kapital
katakan = "aku cinta kamu"
print(katakan)
print("tegaskan, jika kamu memang. ucap si cewe")
print(katakan.upper() + ", tegas si cowo")

#untuk menghitung length bisa gunakan 'len'

print(len(katakan))