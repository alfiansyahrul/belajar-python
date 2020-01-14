#tinggi = int(input("Masukan Tinggi : "))
#jari = int(input("Masukan Jari-jari Lingkaran : "))

print("===== Def function =====")
def tabung(tinggi, diameter):
    volume=((phi*jari*jari)*tinggi)
    print(volume)

tinggi = 28
jari = 10
phi=22/7

print("tingggi = ",tinggi)
print("diameter = ",jari)

print("volume tabung adalah")
tabung(tinggi, jari)

print("====== lambda function ======")

segitiga = lambda sisi : sisi * 3

print("sisi = 50")
print("keliling segitiga", segitiga(50))


print("===== Kalkulator =====")

#penambahan
def tambah (a, b):
   return a+b
#pengurangan
def kurang (a, b):
   return a-b
#perkalian
def kali (a, b):
   return a*b
#pembagian
def bagi (a, b):
   return a/b
#modulo
def modulo (a, b):
   return a%b

#Menu Kalkulator
print("Pilih Operasi :")
print("1. Penambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. pembagian")
print("5. Modulo")
#input dari user
pilih = input("Masukan Pilihan (1/2/3/4/5) : ")
nilai1 =int(input("Masukan Bilangan Pertama : "))
nilai2 =int(input("Masukan Bilangan Ke-dua : "))
if pilih == '1':
   print(nilai1, "+", nilai2, "=", tambah(nilai1,nilai2))
elif pilih == '2':
   print(nilai1, "-", nilai2, "=", kurang(nilai1,nilai2))
elif pilih == '3':
   print(nilai1, "x", nilai2, "=", kali(nilai1,nilai2))
elif pilih =='4':
   print(nilai1, "/", nilai2, "=", bagi(nilai1,nilai2))
elif pilih =='5':
   print(nilai1, "%", nilai2, "=", modulo(nilai1,nilai2))
else:
   print("Pilihan Tidak Ada")
