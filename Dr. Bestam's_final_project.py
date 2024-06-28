import random
import sqlite3

class Food:
    def __init__(self, name: str, raw_material: list):
        self.name = name
        self.raw_material = raw_material

    def __str__(self):
        return f'name of this food: {self.name}\nRaw material: {self.raw_material}'

class Management:
    def __init__(self, db_name="food_management.db"):
        self.foods_list = []
        self.raw_material_dic = dict()
        self.list_situavation = {
            'shanbe': {'nahar': None, 'sham': None},
            'yekshanbe': {'nahar': None, 'sham': None},
            'doshanbe': {'nahar': None, 'sham': None},
            'seshanbe': {'nahar': None, 'sham': None},
            'charshanbe': {'nahar': None, 'sham': None},
            'panjshanbe': {'nahar': None, 'sham': None},
            'jome': {'nahar': None, 'sham': None}
        }
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS food (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL UNIQUE)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS raw_material (
                            id INTEGER PRIMARY KEY,
                            food_id INTEGER,
                            material TEXT NOT NULL,
                            FOREIGN KEY(food_id) REFERENCES food(id))''')
        self.conn.commit()

    def add_food(self, food):
        self.foods_list.append(food)
        cursor = self.conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO food (name) VALUES (?)", (food.name,))
        food_id = cursor.execute("SELECT id FROM food WHERE name=?", (food.name,)).fetchone()[0]
        for material in food.raw_material:
            cursor.execute("INSERT INTO raw_material (food_id, material) VALUES (?, ?)", (food_id, material))
            self.raw_material_dic.update({material: 0})
        self.conn.commit()

    def remove_food(self, food):
        self.foods_list.remove(food)
        cursor = self.conn.cursor()
        food_id = cursor.execute("SELECT id FROM food WHERE name=?", (food.name,)).fetchone()[0]
        cursor.execute("DELETE FROM food WHERE id=?", (food_id,))
        cursor.execute("DELETE FROM raw_material WHERE food_id=?", (food_id,))
        self.conn.commit()

    def show_foods(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT food.name, group_concat(raw_material.material, ', ') FROM food JOIN raw_material ON food.id = raw_material.food_id GROUP BY food.id")
        foods = cursor.fetchall()
        for food in foods:
            print(f'name of this food: {food[0]}\nRaw material: {food[1]}')
            print('-'*10)

    def buy_list(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT material FROM raw_material")
        materials = cursor.fetchall()
        for material in materials:
            print(material[0])

    def barname_ghazaei(self):
        lenth_of_food = len(self.foods_list)
        if lenth_of_food == 0:
            print("No foods available.")
            return

        week = [
            'shanbe',
            'yekshanbe',
            'doshanbe',
            'seshanbe',
            'charshanbe',
            'panjshanbe',
            'jome'
        ]
        vaede_ghazaei = ['nahar', 'sham']
        food_count = {food.name: 0 for food in self.foods_list}
        number_situation_on_week = len(week) * len(vaede_ghazaei)
        number_of_each_food_in_week = number_situation_on_week // lenth_of_food
        remaining_slots = number_situation_on_week % lenth_of_food

        for day in week:
            for vaede in vaede_ghazaei:
                while True:
                    selected_food = random.choice(self.foods_list)
                    if food_count[selected_food.name] < number_of_each_food_in_week or (remaining_slots > 0 and food_count[selected_food.name] == number_of_each_food_in_week):
                        self.list_situavation[day][vaede] = selected_food
                        food_count[selected_food.name] += 1
                        if food_count[selected_food.name] == number_of_each_food_in_week:
                            remaining_slots -= 1
                        break

        for day in week:
            for vaede in vaede_ghazaei:
                print(f'{day}, {vaede}: \n{self.list_situavation[day][vaede]}')

    def __del__(self):
        self.conn.close()

man1 = Management()
man1.add_food(Food('Bandari', ['Sosis', 'Piaz', 'Sibzamani']))
man1.add_food(Food('Ghorme Sabzi', ['Sabzi', 'Piaz', 'Ghosht']))
man1.add_food(Food('Fesenjan', ['Jooje', 'Ghoore', 'Piaz']))
man1.add_food(Food('Zereshk Polo', ['Morgh', 'Zereshk', 'Berenj']))
man1.add_food(Food('Adas Polo', ['Adas', 'Ghoore', 'Berenj']))


print("list kharid:")
man1.buy_list()

print("\n ghaza ha")
man1.show_foods()

print("\n barname ghazaie:")
man1.barname_ghazaei()