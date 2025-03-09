import random

class Role:
    def __init__(self, name, hp_bonus=0, attack_bonus=0, accuracy_bonus=0):
        self.name = name
        self.hp_bonus = hp_bonus
        self.attack_bonus = attack_bonus
        self.accuracy_bonus = accuracy_bonus

class Hero:
    def __init__(self, name, hp, attack, attack_accuracy, role=None):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.attack_accuracy = attack_accuracy
        self.dodged = False
        self.role = role
        if role:
            self.apply_role_bonuses()

    def apply_role_bonuses(self):
        self.hp += self.role.hp_bonus
        self.attack += self.role.attack_bonus
        self.attack_accuracy += self.role.accuracy_bonus

    def attack_enemy(self, enemy):
        if enemy.dodged:
            print(f"{enemy.name} berhasil menghindar dari serangan {self.name}!")
            enemy.dodged = False  # Reset dodge status after being attacked
        else:
            if random.random() <= self.attack_accuracy:
                enemy.hp -= self.attack
                print(f"{self.name} berhasil menyerang {enemy.name} dengan {self.attack} damage! Sisa HP {enemy.name} adalah {enemy.hp}.")
                if enemy.hp <= 0:
                    print(f"{enemy.name} telah tereliminasi!")
            else:
                print(f"{self.name} gagal menyerang {enemy.name}!")

    def regenerate(self, amount):
        self.hp += amount
        print(f"{self.name} meregenerasi {amount} HP!")

    def is_alive(self):
        return self.hp > 0

class Game:
    def __init__(self, heroes):
        self.heroes = heroes
        self.round = 1

    def play_round(self):
        print(f"Round {self.round}\n==========================================================")
        for hero in self.heroes:
            hp_display = hero.hp if hero.is_alive() else "dead"
            attack_display = hero.attack if hero.is_alive() else "dead"
            print(f"{hero.name} [{hp_display}|{attack_display}]")

        if all(not hero.is_alive() for hero in self.heroes):
            return

        for hero in self.heroes:
            if hero.is_alive():
                action = self.get_valid_input(f"{hero.name}, pilih aksi: 1. Attack 2. Heal 3. Dodge\n", [1, 2, 3])
                if action == 1:
                    target = self.choose_target(hero)
                    if target:
                        hero.attack_enemy(target)
                elif action == 2:
                    hero.regenerate(10)  # You can adjust the heal amount as needed
                elif action == 3:
                    hero.dodged = True
                    print(f"{hero.name} menghindar dari serangan!")

        self.round += 1

    def choose_target(self, attacker):
        alive_heroes = [hero for hero in self.heroes if hero.is_alive() and hero != attacker]
        if not alive_heroes:
            return None
        print("Pilih target:")
        for i, hero in enumerate(alive_heroes):
            print(f"{i + 1}. {hero.name} [{hero.hp}|{hero.attack}]")
        target_index = self.get_valid_input("", range(1, len(alive_heroes) + 1)) - 1
        return alive_heroes[target_index]

    def start_game(self):
        while any(hero.is_alive() for hero in self.heroes):
            self.play_round()
            alive_heroes = [hero for hero in self.heroes if hero.is_alive()]
            if len(alive_heroes) == 1:
                print(f"{alive_heroes[0].name} victory!")
                return

        alive_heroes = [hero for hero in self.heroes if hero.is_alive()]
        if alive_heroes:
            print(f"{alive_heroes[0].name} menang!")
        else:
            print("Tidak ada pemenang!")

    def get_valid_input(self, prompt, valid_options):
        while True:
            try:
                choice = int(input(prompt))
                if choice in valid_options:
                    return choice
                else:
                    print("Input invalid, coba lagi.")
            except ValueError:
                print("Input invalid, coba lagi.")

def create_heroes():
    assassin = Role("Assassin", attack_bonus=200) #mengisi hanya attack_bonus dengan 200 dan di passing ke role yaitu class pada line 3
    tank = Role("Tank", hp_bonus=400)
    marksman = Role("Marksman", attack_bonus=100, accuracy_bonus=0.1)

    predefined_heroes = [
        Hero("Zilong", 2100, 400, 0.6, assassin),
        Hero("Layla", 2000, 600, 0.8, marksman),
        Hero("Gatotkaca", 3000, 300, 0.6, tank),
        Hero("Kagura", 2000, 500, 0.9),
        Hero("Ling", 2100, 500, 0.8, assassin),
        Hero("Angela", 2500, 200, 0.8, tank)
    ]
            
    print("Draft Pick:")
    for i, hero in enumerate(predefined_heroes):
        print(f"{i + 1}. {hero.name} (HP: {hero.hp}, Attack: {hero.attack}, Accuracy: {hero.attack_accuracy * 100:.1f}%)")

    heroes = []
    num_heroes = Game.get_valid_input(Game, "Masukkan jumlah player (2-6): ", range(2, 7))
    selected_indices = set()
    for i in range(num_heroes):
        while True:
            choice = Game.get_valid_input(Game, f"Slot {i + 1} (1-6): ", range(1, 7)) - 1
            if choice not in selected_indices:
                selected_indices.add(choice)
                heroes.append(predefined_heroes[choice])
                break
            else:
                print("Hero sudah dipilih, coba lagi.")
    return heroes

if __name__ == "__main__":
    while True:
        heroes = create_heroes()
        game = Game(heroes)
        game.start_game()
        while True:
            play_again = input("Ingin bermain lagi? (y/n): ").strip().lower()
            if play_again in ['y', 'n']:
                break
            else:
                print("Input invalid, coba lagi.")
        if play_again != 'y':
            print("Terima kasih telah bermain!")
            break