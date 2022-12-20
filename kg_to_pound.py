def kg_to_pound():
    factor = 2.2046
    print()
    kg_or_pound = input("Zelis li pretvoriti kilograme u funte (KG) ili funte u kilograme (FUNTE)? Unesi KG ili FUNTE: ").lower()
    print()
    weight = int(input("Unesi iznos za preracunati: "))
    print()
    if kg_or_pound == "funte":
        kilograms = weight / factor
        print(f"{weight} funti je {kilograms:.2f} kilograma")
    else:
        pounds = weight * factor
        print(f"{weight} kilograma je {pounds:.2f} funti")