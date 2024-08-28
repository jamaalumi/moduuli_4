
TUUMAT_CM: float = 2.54

while True:

    tuumat = float(input("Anna tuumamäärä (negatiivinen arvo lopettaa): "))


    if tuumat < 0:
        print("Negatiivinen tuumamäärä saatu. Ohjelma lopettaa.")
        break


    senttimetrit = tuumat * TUUMAT_CM


    print(f"{tuumat} tuumaa on {senttimetrit:.2f} senttimetriä.")