# Grade evaluation program using conditional statements
def grade_evaluation():
    not1 = float(input("Notunuzu giriniz: "))
    if not1 > 100:
        print("Hatalı girdiniz")
    elif 90 < not1 <= 100:
        print("Notunuz A")
    elif 80 < not1 <= 90:
        print("Notunuz B")
    elif 70 < not1 <= 80:
        print("Notunuz C")
    else:
        print("Notunuz F")


# Program that checks whether the entered number is divisible by both 3 and 7 at the same time
def divisibility_check():
    sayi = float(input("Bir sayi giriniz: "))
    if sayi % 3 == 0 and sayi % 7 == 0:
        print("Sayi hem 3'e hem 7'ye bölünebiliyor.")
    else:
        print("Sayi bölünemez.")


# Evaluating air temperature using conditional statements
def temperature_evaluation():
    havaSicakligi = int(input("Hava sıcaklığını giriniz: "))
    if havaSicakligi > 0:
        print("Hava sıcak")
    elif havaSicakligi < 0:
        print("Hava soğuk")
    else:
        print("Hava sıcaklığı 0")


if __name__ == "__main__":
    grade_evaluation()
    divisibility_check()
    temperature_evaluation()

    


