def celsius_to_fahrenheit():
    print()
    c_to_f = input("Zelis li pretvoriti Celzijuse u Fahreheite (C) ili Fahrenheite u Celzijuse (F)? Unesi C ili F: ").lower()
    print()
    degrees = int(input("Unesi jedinicu za preracunati: "))
    print()
    if c_to_f == "c":
        fahrenheit = degrees + 32
        print(f"{degrees} C je {fahrenheit} F")
    else:
        celsius = degrees * (9/5) + 32
        print(f"{degrees} F je {celsius} C")