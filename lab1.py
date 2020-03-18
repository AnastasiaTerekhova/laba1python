import random
import itertools
import datetime

# 1
"""
Напишите скрипт, который преобразует введенное с клавиатуры
вещественное число в денежный формат. Например, число 12,5 должно
быть преобразовано к виду «12 руб. 50 коп.». В случае ввода
отрицательного числа выдайте сообщение «Некорректный формат!»
путем обработки исключения в коде
"""


def task_1():
    try:  # блок который проверяется на ошибки
        money = float(input(
            "Введите число,которое будет преобразовано в денежный формат:"))
        assert money >= 0  # проверка на истинность,что денег больше 0, иначе кинет исключение
        rub = int(money)  # получаем рубли, преобразованием к целому числу
        # от общей суммы отнимаем рубли и умножаем на 100, получаем копейки и округляем
        kop = round((money - rub)*100)
        # выводим,преобразовывая числа в строку
        print(str(rub) + " руб. " + str(kop) + " коп.")
    except AssertionError:  # исключение
        print("Некорректный формат!")


# 2
"""
Написать скрипт, который выводит на экран «True», если элементы
программно задаваемого списка представляют собой возрастающую
последовательность, иначе – «False»
"""


def task_2():
    # генератор списка от 1 до 25 с шагом 2
    lst = [i for i in range(1, 25, 2)]
    lst_c = lst.copy()  # копия списка
    lst_c.sort()  # сортируем копию по умолчанию сортирует по возрастанию
    # выводит true если списки совпали после сортировки,значит он уже был в порядке возрастания,иначе false
    print(lst == lst_c)


# 3
"""
Напишите скрипт, который позволяет ввести с клавиатуры номер
дебетовой карты (16 цифр) и выводит номер в скрытом виде: первые и
последние 4 цифры отображены нормально, а между ними – символы
«*» (например, 5123 **** **** 1212).
"""


def task_3():
    while True:  # срабатывает пока не введем номер карты в правильном формате
        number_card = input("Введите номер карты из 16 цифр:")
        if(number_card.isdigit() and len(number_card) == 16):  # проверяем на правильность ввода
            break
    for i in range(0, 16):
        if(i <= 3 or i >= 12):  # центральные сиволы переписываются
            print(number_card[i], end="")
        else:  # боковые заменяются звездочкой
            print("*", end="")


# 4
"""Напишите скрипт, который разделяет введенный с клавиатуры текст на
слова и выводит сначала те слова, длина которых превосходит 7
символов, затем слова размером от 4 до 7 символов, затем – все
остальные.
"""


def task_4():
    words = (
        input("\nВведите текст, который будет разбит на слова: ")
        .replace(".", " ")  # Замена символов на пробел
        .replace(",", " ")
        .split()  # разбиваем строку на слова по пробелам
    )
    # генерируем список со словами длина которых больше 7
    w_7 = [w for w in words if len(w) > 7]
    w_4_7 = [w for w in words if 4 <= len(w) <= 7]
    w_other = [w for w in words if len(w) < 4]
    print("Все слова длинной > 7: ", *w_7)
    print("Все слова длинной <= 7 и >= 4:", *w_4_7)
    print("Все остальные слова: ", *w_other)


# 5
"""
Напишите скрипт, который позволяет ввести с клавиатуры текст
предложения и сформировать новую строку на основе исходной, в
которой все слова, начинающиеся с большой буквы, приведены к
верхнему регистру. Слова могут разделяться запятыми или пробелами.
Например, если пользователь введет строку «город Донецк, река
Кальмиус», результирующая строка должна выглядеть так: «город
ДОНЕЦК, река КАЛЬМИУС»
"""


def task_5():
    string_new = ""
    string = input(
        "Введите строку, в которой слова с большой буквы будут преобразованы в верхний регистр: "
    ).split(" ")  # вводенную строку разбиваем на слова по пробелам
    for word in string:  # цикл по словам
        if word.istitle():  # если слово начинается с большой буквы
            string_new += word.upper() + " "  # делаем из него верхний регистр
        else:
            string_new += word + " "  # ничего не меняем и переписываем
    print(string_new)


# 6
"""
Напишите программу, позволяющую ввести с клавиатуры текст
предложения и вывести на консоль все символы, которые входят в этот
текст ровно по одному разу.
"""


def task_6():
    text = input("Введите текст, в котором найдутся все уникальные символы: ")
    set_t = set(text)  # множество всех уникальных сиволов
    # генератором объеденяем их в одну строку через пробел
    print("".join([x + " " for x in set_t if text.count(x) == 1]))


# 7
"""
Напишите скрипт, который обрабатывает список строк-адресов
следующим образом: сначала определяет, начинается ли каждая строка
в списке с префикса «www». Если условие выполняется, то скрипт
должен вставить в начало этой строки префикс «http: //», а затем
проверить, что строка заканчивается на «.com». Если у строки другое
окончание, то скрипт должен вставить в конец подстроку «.com». В
итоге скрипт должен вывести на консоль новый список с измененными
адресами. Используйте генераторы списков.
"""


def task_7():
    addr = ["http://www.new.ru", "www.home.com",
            "www.mail.bk", "http://www.donetsk.com"]
    new_addr = [
        (
            # если последние 3 символа не равны com то дописываем http в начало и заменяем символы после последней точки на com
            "http://" + ".".join(i.split(".")[:-1]) + ".com"
            if i[-3:] != "com"
            else "http://" + i  # иначе просто дописываем http в начало
        )
        # если строка начинается с www или http:// то выполняется предыдущий блок
        if i[0:3] == "www" or i[0:7] != "http://"
        # иначе заменяем символы после последней точки на com
        else ".".join(i.split(".")[:-1]) + ".com"
        for i in addr
    ]
    print(new_addr)


# 8
"""
Напишите скрипт, генерирующий случайным образом число n в
диапазоне от 1 до 10000. Скрипт должен создать массив из n целых
чисел, также сгенерированных случайным образом, и дополнить
массив нулями до размера, равного ближайшей сверху степени двойки.
Например, если в массиве было n = 100 элементов, то массив нужно
дополнить 28 нулями, чтобы в итоге был массив из 28
=128 элементов
(ближайшая степень двойки к 100 – это число 128, к 35 – это 64 и т.д.).
"""


def task_8():
    n = random.randint(1, 10000)
    # генерируем список длинной n из случайных чисел от 1 до 10
    mass_rand = [random.randint(1, 10) for i in range(n)]
    print("Сгенерированный размер массива: ", len(mass_rand))
    step = 0
    while n > 1:  # находим степень числа
        n /= 2
        step += 1
    # добовляем столько нулей,сколько нужно
    [mass_rand.append(0) for i in range(pow(2, step) - len(mass_rand))]
    print("Новый размер массива,равный степени 2: ", len(mass_rand))


# 9
"""
Напишите программу, имитирующую работу банкомата. Выберите
структуру данных для хранения купюр разного достоинства в заданном
количестве. При вводе пользователем запрашиваемой суммы денег,
скрипт должен вывести на консоль количество купюр подходящего
достоинства. Если имеющихся денег не хватает, то необходимо
напечатать сообщение «Операция не может быть выполнена!».
Например, при сумме 5370 рублей на консоль должно быть выведено
«5*1000 + 3*100 + 1*50 + 2*10».
"""


def task_9():
    # словарь с количеством купюр и их значениями
    cash = {"1000": 5, "100": 10, "50": 4, "10": 3, "5": 3, "1": 50}
    result = ""  # строка для записи в нее результата
    take_money = int(input("Введите сумму, которую хотите снять: "))
    s = 0
    # находим количество денег в банкомате
    for u in cash.items():
        s += int(u[0]) * u[1]
    # проходимся по всем купюрам в банкомате
    for i in cash.keys():
        nom = int(i)  # текущий номинал купюры
        # сколько купюр текущего номенала нам нужно
        need_kup = int(take_money / nom)
        if s >= take_money:  # если хватает денег
            # если нам нужно больше купюр текущего номинала,чем у нас есть
            if cash.get(i) < need_kup:
                # то выдаем столько купюр,сколько у нас есть
                need_kup = cash.get(i)
            if take_money != 0 and need_kup == 0:  # если нам еще нужны деньги,но у нас нет купюр
                result = "Недостаточно купюр"
                break
            take_money -= need_kup * nom  # отнимаем от суммы которую нужно выдать,то что выдаем
            # списываем со счета банкомата
            cash.update({i: int(cash.get(i) - need_kup)})
            # записываем результаты в строку вывода
            if take_money == 0:  # если уже нечего снимать, то заканчиваем вывод
                result += str(need_kup) + " * " + str(nom)
                break
            else:  # иначе продолжаем
                result += str(need_kup) + " * " + str(nom) + " + "
        else:  # если количество денег в банкомате меньше,чем мы хотим снять
            result = "Недостаточно денег!"
            break
    print(result)


# 10
"""
Напишите скрипт, позволяющий определить надежность вводимого
пользователем пароля. Это задание является творческим: алгоритм
определения надежности разработайте самостоятельно.
"""


def task_10():
    pas = input("Введите пароль: ")
    koeff = 0  # переменная,которая будет влиять на определение сложности пароля
    now_sym = {  # список с параметрами символа
        "up": pas[0].isupper(),  # верхний регистр
        "low": pas[0].islower(),  # нижний регистр
        "dig": pas[0].isdigit(),  # цифра
        "sym": pas[0],  # сам символ
    }
    for i in range(len(pas)):  # цикл по каждому элементу пароля
        last_sym = now_sym.copy()  # сохраняем текущий символ
        if pas[i].isdigit():  # если цифра
            now_sym["dig"] = True
            now_sym["up"] = False
            now_sym["low"] = False
        else:
            now_sym["dig"] = False
            if pas[i].isupper():  # если верхний регстр
                now_sym["up"] = True
                now_sym["low"] = False
            else:
                now_sym["up"] = False
                now_sym["low"] = True
        now_sym["sym"] = pas[i]
        # если текущий символ число, а предыдущий буква или наоборот
        if now_sym["dig"] != last_sym["dig"]:
            koeff += 80
        # если регистры текущего символа и предыдущего разные
        elif (now_sym["up"] and last_sym["low"]) or (now_sym["low"] and last_sym["up"]):
            koeff += 80
        else:
            koeff += 40
    # формула, по которой расчитывается сложность пароля
    level = (len(pas) * (koeff / 10)) / 15
    if level < 30:
        print("Слабый пароль")
    elif 30 <= level < 50:
        print("Средний пароль")
    elif 50 <= level < 90:
        print("Хороший пароль")
    else:
        print("Сильный пароль")


# 11
"""
Напишите генератор frange как аналог range() с дробным шагом.
Пример вызова:
for x in frange(1, 5, 0.1):
print(x)
# выводит 1 1.1 1.2 1.3 1.4 … 4.9
"""

def task_11():
    def frange(start, end, step):
        while start < end: # пока итерируемое число меньше чем конечное
        # округляем текущее число до 1 знака после запятой
            val = round(start, 1)
            start += step # увеличиваем итерируемое число на наш шаг
            yield val # возвращаем округленное число на текущей итерации. yield запоминает на чем остановились

    for x in frange(1, 5, 0.1): # создаем цикл по нашей функции передавая необходимые параметры
        print(x) # выводим возвращаемые нашей функцией значения
# 12
"""
Напишите генератор get_frames(), который производит «оконную
декомпозицию» сигнала: на основе входного списка генерирует набор
списков – перекрывающихся отдельных фрагментов сигнала размера
size со степенью перекрытия overlap. Пример вызова:
for frame in get_frames(signal, size=1024, overlap=0.5):
print(frame)
"""
def task_12():
    def get_frames(signal, size, overlap):  # функция с параметрами
        # находим размер учитывая перекрытие и округляем
        size = round(size*overlap)
        start = 0  # индекс первого сигнала в фрейме
        end = int(size)  # индекс конечного сигнала в фрейме
        while start <= len(signal):  # пока не закончатся сигналы
            # берем диапазон сигналов с индексами от start до end
            frame = signal[start:end]
            yield frame  # возваращаем этот диапазон с запоминанием того, где остановились
            # увеличиваем текущие индексы на размерность
            start += int(size)
            end += int(size)

    signal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # список сигналов
    # вызов нашего метода с заданием определенных параметров
    for frame in get_frames(signal, size=9, overlap=0.3):
        print(frame)


# 13
"""
Напишите собственную версию генератора enumerate под названием
extra_enumerate. Пример вызова:
for i, elem, cum, frac in extra_enumerate(x):
 print(elem, cum, frac)
 В переменной cum хранится накопленная сумма на момент текущей
итерации, в переменной frac – доля накопленной суммы от общей
суммы на момент текущей итерации. Например, для списка x=[1,3,4,2]
вывод будет таким:
 (1, 1, 0.1) (3, 4, 0.4) (4, 8, 0.8) (2, 10, 1)
"""


def task_13():
    def extra_enumerate(x):  # функция с параметром
        frac, cum = 0, 0
        for i in x:
            cum += i
            frac = cum / sum(x)
            # создаем список со значениями, который будем возвращать
            ret = [0, i, cum, frac]
            yield ret  # yield почти то же, что и return.Возвращает список

    x = [1, 3, 4, 2]
    for i, elem, cum, frac in extra_enumerate(x):
        print(elem, cum, frac)


# 14
"""
Напишите декоратор non_empty, который дополнительно проверяет
списковый результат любой функции: если в нем содержатся пустые
строки или значение None, то они удаляются. Пример кода:
@non_empty
def get_pages():
return ['chapter1', '', 'contents', '', 'line1']
"""


def task_14():
    def non_empty(fn):
        def wrapper():
            ls = fn()
            new_ls = []  # новый список,в который будем сохранять нужные элементы
            for i in ls:
                if i is not None and i != "":  # если элемент списка не пустой и не none
                    new_ls.append(i)  # заносим в новый список
            return new_ls

        return wrapper

    @non_empty
    def get_pages():
        return ["sofa", "", "", None, None, "sidney", "home", ""]

    print(get_pages())


# 15
"""
Напишите параметризированный декоратор pre_process, который
осуществляет предварительную обработку (цифровую фильтрацию)
списка по алгоритму: s[i] = s[i]–a∙s[i–1]. Параметр а можно задать в
коде (по умолчанию равен 0.97). Пример кода:
@pre_process(a=0.93)
def plot_signal(s):
 for sample in s:
print(sample)
"""


def task_15():
    def pre_process(a=0.97):  # создаем функцию декоратор с параметром
        def decorated(func):  # что-то на подобии прослойки между методами
            def wrapper(arg):  # arg это и есть наш список s, в plot_signal
                # цикл по всех элементам списка,который мы передали в функцию plot_signal
                for i, val in enumerate(arg):
                    # переопределяем элементы списка по заданной формуле
                    arg[i] = round(arg[i] - a * arg[i - 1], 2)
                ret = func(arg)
                return ret

            return wrapper

        return decorated

    @pre_process(a=0.93)
    def plot_signal(s):
        for sample in s:
            print(sample)

    plot_signal([2, 5, 10, 20])


# 16
"""
Напишите скрипт, который на основе списка из 16 названий
футбольных команд случайным образом формирует 4 группы по 4
команды, а также выводит на консоль календарь всех игр(игры
должны проходить по средам, раз в 2 недели, начиная с 14 сентября
текущего года). Даты игр необходимо выводить в формате «14/09/2016,
22: 45». Используйте модули random и itertools.
"""


def task_16():
    commands = [  # список с 16 командами
        "Манчестер Юнайтед",
        "Спартак",
        "РБ Лейпциг",
        "Динамо",
        "Челси",
        "Реал Мадрид",
        "Аталанта",
        "Арсенал",
        "Бенфика",
        "Реал Бетис",
        "Сантос Лагуна",
        "Атлетико Минейро",
        "Кашима Антлерс",
        "Интернасьонал",
        "Валенсия",
        "Аякс",
    ]
    groups = []
    for i in range(4):
        groups.append([])  # добавляем пустой список в список groups
        for j in range(4):
            k = random.randint(
                0, len(commands) - 1
            )  # рандомим индекс команды, которую будем заосить в новый список
            # добавляем случайную команду в список группы
            groups[i].append(commands.pop(k))
    date = datetime.datetime(  # Задаем начальное время, от которого будем считать
        datetime.datetime.today().year, 9, 14, random.randint(0, 23), random.randint(0, 59)
    )
    while date.weekday() != 2:  # пока день недели не будет средой
        date += datetime.timedelta(days=1)  # увеличиваем счетчик дней на 1
    date_s = date  # делаем копию даты
    for group in groups:  # цикл по каждой группе команд
        print("Группа : " + str(group))
        # создание списка колекций перестановок всех команд в группе по 2 элемента
        games = itertools.permutations(group, 2)
        for game in games:  # цикл по всем играм
            date = datetime.datetime(  # обновляем дату после каждого матча
                date.year,
                date.month,
                date.day,
                random.randint(0, 23),  # рандом часов
                random.randint(0, 59),  # рандом минут
            )
            print(
                str(game[0])
                + " против "
                + str(game[1])
                + " : "
                # приводим к необходимому виду вывод даты
                + date.strftime("%d/%m/%Y, %H:%M")
            )
            # увеличиваем текущую дату на 14 дней
            date += datetime.timedelta(days=14)
        date = date_s  # возвращаем базовую дату


if __name__ == '__main__':
    # task_1()
    # task_2()
    # task_3()
    # task_4()
    # task_5()
    # task_6()
    # task_7()
    # task_8()
    # task_9()
    # task_10()
    # task_11()
    # task_12()
    # task_13()
    # task_14()
    # task_15()
    # task_16()
