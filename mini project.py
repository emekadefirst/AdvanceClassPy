
from abc import ABC, abstractmethod
import random


class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return f"{self.name} (+{self.damage} DMG)"


class Character(ABC):
    def __init__(self, name, health, attack_power):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack_power = attack_power
        self.weapon = None

    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} equipped {weapon}")

    def attack(self, target):
        bonus = self.weapon.damage if self.weapon else 0
        damage = self.attack_power + bonus + random.randint(1, 5)

        target.take_damage(damage)

        print(
            f"{self.name} attacks {target.name} "
            f"for {damage} damage!"
        )

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)

    def is_alive(self):
        return self.health > 0

    @abstractmethod
    def special_ability(self, target):
        pass

    @abstractmethod
    def character_class(self):
        pass

    def __str__(self):
        weapon_name = self.weapon.name if self.weapon else "None"

        return (
            f"{self.character_class()}: {self.name} | "
            f"HP: {self.health}/{self.max_health} | "
            f"ATK: {self.attack_power} | "
            f"Weapon: {weapon_name}"
        )


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 150, 15)

    def character_class(self):
        return "Warrior"

    def special_ability(self, target):
        damage = self.attack_power * 2
        target.take_damage(damage)

        print(
            f"{self.name} uses Shield Bash "
            f"and deals {damage} damage!"
        )


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 80, 25)
        self.mana = 100

    def character_class(self):
        return "Mage"

    def special_ability(self, target):
        if self.mana < 30:
            print(f"{self.name} does not have enough mana!")
            return

        damage = 50
        self.mana -= 30
        target.take_damage(damage)

        print(
            f"{self.name} casts Fireball "
            f"for {damage} damage! "
            f"(Mana: {self.mana})"
        )


class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, 100, 20)

    def character_class(self):
        return "Rogue"

    def special_ability(self, target):
        damage = self.attack_power * 3
        target.take_damage(damage)

        print(
            f"{self.name} performs Backstab! "
            f"Critical hit for {damage} damage!"
        )


# -----------------------------
# Demo
# -----------------------------
if __name__ == "__main__":

    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)

    warrior = Warrior("Arthur")
    mage = Mage("Merlin")

    warrior.equip_weapon(sword)
    mage.equip_weapon(staff)

    print("\n=== Characters ===")
    print(warrior)
    print(mage)

    print("\n=== Battle Begins ===")

    warrior.attack(mage)
    print(mage)

    mage.special_ability(warrior)
    print(warrior)

    warrior.special_ability(mage)
    print(mage)

    print("\n=== Battle Status ===")
    print(warrior)
    print(mage)