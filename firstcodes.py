# You can start learning by first typing "Hello World"
def hello_and_variables():
    print("Hello World")

    a = 5
    print(a)

    numara = 2018
    print(numara)

    dil = "Python"
    print(dil)

    pi = 3.14
    print(pi)

    sayi = 5

    AdiSoyadi = "Suna Yıldız"
    Personel_No = 123456789
    kullanici = "Öğrenci"
    Sayi1 = 10
    sayi_2 = 15
    OGR_NO = 2018123456
    ogrenciBolum_no = 202313171049
    sehir = "Aydın"
    Sehir = "İzmir"

    print(sayi, AdiSoyadi, Personel_No, kullanici,
          Sayi1, sayi_2, OGR_NO, ogrenciBolum_no, sehir, Sehir)


# Demonstrating sep, end and string unpacking
def print_formatting():
    print("Çukurova", "Üniversitesi", sep="*")
    print("P", "y", "t", "h", "o", "n", sep=".")
    print(*"Python", sep=".")
    print(*"Çukurova", sep=".")
    print("bir", "iki", "üç", "dört", "on dört", sep="mumdur", end="mumdur\n")

    ad = "Suna"
    soyadi = "Yildiz"
    sehir = "Aydın"
    yil = 2025
    print(ad, soyadi, sehir, yil, sep="\n")

    print("Suna\nYıldız\n20 yasinda")
    print("bir", "iki", "üç", sep="\t")
    print("Çukurova", "Üniversitesi", sep="\n\n")


# Unicode and Hex character printing
def unicode_and_hex():
    print("\u0068")
    print("\x45")
    print("\u0065")
    print("\x67")


# Data type conversion example
def type_conversion():
    pi = 3.14
    a = 45
    a = str(a)
    print(type(a))

    a = float(pi)
    print(int(a))

    b = "suna"
    a = b
    print(a)


# Variable declaration and printing examples
def variable_examples():
    Ad = "Suna"
    Soyad = "Yıldız"
    Bölüm = "Bilgisayar Mühendisliği"
    BölümNo = 202313171049

    print(Ad, Soyad, Bölüm, BölümNo)
    print(*"ÇukurovaÜniversitesi", sep="_")

    a = "Adana"
    b = "Mersin"
    c = "Hatay"
    print(a, b, c, sep="\n")


# Monthly travel expense calculation
def travel_expense():
    Adı = "Suna"
    Soyadi = "Yıldız"
    Gidis = 1.5
    Dönüs = 1.5
    AyGun = 20

    YolUcret = (Gidis + Dönüs) * AyGun
    print(Adı, Soyadi, "günde", (Gidis + Dönüs),
          "TLden", AyGun, "günde aylık yol masrafı",
          YolUcret, "olmaktadır.")


if __name__ == "__main__":
    hello_and_variables()
    print_formatting()
    unicode_and_hex()
    type_conversion()
    variable_examples()
    travel_expense()
