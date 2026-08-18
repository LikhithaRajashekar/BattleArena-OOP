from abc import ABC, abstractmethod


class Character(ABC):

    def __init__(self, name, health, level):
        self.name = name
        self.level = level
        self.__health = health

    @property
    def health(self):
        return self.__health

    def take_damage(self, damage):
        if damage < 0:
            print("Damage cannot be negative.")
            return

        self.__health -= damage

        if self.__health < 0:
            self.__health = 0

        print(f"{self.name} took {damage} damage.")

    def heal(self, amount):
        if amount <= 0:
            print("Healing amount must be positive.")
            return

        self.__health += amount
        print(f"{self.name} healed by {amount} HP.")

    def is_alive(self):
        return self.__health > 0

    def display_info(self):
        print(f"Name   : {self.name}")
        print(f"Level  : {self.level}")
        print(f"Health : {self.health}")

    @abstractmethod
    def attack(self, opponent):
        pass

    @abstractmethod
    def special_attack(self, opponent):
        pass