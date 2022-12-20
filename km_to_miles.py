def km_to_miles():
    factor = 0.6214
    print()
    km_or_miles = input("Zelis li pretvoriti kilometre u milje (KM) ili milje u kilometre (MILJE)? Unesi KM ili MILJE: ").lower()
    print()
    if km_or_miles != "km" and km_or_miles != "milje":
        print("Krivi unos jedinice za konverziju. Pokušajte ponovno.")
        km_to_miles()
    try:
        distance = int(input("Unesi distancu za preracunati: "))
        print()
        if km_or_miles == "milje":
            kilometers = distance / factor
            print(f"U {distance} milja ima {kilometers:.2f} kilometara")
        elif km_or_miles == "km":
            miles = distance * factor
            print(f"U {distance} kilometara ima {miles:.2f} milja")

    except ValueError:
        print("Nije unesen broj. Pokusajte ponovno.")
        km_to_miles()
