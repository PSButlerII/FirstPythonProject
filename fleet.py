from robot import Robot


class Fleet:
    def __init__(self):
        self.robot_list = []
        self.create_fleet()

    def create_fleet(self):
        kr999 = Robot(KR999, 300, type_of_weapon=Weapon.weapon_type, power_level=400)
        kr998 = Robot(KR998, 300, type_of_weapon=Weapon.weapon_type, power_level=400)
        kr997 = Robot(KR997, 300, type_of_weapon=Weapon.weapon_type, power_level=400)
        kr996 = Robot(KR996, 300, type_of_weapon=Weapon.weapon_type, power_level=400)
        kr995 = Robot(KR995, 300, type_of_weapon=Weapon.weapon_type, power_level=400)
        select_robot = random.choice(self.robot_list)
        print(select_robot)