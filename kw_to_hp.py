def kw_to_hp():
    factor = 1.3596
    print()
    kw_or_hp = input("Zelis li pretvoriti kilovate u konjske snage (KW) ili konjske snage u kilovate (KS)? Unesi KW ili KS: ").lower()
    print()
    amount = int(input("Unesi iznos koji zelis preracunati: "))
    print()
    if kw_or_hp == "ks":
        kw = amount / factor
        print(f"{amount} KS je {kw:.2f} KW")
    else:
        ks = amount * factor
        print(f"{amount} KW je {ks:.2f} KS")