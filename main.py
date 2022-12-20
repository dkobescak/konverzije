from km_to_miles import km_to_miles
from celsius_to_fahrenheit import celsius_to_fahrenheit
from kg_to_pound import kg_to_pound
from l_to_galon import l_to_galon
from kw_to_hp import kw_to_hp


conversion = {
    "1": km_to_miles,
    "2": celsius_to_fahrenheit,
    "3": kg_to_pound,
    "4": l_to_galon,
    "5": kw_to_hp,
}
while True:
    print()
    which_conversion = input("Koju konverziju zelis: 1=Km/miles, 2=C/F, 3=Kg/Funta, 4=litra/galon, "
                             "5=Kw/KS ili exit ako zelite izaci iz programa: ")
    if which_conversion == "exit":
        break
    elif which_conversion not in ["1", "2", "3", "4", "5"]:
        print("Unijeli ste nevazeci broj. Pokusajte ponovno.")
        continue
    else:
        conversion[which_conversion]()

