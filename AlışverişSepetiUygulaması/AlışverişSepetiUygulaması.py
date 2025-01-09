manav_listesi = [
    'Elma',
    'Armut',
    'Muz'
]

sepet = []

print("Mevcut �r�nler:")
for urun in manav_listesi:
    print(urun)

while True:
    secim = input("�r�n se�in (��kmak i�in 'bitti'): ").capitalize()
    if secim == 'Bitti':
        break
    if secim in manav_listesi:
        try:
            miktar = int(input(f"Ka� kilo {secim}? "))
            sepet.append((secim, miktar))
        except ValueError:
            print("L�tfen ge�erli bir say� girin.")
    else:
        print("�r�n mevcut de�il.")

print("Sepetiniz:")
for urun, miktar in sepet:
    print(f"{urun}: {miktar} kilo")

