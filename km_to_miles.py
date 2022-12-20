def km_to_miles():
    factor = 0.6214
    print()
    km_or_miles = input("Zelis li pretvoriti kilometre u milje (KM) ili milje u kilometre (MILJE)? Unesi KM ili MILJE: ").lower()
    print()
    distance = int(input("Unesi distancu za preracunati: "))
    print()
    if km_or_miles == "milje":
        kilometers = distance / factor
        print(f"U {distance} milja ima {kilometers:.2f} kilometara")
    else:
        miles = distance * factor
        print(f"U {distance} kilometara ima {miles:.2f} milja")