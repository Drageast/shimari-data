import Shimari_Blueprint

a = Shimari_Blueprint.Shimari(4448)

b = Shimari_Blueprint.Shimari(3015)


print(a.post_fight_data())
print("-------")
print(b.post_fight_data())

data = Shimari_Blueprint.Shimari.fight(a, b, 3)

print("-------")
print(a.fight_data(data.damage))
print("-------")
print(b.post_fight_data())
