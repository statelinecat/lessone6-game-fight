class Hero:
    def __init__(self, name="Hero"):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name}, оставшееся здоровье {other.health}")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name="Player"):
        self.player = Hero(player_name)
        self.computer = Hero("Computer")

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            action = input("Введите 'a' для атаки или 'q' для выхода: ").strip().lower()
            if action == 'a':
                self.player.attack(self.computer)
                if self.computer.is_alive():
                    self.computer.attack(self.player)
            elif action == 'q':
                break
            else:
                print("Неверный ввод. Попробуйте снова.")

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")


game = Game()
game.start()
