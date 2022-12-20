def l_to_galon():
    factor = 0.2642
    print()
    l_or_gal = input("Zelis li pretvoriti litre u galone (L) ili galone u litre (GAL)? Unesi L ili GAL: ").lower()
    print()
    amount = int(input("Unesi kolicinu za preracunati: "))
    print()
    if l_or_gal == "gal":
        #mozda dodati if za jedninu i mnozinu
        liters = amount / factor
        print(f"{amount} galon/a je {liters:.2f} litri")
    else:
        galons = amount * factor
        print(f"{amount} litra/i je {galons:.2f} galona")