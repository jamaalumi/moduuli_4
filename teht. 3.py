# Alustetaan muuttujat suurimmalle ja pienimmälle luvulle
pienin = None
suurin = None

while True:
    # Kysytään käyttäjältä luku
    syote = input("Syötä luku (tai paina Enter lopettaaksesi): ")

    if syote == "":

        break

    try:
        luku = float(syote)
    except ValueError:
        print("Virheellinen syöte. Syötä vain lukuja.")
        continue

    if pienin is None or luku < pienin:
        pienin = luku
    if suurin is None or luku > suurin:
        suuri = luku

if pienin is not None and suuri is not None:
    print(f"Pienin syötetty luku on {pienin}")
    print(f"Suurin syötetty luku on {suurin}")
else:
    print("Ei syötettyjä lukuja.")
