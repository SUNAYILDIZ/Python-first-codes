sayi1=float(input("Bir sayi giriniz: "))
sayi2=float(input("Bir sayi giriniz: "))
ortalama=(sayi1+sayi2)/2
print(ortalama)

dogumTarihi=input("Doğum tarihinizi GG.AA.YY formatında girin: ")
sayilar=dogumTarihi.split(".")
dogumYili=int(sayilar[2])
bugunTarih=input("Bugünün tarihini GG.AA.YY formatında giriniz: ")
sayilar1=bugunTarih.split(".")
bugunYil=int(sayilar1[2])
yas=bugunYil-dogumYili
print(yas)

x, y, z = 5, 6, 50
print(x + y + z)
print("\n...\n")
x = y = z = 50
print(x + y + z)


