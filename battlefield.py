from fleet import Fleet
from herd import Herd
from weapon import Weapon
import random





class  Battlefield:
    def __init__(self, battlezone):
        self.battlezone=battlezone
        self.player = input("Enter your Name")



    def display_welcome(self):

        def run_game():
            choice = input("Left for Dinosaurs or right for Robots! Choose!")
            if choice == 'left':
                self.dinosaur_list.append()
                self.dinosaur_list.create_herd()
                create_herd()


        print("Welcome to the Game!!")
        # battle():void
        # if choice==
        # dino_turn(dinosaur):void

        # robot_turn(robot):void
        # show_dino_opponent_options():void
        # show_robot_opponent_options():void
        # display_winner():void

 # attack_enemy = (attack_power / 28.4) - robot.health


def create_herd(self):
    spinosaurus = Dinosaur(Spinosaurus, 200, 950, 200)
    tyrannosaurus = Dinosaur(Tyrannosaurus, 200, 950, 200)
    giganotosaurus = Dinosaur(Giganotosaurus, 200, 900, 200)
    oxalaia = Dinosaur(Oxalaia, 200, 850, 200)
    carcharodontosaurus = Dinosaur(Carcharodontosaurus, 100, 800, 200)
    godzilla = Dinosaur(Godzilla, 201, 1001, 201)
    self.dinosaur_list.append(spinosaurus)
    self.dinosaur_list.append(tyrannosaurus)
    self.dinosaur_list.append(giganotosaurus)
    self.dinosaur_list.append(oxalaia)
    self.dinosaur_list.append(carcharodontosaurus)
    self.dinosaur_list.append(godzilla)

    def create_fleet(self):
        robot_one = Robot(KR999, 300, "M242_Bushmaster_Chain_Gun", 200)
        robot_two = Robot(KR998, 300, "M242_Bushmaster_Chain_Gun", 200)
        robot_three = Robot(KR997, 300, "M242_Bushmaster_Chain_Gun", 200)
        robot_four = Robot(KR996, 300, "M242_Bushmaster_Chain_Gun", 200)
        robot_five = Robot(KR995, 300, "M242_Bushmaster_Chain_Gun", 200)

        select_robot = random.choice(self.robot_list)

        print(select_robot)

    def weapon_type(self):
        m242_bushmaster_chain_gun = Weapon("M242_Bushmaster_Chain_Gun", 200)
        m2_browning = Weapon("M2_Browning", 200)
        xm_25_grenade_launcher = Weapon("XM_25_Grenade_Launcher", 200)
        self.type_of_weapon.append(m242_bushmaster_chain_gun)
        self.type_of_weapon.append(m2_browning)
        self.type_of_weapon.append(xm_25_grenade_launcher)

        select_weapon = random.choice(self.type_of_weapon)
        print(select_weapon)


