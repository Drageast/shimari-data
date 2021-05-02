import random
import yaml


class YAML:

    @staticmethod
    def PATH(container: str):
        try:
            with open("balancing.yaml", "r") as f:
                container_ = yaml.safe_load(f)
            container_ = container_[container]
            return container_
        except Exception as e:
            raise yaml.YAMLError(e)

    @staticmethod
    def GET(Container: str, *Load: str or int):
        try:
            dict_ = YAML.PATH(Container)
            new_dict = dict_
            for load in Load:
                new_dict = new_dict[load]

            return new_dict
        except Exception as e:
            raise yaml.YAMLError(e)

    @staticmethod
    def UNPACK(ID):
        try:
            with open("shimari.yaml", "r") as f:
                container = yaml.safe_load(f)
        except Exception as e:
            raise yaml.YAMLError(e)

        if ID == "List":
            List = container["Control"]
            return List

        else:

            try:
                raw_Shimari = container["ID"][ID]

                UnPacked = Object()
                UnPacked.Name = raw_Shimari["Name"]
                UnPacked.Motto = raw_Shimari["Motto"]
                UnPacked.Avatar = raw_Shimari["Avatar"]
                UnPacked.Mana = raw_Shimari["KDTN"]["Mana"]
                UnPacked.Kosten = raw_Shimari["KDTN"]["Kosten"]
                UnPacked.Leben = raw_Shimari["KDTN"]["Leben"]
                UnPacked.Schaden = raw_Shimari["KDTN"]["Schaden"]
                UnPacked.Element = raw_Shimari["KDTN"]["Element"][0]
                UnPacked.Element_Resistenz = raw_Shimari["KDTN"]["Element"][1]
                UnPacked.Seltenheit = raw_Shimari["KDTN"]["Seltenheit"]

                return UnPacked

            except Exception as e:

                raise yaml.YAMLError(e)


class Object(object):
    pass


class ShimariBASE:

    def __init__(self, ID: int):
        self.Data = YAML.UNPACK(ID)
        self.ID = ID
        self.Name: str = self.Data.Name
        self.Motto: str = self.Data.Motto
        self.Avatar: str = self.Data.Avatar
        self.Mana: int = self.Data.Mana
        self.Cost: list = self.Data.Kosten
        self.Damage: list = self.Data.Schaden
        self.Health: int = self.Data.Leben
        self.Element: str = self.Data.Element
        self.Resistance: str = self.Data.Element_Resistenz
        self.Rarity: int = self.Data.Seltenheit
        self.Operator: str = "Player"

        while "1" in self.Motto:
            self.Motto = self.Motto.replace("1", "ä")
        while "2" in self.Motto:
            self.Motto = self.Motto.replace("2", "ö")
        while "3" in self.Motto:
            self.Motto = self.Motto.replace("3", "ü")

    def __str__(self):
        return f"\n`Name`: _{self.Name}_\n`Motto`:\n_{self.Motto}_\n`Mana`: _{self.Mana}_\n`Angriffskosten`: _{self.Cost}_" \
               f"\n`Schaden`: _{self.Damage}_\n`Leben`: _{self.Health}_\n`Element`: _{self.Element}_\n`Resistenz`: _{self.Resistance}_\n`Seltenheit`: **{self.GetRarity()}**\n"

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]

    def debug(self):
        x = [{"Name": self.Name, "Motto": self.Motto},
             {"KDTN": {"Mana": self.Mana, "Kosten": self.Cost, "Schaden": self.Damage, "Leben": self.Health}},
             {"KDTN": {"Element": self.Element, "Resistenz": self.Resistance}},
             {"KDTN": {"Seltenheit - Integer": self.Rarity, "Seltenheit - String": self.GetRarity()}}]
        return x

    def GetRarity(self):
        return "Exotisch" if self.Rarity == 4 else (
            "Legendär" if self.Rarity == 3 else ("Selten" if self.Rarity == 2 else "Normal"))

    def fight_data(self, damage=None):
        y = f"\n`Schaden`: {damage}" if damage is not None else ""
        x = f"`Leben`: {self.Health}\n`Mana`: {self.Mana}{y}"
        return x

    def post_fight_data(self):
        return f"`Mana`: {self.Mana}\n`Angriffskosten`: {self.Cost}\n`Angriffsschaden`: {self.Damage}"

    def price(self):
        base_price = YAML.GET("Shop", "Preis")
        return base_price[3] if self.Rarity == 4 else (
            base_price[2] if self.Rarity == 3 else (base_price[1] if self.Rarity == 2 else base_price[0]))

    def avatar(self):
        return self.Avatar[(int(self.Rarity) - 1)]

    def random_Energie(self):
        rnum = random.randint(YAML.GET("Random_Energie", "Start"), YAML.GET("Random_Energie", "End"))

        if self.Rarity == 4:
            bonus = YAML.GET("Random_Energie", "Bonus")[3]
        if self.Rarity == 3:
            bonus = YAML.GET("Random_Energie", "Bonus")[2]
        if self.Rarity == 2:
            bonus = YAML.GET("Random_Energie", "Bonus")[1]
        if self.Rarity == 1:
            bonus = YAML.GET("Random_Energie", "Bonus")[0]

        self.Mana += int(rnum + bonus)

    def update_Stats(self):
        print(self.Health, self.Data.Leben)
        if self.Health == self.Data.Leben:
            if self.Rarity == 1:
                self.Health = (int(self.Data.Leben + int(YAML.GET("Update_Stats", 1)[0])))
                self.Mana = (int(self.Data.Mana + int(YAML.GET("Update_Stats", 1)[1])))
                print("Stufe 1")
                return
            elif self.Rarity == 2:
                self.Health = (int(self.Data.Leben + int(YAML.GET("Update_Stats", 2)[0])))
                self.Mana = (int(self.Data.Mana + int(YAML.GET("Update_Stats", 2)[1])))
                print("Stufe 2")
                return
            elif self.Rarity == 3:
                self.Health = (int(self.Data.Leben + int(YAML.GET("Update_Stats", 3)[0])))
                self.Mana = (int(self.Data.Mana + int(YAML.GET("Update_Stats", 3)[1])))
                print("Stufe 3")
                return
            elif self.Rarity == 4:
                self.Health = (int(self.Data.Leben + int(YAML.GET("Update_Stats", 4)[0])))
                self.Mana = (int(self.Data.Mana + int(YAML.GET("Update_Stats", 4)[1])))
                print("Stufe 4")
                return

        else:
            print("ELSE")
            return

    def tuple_Shimari(self):
        x = (self.ID, self.Rarity)
        return x


class Shimari(ShimariBASE):


    @staticmethod
    def fight(Shimari1: ShimariBASE, Shimari2: ShimariBASE, Attack: int):
        Shimari1.update_Stats()
        Shimari2.update_Stats()

        if int(Shimari2["Health"]) <= 0:
            return False

        elif int(Shimari1["Mana"]) < 1:
            return False

        else:

            Chance = random.randint(1, 100)


            bonus = YAML.GET("Bonus_Stats", "Resistance") if Shimari1.Element == Shimari2.Resistance else \
                (YAML.GET("Bonus_Stats", 1) if Attack == 1 else (
                    YAML.GET("Bonus_Stats", 2) if Attack == 2 else YAML.GET("Bonus_Stats", 3)))

            Health = int(Shimari2["Health"]) - (int(Shimari1["Damage"][Attack - 1]) + int(bonus))

            Energie = int(Shimari1["Mana"]) - int(Shimari1["Cost"][Attack - 1])

            if Chance <= YAML.GET("Failure_Rate", "Chance"):
                Shimari1["Mana"] = Energie

                data = Object()
                data.damage = "0, Geblockt!"

                return data

            else:

                Shimari2["Health"] = Health
                Shimari1["Mana"] = Energie

                data = Object()
                data.damage = int(Shimari1["Damage"][Attack - 1]) + int(bonus)

                return data
