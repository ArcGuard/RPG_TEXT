import random as r

step = 0
Number_of_Players = int(input('Введите количество игроков: '))
choises = ['1', '2', '3', '4']
name = []
Table_stats = {}
Table_names = {}
Table_races = []
dict_Race_name = {}
Table_name_file = 'Table.txt'
Status_name_file = 'Status.txt'

Race_name = ['Высшие Эльфы', 'Лесные эльфы', 'Тёмные эльфы',
             'Орки', 'Гоблины', 'Гномы', 'Люди', 'Нежить', 'Демонстраторы']
Stats_name = ['Luck', 'Health', 'Strength', 'Agility', 'Intelligence', 'Wisdom']
Bar_name = ['HP', 'HP Regen', 'MP', 'MP Regen', 'Level', 'Current XP', 'LevelUp XP']

Table = [0] * Number_of_Players
Table_bar = [0] * Number_of_Players
for i in range(Number_of_Players):
    Table_bar[i] = [0] * len(Bar_name)
    Table[i] = [0] * len(Stats_name)


def TableRaces():
    Table_races.append([1, 2, 1, 2, 6, 3])  # Высшые эльфы
    Table_races.append([1, 2, 3, 4, 3, 2])  # Лесные эльфы
    Table_races.append([1, 3, 3, 4, 4, 1])  # Тёмные эльфы
    Table_races.append([0, 6, 6, 3, 0, 0])  # Орки
    Table_races.append([2, 3, 2, 4, 4, 0])  # Гоблины
    Table_races.append([1, 4, 4, 1, 4, 1])  # Гномы
    Table_races.append([2, 3, 3, 3, 2, 2])  # Люди
    Table_races.append([1, 2, 1, 1, 2, 2])  # Нежить
    Table_races.append([1, 4, 3, 3, 3, 1])  # Демонстраторы


def choise_race(number):
    print('Выберете расу:')
    for i in range(len(Race_name)):
        print(i + 1, ')', ' ', Race_name[i], sep='')
    name_race = int(input())
    for i in range(len(Stats_name)):
        Table[number] = Table_races[name_race - 1]


def print_Table():
    print('%-20s' % '', end=' ')
    for i in range(Number_of_Players):
        print('%-9s' % name[i], end=' ')
    print()

    for i in range(len(Stats_name)):
        print('%-20s' % Stats_name[i], end=' ')
        for j in range(Number_of_Players):
            print('%-9s' % Table[j][i], end=' ')
        print()


def print_Bar():
    print('%-20s' % '', end=' ')
    for i in range(Number_of_Players):
        print('%-9s' % name[i], end=' ')
    print()

    for i in range(len(Bar_name)):
        print('%-20s' % Bar_name[i], end=' ')
        for j in range(Number_of_Players):
            print('%-9s' % Table_bar[j][i], end=' ')
        print()


def menu():
    print('''
    1) Загрузить файл
    2) Вывести таблицу игроков
    3) Вывести статус-бар игроков
    4) Новый ход
    5) 
    ''')


def chance():
    L = int(input('Введите удачу '))
    chances = (L * 0.03) / (1 + L * 0.03)
    print('Шанс спас-броска равен ', '{:.2%}'.format(chances))






def choise_name():
    for i in range(len(name)):
        print(i, ') ', name[i], sep='')
    a = int(input('Выберете игрока:'))
    return name[a]


def lvlUP(j):
    name_lvlUP = name[j]
    Table_bar[j][2] += 1
    print('Игрок ', name_lvlUP, 'получил новый уровень! ')


def save_file(Table, Table_bar):
    f = open(Table_name_file, 'w')
    for i in range(Number_of_Players):
        a = ' '.join([str(i) for i in Table[i]])
        f.write(a + '\n')
    f.close()

    f = open(Status_name_file, 'w')
    for i in range(Number_of_Players):
        a = ' '.join([str(i) for i in Table_bar[i]])
        f.write(a + '\n')
    f.close()


def load_file():
    f = open(Table_name_file, 'r')
    a = f.readline()
    i = 0
    while a != '':
        Table[i] = a.split()
        i += 1
        a = f.readline()
    f.close()

    f = open(Status_name_file, 'r')
    a = f.readline()
    i = 0
    while a != '':
        Table_bar[i] = a.split()
        i += 1
        a = f.readline()
    f.close()
    return Table, Table_bar


TableRaces()


def choise_name_AOE():
    for i in range(len(name)):
        print(i, ') ', name[i], sep='')
    a = list(map(int, input('Выберете игроков:').split()))
    return a


def crit_damage(damage):
    cha = int(input('Введите шанс '))
    cha_damage = int(input('Введите увеличение урона '))
    rand = r.random()
    if cha / 100 < rand:
        print(damage)
        damage += damage * cha_damage  / 100
        print(damage)
    return damage

def another_damage(damage):
    cha_damage = int(input('Введите увеличение урона '))
    damage += damage * (cha_damage / 100)
    return damage

def resist_skill(damage):
    cha_damage = int(input('Введите сопротивление от скиллов '))
    damage -= damage * (cha_damage / 100)
    return damage



def resist_damage(damage):
    print('''
1) Крит
2) Другие источники
3) Сопротивление от способностей 
4) Отсутствует ''')

    a = input('Выберите модификаторы урона ')
    if a == '1':
        damage = crit_damage(damage)
        print(damage)
        resist_damage(damage)
    if a == '2':
        damage = another_damage(damage)
        resist_damage(damage)
    if a == '3':
        damage = resist_damage(damage)
        resist_damage(damage)
    if a == '4':
        return damage


def physics_resist(name_damage):
    agility = Table[name_damage][3]
    print(agility)
    d = int(agility / 5)
    PR = round((d * 0.05) / (1 + d * 0.05),3)
    print('Сопротивление физическому урону равно', '{:.2%}'.format(PR))
    return PR


def magic_resist(name_damage):
    wisdom = Table[name_damage][5]
    print(wisdom)
    Md = int(wisdom / 5)
    MR = (Md * 0.03) / (1 + Md * 0.03)
    print('Сопротивление магическому урону равно', '{:.2%}'.format(MR))
    return MR

def choise_damage(damage, name_damage):
    print('''
1) Физический
2) Магически ''')
    a = input('Выберите тип урона ')
    print()
    print(name_damage)
    print(damage)
    if a == '1':
        phy = physics_resist(name_damage)
        damage = damage * (1 - phy)
        print(damage)
        return damage
    elif a == '2':
        mag = magic_resist(name_damage)
        damage = damage * (1 - magic_resist(name_damage))
        return damage





def in_damage():
    name_damage = choise_name_AOE()
    damage = float(input('Введите количество урона '))
    damage = resist_damage(damage)


    if len(name_damage) == 1:
        damage = choise_damage(damage, name_damage[0])
        if Table_bar[name_damage[0]][0] - damage >= 0:
            Table_bar[name_damage[0]][0] -= damage
            print('Игрок', name[name_damage[0]], 'получает', damage, 'урона')
        else:
            Table_bar[name_damage[0]][0] = 0
            print('Игрок', name[name_damage[0]], 'Мёртв')


    else:
        for i in range(len(name_damage)):
            damage = choise_damage(damage, name_damage[i])
            if Table_bar[name_damage[i]][0] - damage >= 0:
                print('Игрок', name[name_damage[i]], 'получает', damage, 'урона')
                Table_bar[name_damage[i]][0] -= damage
            else:
                Table_bar[name_damage[i]][0] = 0
                print('Игрок', name[name_damage[i]], 'Мёртв')

def test_regen(j):
    if Table_bar[j][0] + Table_bar[j][1] >= Table[j][1] * 20:
        Table_bar[j][0] = Table[j][1] * 20
    else:
        Table_bar[j][0] += Table_bar[j][1]

    if Table_bar[j][2] + Table_bar[j][3] >= Table[j][1] * 15:
        Table_bar[j][2] = Table[j][1] * 15
    else:
        Table_bar[j][2] += Table_bar[j][3]

def new_move():
    print('''
1) Получение урона
2) Нанесение урона
3) Убийство врага
4) Окончание хода ''')
    ch = input('Выберите требуемое действие:')
    if ch == '1':
        in_damage()
        new_move()
    elif ch == '2':
        new_move()
    elif ch == '3':
        new_move()
    elif ch == '4':
        for j in range(Number_of_Players):
            test_regen(j)

        return step




for i in range(len(Stats_name)):
    Table_stats[Stats_name[i]] = i

for i in range(Number_of_Players):
    name.append(input('Введите имя игрока: '))
    Table_names[name[i]] = i
    choise_race(i)

for i in range(Number_of_Players):
    Table_bar[i][0] = 20 * Table[i][1]  # HP
    Table_bar[i][2] = 15 * Table[i][4]  # MP
    Table_bar[i][1] = round(Table_bar[i][0] / 15)
    Table_bar[i][3] = round(Table_bar[i][2] / 15)
    Table_bar[i][4] = 1  # LVL
    Table_bar[i][6] = 100  # Current XP


while True:
    menu()


    choise = input('Выберите требуемое действие:')
    if choise == '1':
        Table, Table_bar = load_file()


    elif choise == '2':
        print_Table()


    elif choise == '3':
        print_Bar()

    elif choise == '4':
        new_move()
        step += 1
        print('Идёт', step, 'ход')

    for j in range(Number_of_Players):
        if Table_bar[j][5] >= int(Table_bar[j][6] * (1.1 ** (Table_bar[j][4] - 1))):
            lvlUP(j)
    save_file(Table, Table_bar)
