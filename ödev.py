# Grade evaluation program using conditional statements
not1 = float(input("Notunuzu giriniz:"))
if not1>100:
    print("Hatalı girdiniz")
elif 90<not1<=100:
    print("Notunuz A")
elif 80<not1<=90:
    print("Notunuz B")
elif 70<not1<=80:
    print("Notunuz C")
else:
    print("Notunuz F")
    
# Program that checks whether the entered number is divisible by both 3 and 7 at the same time
sayi = float(input("Bir sayi giriniz: "))
if sayi%3==0 and sayi%7==0:
    print("Sayi hem 3've hem 7' ye bölünebiliyor.")
else:
     print("Sayi bölünemez.")

# Evaluating air temperature using conditional statements
havaSicakligi=int(input("Hava sıcaklıgını giriniz: "))
if havaSicakligi>0:
    print("Hava sıcak")
elif havaSicakligi<0:
    print("Hava soguk")
else:
    print("Hava sicakligi 0")

    

