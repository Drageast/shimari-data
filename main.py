import random


class Blueprints(object):
    pass


def ID():
    return random.randint(1000, 9999)


def Calculate():
    inp = input("Gebe einen Schadenswert für Stufe 1 ein. 0 wird als Zufall gewertet. (30-50 Wird empfohlen):\n")
    if int(inp) == 0:
        inp = random.randint(30, 50)
    inp = int(inp)
    y = Blueprints()
    y.Schaden1 = inp
    y.Schaden2 = round(inp * 2.1)
    y.Schaden3 = round(inp * 3.5)
    y.Kosten1 = round(y.Schaden1 * 1.5)
    y.Kosten2 = round(y.Schaden2 * 1.5)
    y.Kosten3 = round(y.Schaden3 * 1.65)
    Energie = round((((y.Kosten1 * y.Kosten2) / y.Schaden3) * 0.13))
    while Energie < (y.Schaden3 * 1.9):
        Energie += random.randint(1, 15)
    y.Energie = Energie
    health = round((1898 ** 1.55) / y.Schaden3)
    y.Health = health
    inp2 = input("Gebe eine Klasseneigenschaft an: 1 = Tank, 2 = Assassine, 3 = Ausgeglichen:\n")
    inp2 = int(inp2)
    if inp2 == 1:
        print("Tank...\n")
        y.Health += random.randint(20, 45)
        y.Kosten1 += random.randint(5, 20)
        y.Kosten2 += random.randint(5, 20)
        y.Kosten3 += random.randint(5, 20)
    if inp2 == 2:
        print("Assassine...\n")
        y.Health -= random.randint(75, 150)
        y.Schaden3 += random.randint(50, 125)
        y.Kosten1 -= random.randint(15, 30)
        y.Kosten2 -= random.randint(15, 30)
        y.Kosten3 -= random.randint(30, 45)
    if inp2 == 3:
        print("Ausgeglichen...\n")

    print(f"ID: {ID()}\n\n"
          f"Energie: {y.Energie}\n"
          f"Schaden: [ {y.Schaden1}, {y.Schaden2}, {y.Schaden3} ]\n"
          f"Kosten: [ {y.Kosten1}, {y.Kosten2}, {y.Kosten3} ]\n"
          f"Leben: {y.Health}")


Calculate()
