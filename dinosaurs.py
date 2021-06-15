class Dinosaur:
    def __init__(self,type,health,energy,attack_power):
        self.dinosaur_type = type
        self.health = health
        self.energy = energy
        self.attack_power = attack_power

    def attack(self, robot):
        robot.health = 300
        robot.health = (self.attack_power/30) - robot.health


