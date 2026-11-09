from classes.Character import Character
class Mage(Character):
    def attack_power(self):
        if self.health > 50:
            return 20
        return 10