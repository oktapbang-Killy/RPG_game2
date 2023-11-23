
"""День проекта 2
Файлы и операционная система модуль OS
берём старый проект и добавляем функциональность с файлами и операционной системой"""
# 23.11.2023 проект 2, доработать игру используя новые знания, добавить новый функционал
import random
import json
class Character:
    def __init__(self, name):
        self.name = name
        self.lives = 5
        self.coins = 30
    
    def display_info(self):
        print(f"Имя: {self.name}")
        print(f"Жизни: {self.lives}")
        print(f"Монеты: {self.coins}")
    
    def encounter_enemy(self):
        enemy_chance = random.random()
        if enemy_chance < 0.8:
            print("Тебя атаковал враг!")
            if random.random() < 0.3:
                print("Ты победил врага, собрав лут, ты обнаружил 20 монет!")
                self.coins += 20
                self.lives += 1
            else:
                print("Враг оказался сильнее. Ты погиб.")
                self.lives -= 1
        else:
            print("Врага не обнаружено. Тебе повезло!")

# Начало игры
print("Добро пожаловать в игру!")
while True: # наконецто удалось зациклить игру
    start_new_game = input("Хотите начать новую игру? (да/нет): ")
    if start_new_game == "да":
        print("Приветствую тебя авантюрист!")
        player_name = input("Как тебя зовут? (введите имя) ")
        player = Character(player_name)
        print(f"Приветствую, {player.name}!")
        # записываю json
        while player.lives > 0:
            player.encounter_enemy()
            player.display_info()
            player_info = { # обновляю json
                "name": player.name,
                "lives": player.lives,
                "coins": player.coins
            }

            with open("player_info.json", "w") as file:
                json.dump(player_info, file)

        print("Game OVER. Таши жизни закончились.")
        #break