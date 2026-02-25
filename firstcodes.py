"""
TEMEL PYTHON KONULARI
Bu dosya değişkenler, veri tipleri, string işlemleri,
listeler, demetler ve sözlükleri örneklerle göstermektedir.
"""


# -------------------------------------------------
# 1️⃣ Değişken Tanımlama ve Yazdırma
# -------------------------------------------------
def variables_example():
    """Farklı veri tiplerinde değişken tanımlama ve yazdırma örnekleri."""

    numara = 2018
    dil = "Python"
    pi = 3.14

    sayi = 5
    adi_soyadi = "Suna Yıldız"
    personel_no = 123456789
    kullanici = "Öğrenci"
    sayi1 = 10
    sayi_2 = 15
    ogr_no = 2018123456
    ogrenci_bolum_no = 202313171049
    sehir1 = "Aydın"
    sehir2 = "İzmir"

    print(numara, dil, pi)
    print(sayi, adi_soyadi, personel_no, kullanici,
          sayi1, sayi_2, ogr_no, ogrenci_bolum_no,
          sehir1, sehir2)


# -------------------------------------------------
# 2️⃣ Print Parametreleri (sep - end)
# -------------------------------------------------
def print_parameters():
    """sep ve end parametrelerinin kullanım örnekleri."""

    print("bir", "iki", "üç", sep="\t")
    print("Çukurova", "Üniversitesi", sep="\n\n")
    print("Summer Internship", end="!\n")

    # String unpacking
    print(*"Python", sep=".")
    print(*"Çukurova", sep=".")


# -------------------------------------------------
# 3️⃣ Unicode ve Hex Karakterler
# -------------------------------------------------
def unicode_example():
    """Unicode ve Hex karakter yazdırma örnekleri."""

    print("\u0068")  # h
    print("\x45")    # E
    print("\u0065")  # e
    print("\x67")    # g


# -------------------------------------------------
# 4️⃣ Veri Tipi Dönüşümleri
# -------------------------------------------------
def type_conversion_example():
    """String, float ve int dönüşüm örnekleri."""

    a = 45
    a = str(a)
    print(type(a))  # str

    pi = 3.14
    a = float(pi)
    print(int(a))   # 3

    b = "suna"
    a = b
    print(a)


# -------------------------------------------------
# 5️⃣ Matematiksel İşlemler
# -------------------------------------------------
def math_operations():
    """Temel matematik işlemleri örnekleri."""

    a = 6 // 2      # Tam sayı bölme
    b = 6 ** 2      # Üs alma
    c = ((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

    print(a)
    print(b)
    print(c)


# -------------------------------------------------
# 6️⃣ String İşlemleri
# -------------------------------------------------
def string_operations():
    """String uzunluğu ve slicing örnekleri."""

    metin = "Dijital Beceriler"
    metin += " Python Eğitimi"
    print(metin)

    yazi = "Welcome to Paris"
    print(len(yazi))     # Uzunluk
    print(yazi[2:5])     # Parça alma

    name = "Sabahattin"
    print(name[4:8])


# -------------------------------------------------
# 7️⃣ Listeler
# -------------------------------------------------
def list_examples():
    """Liste işlemleri örnekleri."""

    karma_list = ["Bilişim", 58, "Türkçe", 3.14]
    print(len(karma_list))

    sayilar = [1,2,3,4,5,6,7,8,9]
    print(sayilar[0])
    print(sayilar[-1])

    list1 = [1,2,3]
    list2 = [4,5,6]
    print(list1 + list2)

    list3 = [6,7,8,9]
    print(3 * list3)

    liste = [28,50,65,79,92]
    liste[3] = 11
    liste[-3:] = [100,400,500]
    print(liste)


# -------------------------------------------------
# 8️⃣ Demetler (Tuple)
# -------------------------------------------------
def tuple_examples():
    """Demet işlemleri örnekleri."""

    demet = (1,4,4,4,7,89,8)
    print(demet.count(4))

    demet1 = ("Python","Arduino","Scratch")
    print(demet1.index("Scratch"))


# -------------------------------------------------
# 9️⃣ Sözlük (Dictionary)
# -------------------------------------------------
def dictionary_examples():
    """Sözlük veri tipi örnekleri."""

    dictionary = {
        "Name": "Suna",
        "Surname": "Yıldız",
        "Şehir": "Aydın",
        "Age": 20,
        "Weight": 52
    }

    dictionary["Height"] = 160
    dictionary["Age"] += 1

    print(dictionary.keys())
    print(dictionary.values())
    print(dictionary.items())

    for key, value in dictionary.items():
        print("Anahtar:", key, "Değer:", value)


# -------------------------------------------------
# MAIN
# -------------------------------------------------
def main():
    variables_example()
    print("-" * 40)
    print_parameters()
    print("-" * 40)
    unicode_example()
    print("-" * 40)
    type_conversion_example()
    print("-" * 40)
    math_operations()
    print("-" * 40)
    string_operations()
    print("-" * 40)
    list_examples()
    print("-" * 40)
    tuple_examples()
    print("-" * 40)
    dictionary_examples()


if __name__ == "__main__":
    main()
