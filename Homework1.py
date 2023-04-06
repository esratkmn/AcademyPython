def kredileriListele():
 krediler = ["Hızlı kredi" , "Maaşını Halkbank'tan alanlara özel" , "Mutlu emekli ihtiyaç kredisi" ]

 for kredi in krediler:
    print("<option>"+kredi+"<option>")

kredileriListele()
kredileriListele()
kredileriListele()
kredileriListele()
kredileriListele()
kredileriListele()

#-------------------------
#degiskenler.py
baslik = "HABERİNİZ OLSUN"
vade = 12
faizOrani1 = 1.47
faizOrani2 = 1.44

print(baslik)
print(type(baslik))
print(type(vade))
print(type(faizOrani1))

mesaj = "Hoşgeldin"
musteriAdi = "Esra"
musteriSoyadi = "Tokman"
sonucMesaj = mesaj +" "+musteriAdi +" "+musteriSoyadi +"!"
print(sonucMesaj)

sayi1 = 10
sayi2 = 20

#------------------------
#donguler.py
krediler = ["Hızlı kredi" , "Maaşını Halkbank'tan alanlara özel" , "Mutlu emekli ihtiyaç kredisi" ]

for kredi in krediler:
  print(kredi)

for i in range(len(krediler)):
  print(krediler[i])

for i in range(3,10):
  print(i)

for i in range(0,10,2):
  print(i)

for i in range(1,12,2):
  print(i)

  #------------------------
  #listeler.py
  krediler = ["Hızlı kredi" , "Maaşını Halkbank'tan alanlara özel" , "Mutlu emekli ihtiyaç kredisi" ]

print(krediler)
print(krediler[0])
print(krediler[1])
print(krediler[2])
print(len(krediler))
krediler[0] = "Çabuk kredi"
print(krediler)

print(krediler[5])

#-------------------------------
#sartBlokları.py
dolarDun = 7.65
dolarBugun = 7.85

if dolarDun>dolarBugun:
  print("Azalış oku")
  print("Bitti")
elif dolarDun<dolarBugun:
  print("Artış oku")

else:
  print("Eşittir oku")
  print("Bitti")

#if dolarDun<dolarBugun:
 # print("Artış oku")

#if dolarDun==dolarBugun :
 # print("Eşittir oku")

