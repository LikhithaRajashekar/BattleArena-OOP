from character import Character


class Warrior(Character):

    def attack(self, opponent):
        damage = 20
        opponent.take_damage(damage)
        print(f"{self.name} attacks {opponent.name} with a sword!")

    def special_attack(self, opponent):
        damage = 35
        opponent.take_damage(damage)
        print(f"{self.name} uses POWER STRIKE on {opponent.name}!")


class Mage(Character):

    def attack(self, opponent):
        damage = 15
        opponent.take_damage(damage)
        print(f"{self.name} attacks {opponent.name} with magic!")

    def special_attack(self, opponent):
        damage = 40
        opponent.take_damage(damage)
        print(f"{self.name} casts FIREBALL on {opponent.name}!")


class Archer(Character):

    def attack(self, opponent):
        damage = 18
        opponent.take_damage(damage)
        print(f"{self.name} attacks {opponent.name} with an arrow!")

    def special_attack(self, opponent):
        damage = 30
        opponent.take_damage(damage)
        print(f"{self.name} uses MULTI-SHOT on {opponent.name}!")