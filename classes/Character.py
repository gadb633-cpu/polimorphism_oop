
class Character:
    def __init__(self,name,health):
        self.name = name
        self.life = health
    def attack_power(self):
        raise NotImplementedError("error")
        