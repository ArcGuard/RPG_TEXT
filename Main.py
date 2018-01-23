# step - Количество ходов
# lvlupXP - количество опыта на первый уровень
# Number_of_Players - Количество игроков
# name - Имена игроков
# Table_races - Таблица статов для разных рас
# Table_name_file - Имя для сохранения таблицы статов
# Status_name_file - Имя для сохранения таблицы статус-бара
# Race_name - Названия рас
# Stats_name -Названия статов
# Bar_name - Названия статус-баров
# Table - Таблица статов
# Table_bar - Таблица статус-бара


import random as r # Импортируем библиотеку рандома

step = 0
lvlupXP = 100
Number_of_Players = int(input('Введите количество игроков: '))
name = []
Table_races = []
Table_name_file = 'Table1.txt'
Status_name_file = 'Status1.txt'

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

# Выбор расы для каждого игрока в начале игры
def choise_race(number : int):
    print('Выберете расу:')
    for i in range(len(Race_name)):
        print(i + 1, ')', ' ', Race_name[i], sep='')
    name_race = int(input())
    for i in range(len(Stats_name)):
        Table[number] = Table_races[name_race - 1]

# Вывод таблицы статов
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

# Вывод таблицы статус-бара
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

# Большой некрасивый вывод, который сделал отдельной функцией
def menu():
    print('''
    1) Загрузить файл
    2) Вывести таблицу игроков
    3) Вывести статус-бар игроков
    4) Новый ход
    5) Изменить характеристики игрока
    ''')

# Шанс спас-броска (пока ещё не пригодился)
def chance():
    L = int(input('Введите удачу '))
    chances = (L * 0.03) / (1 + L * 0.03)
    print('Шанс спас-броска равен ', '{:.2%}'.format(chances))

# Выбор одного имени для действия
def choise_name():
    for i in range(len(name)):
        print(i, ') ', name[i], sep='')
    a = int(input('Выберете игрока:'))
    return a

# Выбор несколькоих имён для действия
def choise_name_AOE():
    for i in range(len(name)):
        print(i, ') ', name[i], sep='')
    a = list(map(int, input('Выберете игроков:').split()))
    return a

# Поднятие уровня (ещё не доработана)
# Будет сделано добавление статов игроку
# И возможно что-то ещё
def lvlUP(j : int):
    name_lvlUP = name[j]
    Table_bar[j][2] += 1
    print('Игрок ', name_lvlUP, 'получил новый уровень! ')

# Сохраняем две таблицы в два отдельных файла
def save_file(Table, Table_bar):
    f = open(Table_name_file, 'w')
    for i in range(Number_of_Players):
        a = ' '.join([str(i) for i in Table[i]])
        f.write(a + '\n')
    f.close()

    f = open(Status_name_file, 'w')
    for i in range(Number_of_Players):
        # Преобразовываем числа в строки
        # Люблю генераторы в Питоне
        # Всё можно делать в одну строку с:
        a = ' '.join([str(i) for i in Table_bar[i]])
        f.write(a + '\n')
    f.close()

# Загружаем таблицы
def load_file():
    f = open(Table_name_file, 'r')
    a = f.readline()
    i = 0
    while a != '':
        print(a.split()[i])
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
    for i in range(len(name)):
        for j in range(Number_of_Players):
            Table[j][i] = float(Table[j][i])

    # Это страшная кракозябра, которая преобразует все в числа
    # Чтобы записать в файл, надо было все числа в строки преобразовать
    # Тут как бы наоборот
    for i in range(len(Bar_name)):
        for j in range(Number_of_Players):
            Table_bar[j][i] = float(Table_bar[j][i])

    return Table, Table_bar


# Подсчёт удара с крита
def crit_damage(damage : float):
    cha = int(input('Введите шанс '))
    cha_damage = int(input('Введите увеличение урона '))
    rand = r.random()

    # Тут возможно написан бред, но так работает
    # А без бреда не оч
    # Я про присваивания в else.
    if cha / 100 > 1 - rand:
        damage = damage * (1 + cha_damage / 100)
        return damage
    else:
        damage = damage
        return damage

# Подсчёт других увеличений урона
def another_damage(damage: float):
    cha_damage = int(input('Введите увеличение урона '))
    damage = damage * (1 + cha_damage / 100)
    return damage

# Подсчёт сопротивления урона
def resist_skill(damage: float):
    cha_damage = int(input('Введите сопротивление от скиллов '))
    damage = damage * (cha_damage / 100)
    return damage

# Выбираем модификаторы урона
# И с учётом вышеподсчитанного прибавляем\убавляем урон
# Возвращает или саму себя (несколько критов и прочее)
# Или урон, если отсутвует больше
def resist_damage(damage: float):
    print('''
1) Крит
2) Другие источники
3) Сопротивление от способностей 
4) Отсутствует ''')
    a = input('Выберите модификаторы урона ')
    new_damage = damage
    print(new_damage)
    if a == '1':
        crit = crit_damage(new_damage)
        new_damage = round(crit,2)
        print(new_damage)
        return resist_damage(new_damage)
    elif a == '2':
        another = another_damage(new_damage)
        new_damage = round(another,2)
        return resist_damage(new_damage)
    elif a == '3':
        resist = resist_skill(new_damage)
        new_damage -= round(resist,2)
        print(new_damage)
        return resist_damage(new_damage)
    elif a == '4':
        damage = new_damage
        print(damage)
        return damage
    else:
        return resist_damage(new_damage)



# Подсчёт физического сопротивления в зависимости от характеристик
def physics_resist(name_damage: int):
    agility = Table[name_damage][3]
    print(agility)
    d = int(agility / 5)
    PR = round((d * 0.05) / (1 + d * 0.05), 3)
    print('Сопротивление физическому урону равно', '{:.2%}'.format(PR))
    return PR

# Подсчёт магического сопротивления в зависимости от характеристик
def magic_resist(name_damage: int):
    wisdom = Table[name_damage][5]
    print(wisdom)
    Md = int(wisdom / 5)
    MR = (Md * 0.03) / (1 + Md * 0.03)
    print('Сопротивление магическому урону равно', '{:.2%}'.format(MR))
    return MR

# Выбор наносимого урона
def choise_damage(damage: float, name_damage: int):
    print('''
1) Физический
2) Магически ''')
    a = input('Выберите тип урона ')
    print(damage)
    if a == '1':
        phy = physics_resist(name_damage)
        damage = damage * (1 - phy)
        return damage
    elif a == '2':
        mag = magic_resist(name_damage)
        damage = damage * (1 - mag)
        return damage

# Выбираем кто получил урон
# Считаем его, учитывая всё что угодно
# Отнимаем жизни в таблице
def in_damage(damage: float):
    name_damage = choise_name_AOE()
    kek = resist_damage(damage)
    damage = kek
    print(damage)
    # Если одному человеку наносим, то не функция range()
    # Не вызовется. Поэтому учитываем отдельно случай для одного человека
    if len(name_damage) == 1:
        choises = choise_damage(damage, name_damage[0])
        damage = choises
        if Table_bar[name_damage[0]][0] - damage >= 0:
            Table_bar[name_damage[0]][0] -= damage
            print('Игрок', name[name_damage[0]], 'получает', damage, 'урона')
        else:
            Table_bar[name_damage[0]][0] = 0
            print('Игрок', name[name_damage[0]], 'Мёртв')

    # Соответственно тут циклом многим людям отнимаем
    else:
        for i in range(len(name_damage)):
            choises = choise_damage(damage, name_damage[i])
            damage = choises
            if Table_bar[name_damage[i]][0] - damage >= 0:
                print('Игрок', name[name_damage[i]], 'получает', damage, 'урона')
                Table_bar[name_damage[i]][0] -= damage
            else:
                Table_bar[name_damage[i]][0] = 0
                print('Игрок', name[name_damage[i]], 'Мёртв')

# Странное название функции
# Но вроде всё работает
# Так что зачем что-то менять?) :kappa:
# Реген маны и жизней
def test_regen(j: int):
    if Table_bar[j][0] + Table_bar[j][1] >= Table[j][1] * 20:
        Table_bar[j][0] = Table[j][1] * 20
    else:
        Table_bar[j][0] += Table_bar[j][1]

    if Table_bar[j][2] + Table_bar[j][3] >= Table[j][1] * 15:
        Table_bar[j][2] = Table[j][1] * 15
    else:
        Table_bar[j][2] += Table_bar[j][3]

# Ужасно некрасивая, но до ужаса простая функция
# Которая изменяет статы с клавиатуры
def change_stats(j):
    print('''
1) Luck
2) Health
3) Strength
4) Agility
5) Intelligence
6) Wisdom
7) HP
8) HP Regen
9) MP
10) MP Regen''')
    choise = input('Выберете что изменить: ')
    value = float(input('Выберете на сколько изменить '))
    if choise == '1':
        Table[j][0] += value
    elif choise == '2':
        Table[j][1] += value
    elif choise == '3':
        Table[j][2] += value
    elif choise == '4':
        Table[j][3] += value
    elif choise == '5':
        Table[j][4] += value
    elif choise == '6':
        Table[j][5] += value
    elif choise == '7':
        Table_bar[j][0] += value
    elif choise == '8':
        Table_bar[j][1] += value
    elif choise == '9':
        Table_bar[j][2] += value
    elif choise == '10':
        Table_bar[j][3] += value

def regen():
    for j in range(Number_of_Players):
        pass


# Опять же много принтов
# И сразу же выбор действия
# И вызов различных функций, исходя из выбора
# Пока ещё много чего зациклено, ибо не написаны функции
def new_move():
    print('''
1) Получение урона
2) Нанесение урона
3) Убийство врага
4) Окончание хода
5) Вывести таблицу игроков
6) Вывести статус бар игроков ''')
    ch = input('Выберите требуемое действие:')
    if ch == '1':
        damage = float(input('Введите количество урона '))
        in_damage(damage)
        new_move()
    elif ch == '2':
        new_move()
    elif ch == '3':
        new_move()
    elif ch == '4':
        for j in range(Number_of_Players):
            test_regen(j)
            return step
    elif ch == '5':
        print_Table()
        new_move()
    elif ch == '6':
        print_Bar()
        new_move()
    else:
        new_move()


# Создаем таблицу рас
TableRaces()

# Вводим имена игроков и выбираем им расу
for i in range(Number_of_Players):
    name.append(input('Введите имя игрока: '))
    choise_race(i)

# Создаем начальные запасы HP, MP и прочего
for i in range(Number_of_Players):
    Table_bar[i][0] = 20 * Table[i][1]  # HP
    Table_bar[i][2] = 15 * Table[i][4]  # MP
    Table_bar[i][1] = round(Table[i][1] / 15) # HP regen
    Table_bar[i][3] = round(Table[i][5] / 15) # MP regen
    Table_bar[i][4] = 1  # LVL
    Table_bar[i][6] = 100  # Current XP

# Зацикленная сама игра
while True:
    menu()

    choise = input('Выберите требуемое действие:')
    # Загрузить файл
    if choise == '1':
        Table, Table_bar = load_file()

    # Вывести таблицу игроков
    elif choise == '2':
        print_Table()

    # Вывести статус-бар игроков
    elif choise == '3':
        print_Bar()

    # Новый ход
    elif choise == '4':
        new_move()
        step += 1
        print('Идёт', step, 'ход')

    # Измена характеристик
    elif choise == '5':
        change_name = choise_name()
        change_stats(change_name)

        new_move()

    # Проверка на опыт
    for j in range(Number_of_Players):
        Table_bar[j][6] = round(lvlupXP * (1.1 ** Table_bar[j][4] - 1))
        if Table_bar[j][5] >= Table_bar[j][6]:
            lvlUP(j)
    save_file(Table, Table_bar)
