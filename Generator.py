import random
import yaml


def ID():
    with open("Data.yaml", "r") as f:
        data = yaml.safe_load(f)
    Inside = True
    while Inside is True:
        Id = random.randint(1000, 9999)

        if Id not in data["ID"]:
            Inside = False
    return Id


print(ID())
