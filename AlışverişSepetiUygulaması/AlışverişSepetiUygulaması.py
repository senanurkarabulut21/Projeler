manav_listesi = [
    'Elma',
    'Armut',
    'Muz'
]

sepet = []

print("Mevcut Ürünler:")
for urun in manav_listesi:
    print(urun)

while True:
    secim = input("Ürün seçin (Çýkmak için 'bitti'): ").capitalize()
    if secim == 'Bitti':
        break
    if secim in manav_listesi:
        try:
            miktar = int(input(f"Kaç kilo {secim}? "))
            sepet.append((secim, miktar))
        except ValueError:
            print("Lütfen geçerli bir sayý girin.")
    else:
        print("Ürün mevcut deðil.")

print("Sepetiniz:")
for urun, miktar in sepet:
    print(f"{urun}: {miktar} kilo")

