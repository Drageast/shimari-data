import random


def balance():
    BasisEnergie = input("BasisEnergie (Range 0 - 75):")
    if int(BasisEnergie) == 0:
        BasisEnergie = random.randint(40, 75)
    BasisEnergie = int(BasisEnergie)

    BASE = 1250

    Baseline = BASE / int(BasisEnergie)

    Damage1 = round(BasisEnergie // 4)
    Damage2 = round(BasisEnergie // 3)
    Damage3 = round(BasisEnergie // 2)

    Cost1 = round(BasisEnergie * 0.35)
    Cost2 = round(BasisEnergie * 0.5)
    Cost3 = round(BasisEnergie * 0.65)

    Health = round(Baseline + round(((Cost1 + Damage1) + (Cost2 + Damage2) + (Cost3 + Damage3)) / (BASE / (Baseline ** 2.2))))

    ID = random.randint(1000, 9999)


    print(f"ID: {ID}\n\n"
          f"Energie: {BasisEnergie}\n"
          f"Schaden: [ {Damage1}, {Damage2}, {Damage3} ]\n"
          f"Kosten: [ {Cost1}, {Cost2}, {Cost3} ]\n"
          f"Leben: {Health}"
          )



balance()
