import random


randomSayi = random.randint(1,100)
sayac = 0

while True:
    sayac += 1
    sayi = int(input("1 ile 100 aras�nda rastgele se�ilen say�y� bilmek i�in bir say� giriniz (oyundan ��kmak i�in '0' a bas�n�z): "))
    if (sayi == 0):
        print("Oyundan ��k�ld�")
        break
    if (sayi < randomSayi):
        print("Daha B�y�k Bir say� Giriniz. ")
        continue
    if (sayi > randomSayi):
        print("Daha K���k Bir say� Giriniz. ")
        continue
    else:
        print("Tebrikler Do�ru Bildiniz")
        print("Rastgele Se�ilen Say�: {}".format(randomSayi))
        print("Tahmin Say�s�: {}".format(sayac))
        break

