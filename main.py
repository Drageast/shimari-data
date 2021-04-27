import random


class Blueprints(object):
    pass


def inputs(attr: int):
    if attr == 1:
        data = input("Gebe bitte den niedrigsten Schadenswert ein. 0 wird als Zufall gewertet:")
    if attr == 2:
        data = input("Spezifiziere, ob: Tank (1), Assassine (2), Ausgeglichen (3):")
    return int(data)


def ID():
    return random.randint(1000, 9999)


def Damage():
    x = Blueprints()
    data = inputs(1)
    x.input1 = data
    if data == 0:
        x.dmg1 = random.randint(15, 55)
    else:
        x.dmg1 = data
    x.dmg2 = round(x.dmg1 * 1.79)
    x.dmg3 = round(x.dmg2 * 2.13)
    return x


def Cost():
    x = Damage()
    x.cost1 = round(x.dmg1 * 0.69)
    x.cost2 = round(x.dmg2 * 0.68)
    x.cost3 = round(x.dmg3 * 0.67)
    return x


def Health():
    x = Cost()
    health = round((x.dmg1 + x.dmg2 + x.dmg3) * 3)
    data = inputs(2)
    x.input2 = data
    if data == 1:
        health += random.randint(1, 50)
        x.dmg1 -= random.randint(1, 15)
        x.dmg2 -= random.randint(1, 15)
        x.dmg3 -= random.randint(1, 15)
    elif data == 2:
        health -= random.randint(1, 40)
        x.dmg1 += random.randint(1, 20)
        x.dmg2 += random.randint(1, 20)
        x.dmg3 += random.randint(1, 20)
        x.cost1 -= random.randint(1, 10)
        x.cost2 -= random.randint(1, 10)
        x.cost3 -= random.randint(1, 10)
    else:
        pass

    x.health = health
    return x


def BaseEnergie():
    x = Health()
    Energie = round((x.cost1 + x.cost2 + (x.cost3 / 1.32)) / 1.11)
    x.energie = Energie
    return x


def Merge():
    x = BaseEnergie()
    while x.health >= 1050:
        x.health -= random.randint(1, 15)
    while x.dmg3 >= 180:
        x.dmg3 -= random.randint(1, 15)
    while x.health <= 500:
        x.health += random.randint(1, 15)

    print(f"\n\n\nID: {ID()}\n\n"
          f"Energie: {x.energie}\n"
          f"Schaden: [ {x.dmg1}, {x.dmg2}, {x.dmg3} ]\n"
          f"Kosten: [ {x.cost1}, {x.cost2}, {x.cost3} ]\n"
          f"Leben: {x.health}")


Merge()
