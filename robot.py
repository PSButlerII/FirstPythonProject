from weapon import Weapon

class Robot:
    def __init__(self, name, health, type_of_weapon, power_level):
        self.name = name
        self.health = health
        self.weapon_type = Weapon.type_of_weapon
        self.power_level = power_level

    # def set_name(self):
    #    kr999 = Robot(KR999,300,type_of_weapon=Weapon.weapon_type,power_level=400)
    #    kr998=Robot(KR998,300,type_of_weapon=Weapon.weapon_type,power_level=400)
    #    kr997=Robot(KR997,300,type_of_weapon=Weapon.weapon_type,power_level=400)
    #    kr996=Robot(KR996,300,type_of_weapon=Weapon.weapon_type,power_level=400)
    #    kr995=Robot(KR995,300,type_of_weapon=Weapon.weapon_type,power_level=400)

    def attack(self,dinosaur):

