# seperti bahasa lainnya, python memiliki variable dan tipe data, dan ini sendiri adalah komen yang diawali dengan tanda '#' 
from xml.etree.ElementTree import tostring


firstname = "mohammad"
middlename = " izamul fikri"
lastname = " fahmi"

umur = 19

print(firstname+middlename+lastname)
print("umur " + str(umur))
print("-------- Cara Lain --------")
#cara lain memanggil variable
print(f"{firstname}{middlename}{lastname}")
#karena agar int bisa ditampilkan, maka harus diubah dahulu kedalam str. namun ketika menggunakan cara awalan f tidak perlu
print(f"umur {umur}")   

# dalam python tidak perlu menginisialisasi tipe data seperti int atau String, tapi secara canggih python sudah bisa mengerti

print("Mengecek tipe data")
print("tipe data umur : " + str(type(umur)))
print("tipe data last name : "+ str(type(lastname)))

# terdapat juga variable lain seperti boolean, float, dll, tinggal disesuaikan saja