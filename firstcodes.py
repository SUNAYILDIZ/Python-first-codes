# You can start learning by first typing "Hello World" 
print("Hello World ");
# Assign a value to a variable,then print his value to the screen
a=5;
print(a);

numara=2018;
print(numara);
dil ="Python";
print(dil);
pi=3.14;
print(pi);
sayi=5;

#print all variables with a single print command

AdiSoyadi="Suna Yıldız";
Personel_No=123456789;
kullanici="Öğrenci";
Sayi1=10;
sayi_2=15;
OGR_NO=2018123456;
ogrenciBolum_no=202313171049;
sehir="Aydın";
Sehir="İzmir";
print(sayi,AdiSoyadi,Personel_No,kullanici,Sayi1,sayi_2,OGR_NO,ogrenciBolum_no,sehir,Sehir);

# Separating characters using the print() function,
# demonstrating the use of a custom separator (sep) and line end (end) control

print("Çukurova","Üniversitesi",sep="*");
print("P","y","t","h","o","n",sep=".");
print(*"Python",sep=".");
print(*"Çukurova",sep=".");
print("bir", "iki", "üç", "dört", "on dört",sep="mumdur",end="mumdur\n");
ad= "Suna";
soyadi="Yildiz";
sehir="Aydın";
yil=2025;
print(ad,soyadi,sehir,yil,sep="\n");
print("Suna\nYıldız\n20 yasinda");
print("bir","iki","üç",sep="\t");
print("Çukurova","Üniversitesi",sep="\n\n");

# Printing characters on the screen using their Unicode (\uXXXX) and Hex (\xXX) codes
print("\u0068");
print("\x45");
print("\u0065");
print("\x67");

# Converting to different data types and redefining variables
a=45;
a=str(a);
print(type(a));
a=float(pi);
print(int(a))
b="suna";
a=b
print(a)

# Variable declaration in Python, separating with underscores, and printing lines one below the other
Ad="Suna"
Soyad="Yıldız"
Bölüm="Bilgisayar Mühendisliği"
BölümNo=202313171049
print(Ad,Soyad,Bölüm,BölümNo)
print(*"ÇukurovaÜniversitesi",sep ="_")
a="Adana"
b="Mersin"
c="Hatay"
print(a,b,c,sep="\n")

# Calculating monthly travel expenses using variables and printing them to the screen
Adı="Suna"
Soyadi="Yıldız"
Gidis=1.5
Dönüs=1.5
AyGun=20
YolUcret=(Gidis+Dönüs)*20
print(Adı,Soyad,"günde",(Gidis+Dönüs),"TLden",AyGun,"günde aylık yol masrafı",YolUcret,"olmaktadır.")



