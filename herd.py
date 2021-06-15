from dinosaurs import Dinosaur
import random


class Herd:
    def __init__(self):
        self.max_dinosaurs = 5
        self.dinosaur_list = []

    def add_herd(self):
        if len(self.dinosaur_list) < self.max_dinosaurs:
            self.dinosaur_list.append(Dinosaur)
            spinosaurus = Dinosaur(Spinosaurus, 200, 950, 200)
            tyrannosaurus = Dinosaur(Tyrannosaurus, 200, 950, 200)
            giganotosaurus = Dinosaur(Giganotosaurus, 200, 900, 200)
            oxalaia = Dinosaur(Oxalaia, 200, 850, 200)
            carcharodontosaurus = Dinosaur(Carcharodontosaurus, 100, 800, 200)
            godzilla = Dinosaur(Godzilla, 201, 1001, 201)
