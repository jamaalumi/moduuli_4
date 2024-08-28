import random


arvattu_luku = random.randint(1, 10)

print("Yritä arvata, mikä luku on välillä 1 ja 10.")

while True:

    pelaajan_arvaus = input("Syötä arvauksesi: ")

    try:
        arvaus = int(pelaajan_arvaus)
    except ValueError:
        print("Virheellinen syöte. Syötä vain kokonaislukuja.")
        continue

    if arvaus < arvattu_luku:
        print("Liian pieni arvaus.")
    elif arvaus > arvattu_luku:
        print("Liian suuri arvaus.")
    else:
        print("Oikein! Olet arvannut numeron oikein.")
        break
