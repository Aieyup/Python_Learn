print("****************\tHesap Makinesine Hosgeldiniz\t****************")
toplama='+'
cikarma='-'
carpma='x'
bolme='/'
print(f"Toplama icin {toplama} Tusuna Basiniz\nCikarma icin {cikarma} Tusuna Basiniz\nCarpma icin {carpma} Tusuna Basiniz\nBolme icin {bolme} Tusuna Basiniz")
islemTipi=str(input("Lutfen yapmak istediginiz islemi giriniz:"))

if islemTipi ==toplama:
    sayi1=float(input("Lutfen toplamak istediginiz ilk sayiyi Giriniz: "))
    print(sayi1)
    sayi2=float(input("Lutfen toplamak isteginiz ikinci sayiyi Giriniz:"))
    toplam=sayi1+sayi2
    print(f"{sayi1} + {sayi2} ={toplam}")
elif islemTipi ==cikarma:
    sayi1=float(input("Lutfen cikarma istediginiz ilk sayiyi Giriniz: "))
    print(sayi1)
    sayi2=float(input("Lutfen cikarma isteginiz ikinci sayiyi Giriniz:"))
    cikarma=sayi1-sayi2
    print(f"{sayi1} - {sayi2} ={cikarma}")
elif islemTipi ==carpma:
    sayi1=float(input("Lutfen carpma istediginiz ilk sayiyi Giriniz: "))
    print(sayi1)
    sayi2=float(input("Lutfen carpma isteginiz ikinci sayiyi Giriniz:"))
    carpma=sayi1*sayi2
    print(f"{sayi1} X {sayi2} ={carpma}")
elif islemTipi ==bolme:
    sayi1=float(input("Lutfen bolme istediginiz ilk sayiyi Giriniz: "))
    print(sayi1)
    sayi2=float(input("Lutfen bolme isteginiz ikinci sayiyi Giriniz:"))
    bolme=sayi1/sayi2
    print(f"{sayi1} / {sayi2} ={bolme}")
else: 
    print("Hatali Islem Tipi Girdiniz!!")
print("************************************************************************")
input("... Programdan Çıkmak için her hangi bir Tuşa basın lutfen ...")