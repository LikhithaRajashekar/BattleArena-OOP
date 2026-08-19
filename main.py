from characters import Warrior, Mage, Archer
from battle import Battle


print("===== BATTLE ARENA =====")

print("\nChoose Character 1:")
print("1. Warrior")
print("2. Mage")
print("3. Archer")

choice1 = input("Enter your choice: ")

print("\nChoose Character 2:")
print("1. Warrior")
print("2. Mage")
print("3. Archer")

choice2 = input("Enter your choice: ")


if choice1 == "1":
    character1 = Warrior("Thor", 120, 1)
elif choice1 == "2":
    character1 = Mage("Merlin", 100, 1)
elif choice1 == "3":
    character1 = Archer("Robin", 110, 1)
else:
    print("Invalid choice for Character 1.")
    exit()


if choice2 == "1":
    character2 = Warrior("Hercules", 120, 1)
elif choice2 == "2":
    character2 = Mage("Gandalf", 100, 1)
elif choice2 == "3":
    character2 = Archer("Legolas", 110, 1)
else:
    print("Invalid choice for Character 2.")
    exit()


battle = Battle(character1, character2)

battle.display_characters()

battle.start_battle()
