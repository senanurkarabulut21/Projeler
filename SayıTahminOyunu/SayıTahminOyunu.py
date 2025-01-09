import random


randomSayi = random.randint(1,100)
sayac = 0

while True:
    sayac += 1
    sayi = int(input("1 ile 100 arasýnda rastgele seçilen sayýyý bilmek için bir sayý giriniz (oyundan çýkmak için '0' a basýnýz): "))
    if (sayi == 0):
        print("Oyundan Çýkýldý")
        break
    if (sayi < randomSayi):
        print("Daha Büyük Bir sayý Giriniz. ")
        continue
    if (sayi > randomSayi):
        print("Daha Küçük Bir sayý Giriniz. ")
        continue
    else:
        print("Tebrikler Doðru Bildiniz")
        print("Rastgele Seçilen Sayý: {}".format(randomSayi))
        print("Tahmin Sayýsý: {}".format(sayac))
        break

