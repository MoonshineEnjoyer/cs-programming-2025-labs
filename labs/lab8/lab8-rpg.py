import random
import sys


class Character:
    def __init__(self, race, hp, attack, defense, agility, height, weight):
        self.race = race
        self.hp = hp
        self.max_hp = hp
        self.base_attack = attack
        self.base_defense = defense
        self.agility = agility
        self.height = height
        self.weight = weight
        self.level = 1
        self.exp = 0
        self.exp_to_next = 30
        self.skill_points = 0
        self.inventory = []
        self.weapon = None
        self.armor = None
        self.can_level_up = False  # Флаг для возможности прокачки

    @property
    def attack(self):
        return self.base_attack + (self.weapon["value"] if self.weapon else 0)

    @property
    def defense(self):
        return self.base_defense + (self.armor["value"] if self.armor else 0)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def gain_exp(self, amount):
        self.exp += amount
        print(f"Получено {amount} опыта.")
        if self.exp >= self.exp_to_next:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp -= self.exp_to_next
        self.exp_to_next = 30 + (self.level - 1) * 30
        self.skill_points += 1
        print(f"Поздравляем! Вы достигли {self.level} уровня!")
        print(f"Доступно очков прокачки: {self.skill_points}")

    def add_item(self, item):
        if len(self.inventory) < 8:
            self.inventory.append(item)
            print(f"Добавлено в инвентарь: {item['name']}")
            return True
        else:
            print("Инвентарь полон! Выберите что делать:")
            print("1 - Выбросить предмет из инвентаря")
            print("2 - Пропустить этот предмет")

            try:
                choice = int(input("Ваш выбор: "))
                if choice == 1:
                    self.show_inventory()
                    item_choice = int(input("Номер предмета для удаления: "))
                    if 1 <= item_choice <= len(self.inventory):
                        removed = self.inventory.pop(item_choice - 1)
                        print(f"Выброшено: {removed['name']}")
                        self.inventory.append(item)
                        print(f"Добавлено: {item['name']}")
                        return True
                    else:
                        print("Неверный номер. Предмет пропущен.")
                        return False
                elif choice == 2:
                    print("Предмет пропущен.")
                    return False
                else:
                    print("Неверный выбор. Предмет пропущен.")
                    return False
            except:
                print("Неверный ввод. Предмет пропущен.")
                return False

    def show_inventory(self):
        if not self.inventory:
            print("Инвентарь пуст!")
            return
        print("\n--- Инвентарь ---")
        for i, item in enumerate(self.inventory, 1):
            item_type = ""
            if item["type"] == "potion":
                item_type = "[Зелье]"
            elif item["type"] == "weapon":
                item_type = "[Оружие]"
            elif item["type"] == "armor":
                item_type = "[Броня]"
            print(f"{i}. {item_type} {item['name']} - {item['description']}")

    def discard_item(self):
        """Выбросить предмет из инвентаря"""
        if not self.inventory:
            print("Инвентарь пуст! Нечего выбрасывать.")
            return False

        self.show_inventory()
        try:
            item_choice = int(input("Номер предмета для выбрасывания (0 для отмены): "))
            if item_choice == 0:
                print("Отмена.")
                return False
            elif 1 <= item_choice <= len(self.inventory):
                removed = self.inventory.pop(item_choice - 1)
                print(f"Выброшено: {removed['name']}")
                print(f"В инвентаре осталось {len(self.inventory)}/8 предметов.")
                return True
            else:
                print("Неверный номер предмета.")
                return False
        except ValueError:
            print("Неверный ввод. Введите число.")
            return False

    def use_item(self, item_index):
        if 0 <= item_index < len(self.inventory):
            item = self.inventory[item_index]
            if item["type"] == "potion":
                self.heal(item["value"])
                print(f"Использовано {item['name']}. Восстановлено {item['value']} HP.")
                print(f"Текущее HP: {self.hp}/{self.max_hp}")
                del self.inventory[item_index]
                return True
            else:
                print("Этот предмет нельзя использовать как зелье.")
                return False
        else:
            print("Неверный номер предмета.")
            return False

    def equip_item(self, item_index):
        if 0 <= item_index < len(self.inventory):
            item = self.inventory[item_index]
            if item["type"] == "weapon":
                if self.weapon:
                    self.inventory.append(self.weapon)
                    print(f"Снято оружие: {self.weapon['name']}")
                self.weapon = item
                self.inventory.remove(item)
                print(f"Экипировано оружие: {item['name']}")
                print(f"Теперь ваша атака: {self.attack}")
                return True
            elif item["type"] == "armor":
                if self.armor:
                    self.inventory.append(self.armor)
                    print(f"Снята броня: {self.armor['name']}")
                self.armor = item
                self.inventory.remove(item)
                print(f"Экипирована броня: {item['name']}")
                print(f"Теперь ваша защита: {self.defense}")
                return True
            else:
                print("Это нельзя экипировать (только оружие или броня).")
                return False
        else:
            print("Неверный номер предмета.")
            return False

    def show_stats(self):
        print(f"\n--- Характеристики персонажа ---")
        print(f"Раса: {self.race}")
        print(f"Уровень: {self.level} | Опыт: {self.exp}/{self.exp_to_next}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(
            f"Атака: {self.base_attack} + {self.weapon['value'] if self.weapon else 0} = {self.attack}"
        )
        print(
            f"Защита: {self.base_defense} + {self.armor['value'] if self.armor else 0} = {self.defense}"
        )
        print(f"Ловкость: {self.agility}")
        print(f"Рост: {self.height} см | Вес: {self.weight} кг")
        print(f"Предметов в инвентаре: {len(self.inventory)}/8")
        print(f"Доступно очков прокачки: {self.skill_points}")
        if self.weapon:
            print(f"Оружие: {self.weapon['name']} (+{self.weapon['value']} к атаке)")
        if self.armor:
            print(f"Броня: {self.armor['name']} (+{self.armor['value']} к защите)")


class Enemy:
    def __init__(self, name, hp, attack, defense, exp, floor):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.exp = exp
        self.floor = floor

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def calculate_damage(self, target_defense):
        """Расчет урона с учетом критического удара"""
        damage = max(1, self.attack - target_defense // 2)

        # 5% шанс критического удара для врага
        if random.random() < 0.05:  # 5% шанс
            damage = int(damage * 1.5)  # Умножаем урон в 1.5 раза
            return damage, True  # Возвращаем урон и флаг критического удара

        return damage, False  # Обычный урон без крита


class Game:
    def __init__(self):
        self.player = None
        self.current_room = 0
        self.floor = 1
        self.max_floors = 5
        self.rooms_per_floor = 6
        self.visible_chance = 0.5

    def create_character(self):
        print("\n=== ВЫБОР РАСЫ ===")
        print("\nДоступные расы:")
        print("1 - ЧЕЛОВЕК")
        print("   HP: 80-120")
        print("   Атака: 10-15")
        print("   Защита: 5-10")
        print("   Ловкость: 5-10")

        print("2 - ЭЛЬФ")
        print("   HP: 70-100")
        print("   Атака: 12-18")
        print("   Защита: 3-8")
        print("   Ловкость: 10-15")

        print("3 - ДВОРФ")
        print("   HP: 100-150")
        print("   Атака: 8-14")
        print("   Защита: 8-15")
        print("   Ловкость: 3-7")

        choice = input("Выберите расу (1-3): ")
        if choice == "1":
            race = "Человек"
            hp = random.randint(80, 120)
            attack = random.randint(10, 15)
            defense = random.randint(5, 10)
            agility = random.randint(5, 10)
            height = random.randint(160, 190)
            weight = random.randint(60, 100)
        elif choice == "2":
            race = "Эльф"
            hp = random.randint(70, 100)
            attack = random.randint(12, 18)
            defense = random.randint(3, 8)
            agility = random.randint(10, 15)
            height = random.randint(170, 200)
            weight = random.randint(50, 80)
        elif choice == "3":
            race = "Дворф"
            hp = random.randint(100, 150)
            attack = random.randint(8, 14)
            defense = random.randint(8, 15)
            agility = random.randint(3, 7)
            height = random.randint(130, 160)
            weight = random.randint(70, 120)
        else:
            print("Неверный выбор, по умолчанию выбран Человек.")
            race = "Человек"
            hp = random.randint(80, 120)
            attack = random.randint(10, 15)
            defense = random.randint(5, 10)
            agility = random.randint(5, 10)
            height = random.randint(160, 190)
            weight = random.randint(60, 100)

        self.player = Character(race, hp, attack, defense, agility, height, weight)
        print(f"\nВаш персонаж создан!")
        self.player.show_stats()

    def generate_enemy(self):
        enemy_types = ["Гоблин", "Скелет", "Орк", "Волк", "Зомби", "Тролль", "Хамелеон"]
        name = random.choice(enemy_types)
        hp = random.randint(30, 60) + self.floor * 10
        attack = random.randint(5, 12) + self.floor * 2
        defense = random.randint(2, 8) + self.floor
        exp = 30
        return Enemy(name, hp, attack, defense, exp, self.floor)

    def generate_loot(self):
        loot_types = [
            {
                "type": "potion",
                "name": "Зелье лечения",
                "description": "Восстанавливает 30 HP",
                "value": 30,
            },
            {
                "type": "potion",
                "name": "Большое зелье лечения",
                "description": "Восстанавливает 60 HP",
                "value": 60,
            },
            {
                "type": "weapon",
                "name": "Деревянный меч",
                "description": "Увеличивает атаку на 1",
                "value": 1,
            },
            {
                "type": "weapon",
                "name": "Стальной меч",
                "description": "Увеличивает атаку на 3",
                "value": 3,
            },
            {
                "type": "weapon",
                "name": "Острый топор",
                "description": "Увеличивает атаку на 5",
                "value": 5,
            },
            {
                "type": "armor",
                "name": "Кожаный доспех",
                "description": "Увеличивает защиту на 2",
                "value": 2,
            },
            {
                "type": "armor",
                "name": "Кольчуга",
                "description": "Увеличивает защиту на 3",
                "value": 3,
            },
            {
                "type": "armor",
                "name": "Стальные латы",
                "description": "Увеличивает защиту на 4",
                "value": 4,
            },
        ]
        return random.choice(loot_types)

    def calculate_player_damage(self, enemy_defense):
        """Расчет урона игрока с учетом критического удара"""
        damage = max(1, self.player.attack - enemy_defense // 2)

        # 5% шанс критического удара для игрока
        if random.random() < 0.05:  # 5% шанс
            damage = int(damage * 1.5)  # Умножаем урон в 1.5 раза
            return damage, True  # Возвращаем урон и флаг критического удара

        return damage, False  # Обычный урон без крита

    def combat(self, enemy):
        print(f"\nВы встретили врага: {enemy.name} (Этаж {enemy.floor})!")
        print(f"HP врага: {enemy.hp}/{enemy.max_hp}")

        while enemy.hp > 0 and self.player.hp > 0:
            print("\nВаши действия:")
            print("1 - Атаковать")
            print("2 - Использовать зелье")
            print("3 - Попытаться уклониться")
            choice = input("> ")

            if choice == "1":
                # Расчет урона игрока с учетом возможного критического удара
                damage, is_critical = self.calculate_player_damage(enemy.defense)

                if is_critical:
                    print("КРИТИЧЕСКИЙ УДАР!")
                    print("Ваш урон увеличен в 1.5 раза!")

                enemy.take_damage(damage)
                print(f"Вы нанесли {damage} урона врагу.")
                print(f"HP врага: {enemy.hp}/{enemy.max_hp}")

                if enemy.hp <= 0:
                    print(f"Вы победили {enemy.name}!")
                    self.player.gain_exp(enemy.exp)
                    if random.random() < 0.7:
                        loot = self.generate_loot()
                        if not self.player.add_item(loot):
                            print("Предмет не был добавлен в инвентарь.")
                    break

            elif choice == "2":
                if not self.player.inventory:
                    print("Инвентарь пуст!")
                    continue
                potions = [
                    (i, item)
                    for i, item in enumerate(self.player.inventory, 1)
                    if item["type"] == "potion"
                ]
                if not potions:
                    print("У вас нет зелий!")
                    continue
                print("\nДоступные зелья:")
                for i, (index, item) in enumerate(potions, 1):
                    print(f"{i}. {item['name']} - {item['description']}")

                try:
                    potion_choice = int(input("Номер зелья для использования: "))
                    if 1 <= potion_choice <= len(potions):
                        actual_index = potions[potion_choice - 1][0] - 1
                        self.player.use_item(actual_index)
                    else:
                        print("Неверный номер.")
                        continue
                except:
                    print("Неверный ввод.")
                    continue

            elif choice == "3":
                dodge_chance = self.player.agility / 20
                if random.random() < dodge_chance:
                    print("Вы успешно уклонились!")
                    continue
                else:
                    print("Уклонение не удалось!")

            else:
                print("Неверный выбор.")
                continue

            if enemy.hp > 0:
                # Расчет урона врага с учетом возможного критического удара
                damage, is_critical = enemy.calculate_damage(self.player.defense)

                if is_critical:
                    print("Враг наносит КРИТИЧЕСКИЙ УДАР!")
                    print("Его урон увеличен в 1.5 раза!")

                self.player.take_damage(damage)
                print(f"Враг атаковал и нанес {damage} урона.")
                print(f"Ваше HP: {self.player.hp}/{self.player.max_hp}")

                if self.player.hp <= 0:
                    self.game_over()
                    return

    def game_over(self):
        """Обработка смерти персонажа"""
        print("         ВЫ ПОГИБЛИ!             ")

        print("\nЧто вы хотите сделать?")
        print("1 - Начать новую игру")
        print("2 - Выйти из игры")

        while True:
            choice = input("Ваш выбор: ")
            if choice == "1":
                self.restart_game()
                return
            elif choice == "2":
                print("Спасибо за игру!")
                sys.exit()
            else:
                print("Неверный выбор. Введите 1 или 2.")

    def restart_game(self):
        """Перезапуск игры с самого начала"""
        # Сброс всех игровых параметров
        self.player = None
        self.current_room = 0
        self.floor = 1

        # Создание нового персонажа
        self.create_character()
        input("\nНажмите Enter, чтобы войти в подземелье...")
        print("\nВы входите в подземелье...")

    def rest_room(self):
        print("\nВы вошли в комнату отдыха.")
        print("Здесь безопасно. Вы можете отдохнуть и прокачать характеристики.")

        # Включаем возможность прокачки
        self.player.can_level_up = True

        self.player.heal(self.player.max_hp // 2)
        print(f"Вы отдохнули. HP: {self.player.hp}/{self.player.max_hp}")

        if self.player.skill_points > 0:
            print("У вас есть нераспределенные очки прокачки!")
            self.level_up_menu()
        else:
            print("У вас нет очков для прокачки.")

        # Покидаем комнаты отдыха - выключаем возможность прокачки
        self.player.can_level_up = False
        print("Вы покидаете комнату отдыха.")

    def treasure_room(self):
        print("\nВы нашли комнату с сундуком!")
        loot = self.generate_loot()
        if not self.player.add_item(loot):
            print("Вы решили не брать предмет.")

    def level_up_menu(self):
        if not self.player.can_level_up:
            print("Прокачка характеристик доступна только в комнатах отдыха!")
            return

        while self.player.skill_points > 0:
            print(f"\n=== ПРОКАЧКА ХАРАКТЕРИСТИК ===")
            print(f"Очков прокачки: {self.player.skill_points}")
            print(f"1 - +10 к максимальному HP (текущее: {self.player.max_hp})")
            print(f"2 - +2 к атаке (текущая: {self.player.base_attack})")
            print(f"3 - +2 к защите (текущая: {self.player.base_defense})")
            print(f"4 - +2 к ловкости (текущая: {self.player.agility})")
            print("0 - Выйти")

            choice = input("Ваш выбор: ")
            if choice == "0":
                print(f"У вас осталось {self.player.skill_points} очков прокачки.")
                break
            elif choice == "1":
                self.player.max_hp += 10
                self.player.skill_points -= 1
                print(
                    f"Максимальное HP увеличено на 10. Текущее HP: {self.player.hp}/{self.player.max_hp}"
                )
            elif choice == "2":
                self.player.base_attack += 2
                self.player.skill_points -= 1
                print(
                    f"Базовая атака увеличена на 2. Текущая атака: {self.player.attack}"
                )
            elif choice == "3":
                self.player.base_defense += 2
                self.player.skill_points -= 1
                print(
                    f"Базовая защита увеличена на 2. Текущая защита: {self.player.defense}"
                )
            elif choice == "4":
                self.player.agility += 2
                self.player.skill_points -= 1
                print(
                    f"Ловкость увеличена на 2. Текущая ловкость: {self.player.agility}"
                )
            else:
                print("Неверный выбор.")

            if self.player.skill_points == 0:
                print("Все очки прокачки распределены!")

    def choose_direction(self):
        self.current_room += 1
        if self.current_room > self.rooms_per_floor:
            self.floor += 1
            self.current_room = 1
            if self.floor <= self.max_floors:
                print(f"\n=== Вы достигли этажа {self.floor}! ===")
            else:
                print(f"\n=== ПОЗДРАВЛЯЕМ! Вы прошли все {self.max_floors} этажей! ===")
                print("Игра завершена!")
                self.game_completed()
                return None

        print(
            f"\nПеред вами развилка. (Этаж {self.floor}, Комната {self.current_room}/{self.rooms_per_floor})"
        )

        left_type = random.choice(["enemy", "rest", "treasure"])
        right_type = random.choice(["enemy", "rest", "treasure"])

        left_desc = (
            "???"
            if random.random() > self.visible_chance
            else self.room_description(left_type)
        )
        right_desc = (
            "???"
            if random.random() > self.visible_chance
            else self.room_description(right_type)
        )

        print(f"(1) Слева: {left_desc}")
        print(f"(2) Справа: {right_desc}")

        while True:
            choice = input("Куда пойти? (1/2) > ")
            if choice == "1":
                return left_type
            elif choice == "2":
                return right_type
            else:
                print("Неверный выбор.")

    def game_completed(self):
        """Обработка завершения игры (прохождения всех этажей)"""
        print("ВЫ УСПЕШНО ПРОШЛИ ВСЕ ЭТАЖИ ПОДЗЕМЕЛЬЯ!")
        print(f"\nИтоговые характеристики:")
        self.player.show_stats()

        print("\nЧто вы хотите сделать?")
        print("1 - Начать новую игру")
        print("2 - Выйти из игры")

        while True:
            choice = input("Ваш выбор: ")
            if choice == "1":
                print("НАЧИНАЕМ НОВОЕ ПРИКЛЮЧЕНИЕ!")
                self.restart_game()
                return
            elif choice == "2":
                print("Спасибо за игру!")
                sys.exit()
            else:
                print("Неверный выбор. Введите 1 или 2.")

    def room_description(self, room_type):
        if room_type == "enemy":
            return "Враг!"
        elif room_type == "rest":
            return "Комната отдыха"
        elif room_type == "treasure":
            return "Сундук"

    def room_event(self, room_type):
        if room_type == "enemy":
            enemy = self.generate_enemy()
            self.combat(enemy)
        elif room_type == "rest":
            self.rest_room()
        elif room_type == "treasure":
            self.treasure_room()

    def main_menu(self):
        while True:
            print("\n=== ГЛАВНОЕ МЕНЮ ===")
            print("1 - Продолжить исследование")
            print("2 - Посмотреть характеристики")
            print("3 - Просмотреть инвентарь")
            print("4 - Экипировать оружие/броню")
            print("5 - Использовать зелье")
            print("6 - Выбросить предмет")
            print("0 - Выйти из игры")

            choice = input("> ")
            if choice == "1":
                room_type = self.choose_direction()
                if room_type is None:  # Игра завершена
                    continue
                self.room_event(room_type)
            elif choice == "2":
                self.player.show_stats()
            elif choice == "3":
                self.player.show_inventory()
            elif choice == "4":
                if not self.player.inventory:
                    print("Инвентарь пуст!")
                    continue

                equipable_items = [
                    (i, item)
                    for i, item in enumerate(self.player.inventory, 1)
                    if item["type"] in ["weapon", "armor"]
                ]

                if not equipable_items:
                    print("У вас нет оружия или брони для экипировки!")
                    continue

                print("\nДоступное оружие и броня:")
                for i, (index, item) in enumerate(equipable_items, 1):
                    item_type = "Оружие" if item["type"] == "weapon" else "Броня"
                    print(f"{i}. [{item_type}] {item['name']} - {item['description']}")

                try:
                    equip_choice = int(input("Номер предмета для экипировки: "))
                    if 1 <= equip_choice <= len(equipable_items):
                        actual_index = equipable_items[equip_choice - 1][0] - 1
                        self.player.equip_item(actual_index)
                    else:
                        print("Неверный номер.")
                except:
                    print("Неверный ввод.")

            elif choice == "5":
                if not self.player.inventory:
                    print("Инвентарь пуст!")
                    continue

                potions = [
                    (i, item)
                    for i, item in enumerate(self.player.inventory, 1)
                    if item["type"] == "potion"
                ]
                if not potions:
                    print("У вас нет зелий!")
                    continue

                print("\nДоступные зелья:")
                for i, (index, item) in enumerate(potions, 1):
                    print(f"{i}. {item['name']} - {item['description']}")

                try:
                    potion_choice = int(input("Номер зелья для использования: "))
                    if 1 <= potion_choice <= len(potions):
                        actual_index = potions[potion_choice - 1][0] - 1
                        self.player.use_item(actual_index)
                    else:
                        print("Неверный номер.")
                except:
                    print("Неверный ввод.")

            elif choice == "6":
                # Выбросить предмет из инвентаря
                self.player.discard_item()

            elif choice == "0":
                print("Спасибо за игру!")
                sys.exit()
            else:
                print("Неверный выбор.")

    def run(self):
        print("=== ТЕКСТОВАЯ RPG: ===")
        print(f"Цель: пройти все {self.max_floors} этажей подземелья")

        self.create_character()
        input("\nНажмите Enter, чтобы войти в подземелье...")
        print("\nВы входите в подземелье...")
        self.main_menu()


if __name__ == "__main__":
    game = Game()
    game.run()
