from dinosaurs import Dinosaur
import random


class Herd:
    def __init__(self):
        self.dinosaur_type = dinosaur_list.get()
        self.dinosaur_list = []
        self.create_herd()

    def create_herd(self):
        spinosaurus = Dinosaur(Spinosaurus, 100, 1000, 200)
        tyrannosaurus = Dinosaur(Tyrannosaurus, 100, 950, 200)
        giganotosaurus = Dinosaur(Giganotosaurus, 100, 900, 200)
        oxalaia = Dinosaur(Oxalaia, 100, 850, 200)
        carcharodontosaurus = Dinosaur(Carcharodontosaurus, 100, 800, 200)
        godzilla = Dinosaur(Godzilla, 101, 1001, 201)
        self.dinosaur_list.append(spinosaurus)
        self.dinosaur_list.append(tyrannosaurus)
        self.dinosaur_list.append(giganotosaurus)
        self.dinosaur_list.append(oxalaia)
        self.dinosaur_list.append(carcharodontosaurus)
        self.dinosaur_list.append(godzilla)
        select_dinosaur = random.choice(dinosaur_list)
        selected_dinosaur = select_dinosaur()
        print(select_dinosaur, selected_dinosaur)

        # dinosaur_list = {'1': {'name': Spinosaurus, 'attack_power': 200, 'energy': 1000, 'health': 100},
        # '2':{'name':Tyrannosaurus, 'attack_power':200, 'energy':950, 'health':100},
        # '3':{'name':Giganotosaurus, 'attack_power':200, 'energy':900, 'health':100},
        # '4':{'name':Oxalaia_quilombensis, 'attack_power':200, 'energy':800, 'health':100},
        # '5':{'name':Carcharodontosaurus, 'attack_power':200, 'energy':1000, 'health':100},
        # '6':{'name':Godzilla, 'attack_power':200, 'energy':1000, 'health':100}}
