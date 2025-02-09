import random
# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health

    def attack(self, opponent):
        random_damage = random.randint(int(self.attack_power * 0.8), int(self.attack_power * 1.2))
        opponent.health -= random_damage
        print(f"{self.name} attacks {opponent.name} for {random_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self, amount):
        self.health = amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} healed {amount} and now has {self.health} health.")


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=30)

    def sword(self):
        print(f"{self.name} slashes The Dark Wizard with a sword!")

    def armor(self):
        print(f"{self.name} protects themself with a suit of armor!")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=15) 

    def spell_cast(self):
        print(f"{self.name} casts a spell!")

    def iron_first(self):
        print(f"{self.name} hand glows and they throw a defening punch at The Dark Wizard!")

class Archer(Character):
    def __init__ (self, name):
        super().__init__(name, health=120, attack_power=20)

    def shoot_arrow(self):
        print(f"{self.name} shoots two arrows at The Dark Wizard!")

    def evade(self):
        print(f"{self.name} evades the attacks coming with flips!")

class Paladin(Character):
    def __init__ (self, name):
        super().__init__(name, health=130, attack_power=25)

    def strike(self):
        print(f"{self.name} strikes opponent with lightning!")

    def divine_shield(self):
        if self.health < 20:
            self.attack_power = 0
            self.health -= 2
            print(f"{self.name} protects themself with a divine shield! Health is now {self.health}.")
        else:
            print(f"{self.name} has enough health to fight.")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=10)
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  
    print("4. Paladin")
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Warrior):
                action = input("choose warrior special ability: 1. Sword, 2. Armor:")
                if action == '1':
                    player.sword()
                elif action == '2':
                    player.armor()
            elif isinstance(player, Mage):
                action = input("choose Mage special ability: 1.Cast Spell, 2.Iron Fist:")
                if action == '1':
                    player.spell_cast()
                elif action == '2':
                    player.iron_first()
            elif isinstance(player, Archer):
                action = input("choose Archer special ability: 1.shoot arrow, 2.evade:")
                if action == '1':
                    player.shoot_arrow()
                elif action == '2':
                    player.evade()
            elif isinstance(player, Paladin):
                action = input("Choose Paladin special ability: 1.Holy Strike, 2.Divine Shield:")
                if action == '1':
                    player.strike()
                elif action == '2':
                    player.divine_shield()
        elif choice == '3':
            heal_amount = int(input("enter amount of health to heal:"))
            player.heal(heal_amount)
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            print(f"{wizard.name} has earned the victory!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")
        print(f"congraturlations {player.name} you are the victor!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle (player, wizard)

if __name__ == "__main__":
    main()