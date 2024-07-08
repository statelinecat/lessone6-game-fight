

from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack_power_bonus(self):
        pass

    @abstractmethod
    def after_attack_penalty(self):
        pass


class Sword(Weapon):
    def __init__(self, name="Мечом"):
        self.name = name
    def attack_power_bonus(self):
        return 10

    def after_attack_penalty(self):
        return 2

class Axe(Weapon):
    def __init__(self, name="Топором"):
        self.name = name
    def attack_power_bonus(self):
        return 15

    def after_attack_penalty(self):
        return 4

class Hammer(Weapon):
    def __init__(self, name="Молотом"):
        self.name = name
    def attack_power_bonus(self):
        return 20

    def after_attack_penalty(self):
        return 6

class Punch(Weapon):
    def __init__(self, name="Кулаком"):
        self.name = name
    def attack_power_bonus(self):
        return 0

    def after_attack_penalty(self):
        return 0

class Hero:
    def __init__(self, name="Hero"):
        self.name = name
        self.health = 100
        self.attack_power = 20
        self.weapon = None

    def choose_weapon(self, weapon_type):
        if weapon_type.lower() == "1":
            self.weapon = Sword()
        elif weapon_type.lower() == "2":
            self.weapon = Axe()
        elif weapon_type.lower() == "3":
            self.weapon = Hammer()
        elif weapon_type.lower() == "0":
            self.weapon = Punch()
        else:
            print("Неизвестный тип оружия. Выберите 'меч', 'топор' или 'молот'.")
        self.attack_power += self.weapon.attack_power_bonus()

    def attack(self, other):
        if self.weapon:
            other.health -= self.attack_power + self.weapon.attack_power_bonus()
            print(f"{self.name} атакует {other.name} с помощью {self.weapon.name}, "
                  f"оставшееся здоровье {other.health}")
            self.attack_power -= self.weapon.after_attack_penalty()
        else:
            print("Вы не выбрали оружие.")

    def is_alive(self):
        return self.health > 0

import random

class Game:
    def __init__(self, player_name="Player"):
        self.player = Hero(player_name)
        self.computer = Hero("Computer")

    def start(self):
        # self.player.choose_weapon(input("Выберите оружие: 0 - без оружия, 1 - меч, 2 - топор, 3 - молот: "))
        while self.player.is_alive() and self.computer.is_alive():
            self.player.choose_weapon(input("Выберите оружие: 0 - без оружия, 1 - меч, 2 - топор, 3 - молот: "))
            self.computer.choose_weapon(randint(0, 9))
            action = input("Введите '1' для атаки или '0' для выхода: ").strip().lower()
            if action == '1':
                self.player.attack(self.computer)
                if self.computer.is_alive():
                    self.computer.attack(self.player)
            elif action == '0':
                break
            else:
                print("Неверный ввод. Попробуйте снова.")

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")


game = Game()
game.start()
