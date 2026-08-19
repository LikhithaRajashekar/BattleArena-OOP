class Battle:

    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2

    def display_characters(self):
        print("\n===== BATTLE CHARACTERS =====")

        self.character1.display_info()

        print()

        self.character2.display_info()

    def start_battle(self):
        print("\n===== BATTLE STARTED =====")
        print(f"{self.character1.name} VS {self.character2.name}")

        turn = 1

        while self.character1.is_alive() and self.character2.is_alive():

            print(f"\n----- Turn {turn} -----")

            if turn % 2 == 1:
                attacker = self.character1
                defender = self.character2
            else:
                attacker = self.character2
                defender = self.character1

            print(f"{attacker.name}'s turn")

            attacker.attack(defender)

            if not defender.is_alive():
                break

            turn += 1

        self.display_winner()

    def display_winner(self):
        print("\n===== BATTLE RESULT =====")

        if self.character1.is_alive():
            print(f"Winner: {self.character1.name}")
        elif self.character2.is_alive():
            print(f"Winner: {self.character2.name}")
        else:
            print("The battle ended in a draw.")