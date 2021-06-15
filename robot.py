from weapon import Weapon


class Robot:
    def __init__(self, name, health,weapon,power_level):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.power_level = power_level

    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.weapon.attack_power
        if self.health < 300:
            self.power_level = self.power_level - 10
