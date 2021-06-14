from weapon import Weapon


class Robot:
    def __init__(self, name, health, type_of_weapon, power_level):
        self.name = name
        self.health = health
        self.weapon_type = Weapon.type_of_weapon
        self.power_level = power_level

    def attack(self, dinosaur):
        pass
