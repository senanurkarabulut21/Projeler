sayi1 = int(input("�lk Say�y� Giriniz. "))
sayi2 = int(input("�kinci Say�y� Giriniz. "))
islem = input("Yapmak �stedi�iniz ��lemi Giriniz.(Toplama. +, ��karma: -, �arpma: *, B�lme: /)")

if islem == "+":
    print("Sonu�: "+str(sayi1+sayi2))

elif islem == "-":
    print("Sonu�: "+str(sayi1-sayi2))

elif islem == "*":
    print("Sonu�: "+str(sayi1*sayi2))

elif islem == "/":
    print("Sonu�: "+str(sayi1/sayi2))