sayi1 = int(input("Ýlk Sayýyý Giriniz. "))
sayi2 = int(input("Ýkinci Sayýyý Giriniz. "))
islem = input("Yapmak Ýstediðiniz Ýþlemi Giriniz.(Toplama. +, Çýkarma: -, Çarpma: *, Bölme: /)")

if islem == "+":
    print("Sonuç: "+str(sayi1+sayi2))

elif islem == "-":
    print("Sonuç: "+str(sayi1-sayi2))

elif islem == "*":
    print("Sonuç: "+str(sayi1*sayi2))

elif islem == "/":
    print("Sonuç: "+str(sayi1/sayi2))