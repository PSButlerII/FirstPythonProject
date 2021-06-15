import random
from robot import Robot


class Fleet:
    def __init__(self):
        self.robot_list = []
        self.max_robot = 5

    def create_fleet(self):
        robot_one = Robot(KR999, 300, "M242_Bushmaster_Chain_Gun", 200)
        robot_two = Robot(KR998, 300, "M242_Bushmaster_Chain_Gun", 200)
        robot_three = Robot(KR997, 300, "M242_Bushmaster_Chain_Gun", 200)
        robot_four = Robot(KR996, 300, "M242_Bushmaster_Chain_Gun", 200)
        robot_five = Robot(KR995, 300, "M242_Bushmaster_Chain_Gun", 200)
        select_robot = random.choice(self.robot_list)


