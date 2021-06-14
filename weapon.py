import random

class Weapon:
    def __init__(self, name, attack_power):
        self.type_of_weapon = []
        self.weapon_name = name
        self.attack_power = int('attack_power')
        self.weapon_type()

    def weapon_type(self):
        m242_bushmaster_chain_gun = Weapon(M242_Bushmaster_Chain_Gun, 900)
        m2_browning = Weapon(M2_Browning, 600)
        xm_25_grenade_launcher = Weapon(XM_25_Grenade_Launcher, 300)
        self.type_of_weapon.append(m242_bushmaster_chain_gun)
        self.type_of_weapon.append(m2_browning)
        self.type_of_weapon.append(xm_25_grenade_launcher)
        select_weapon = random.choice(type_of_weapon)
        print(select_weapon)
