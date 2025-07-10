# import pygame
# import random
#
#
# def generate_ball():
#    global ball_x
#    global ball_y
#    ball_x = random.randint(0,WIDTH)
#    ball_y = random.randint(0,HEIGHT)
#    red = random.randint(100,255)
#    green = random.randint(100,255)
#    blue = random.randint(100,255)
#    pygame.draw.circle(
#        main_screen,
#        (red,green,blue),
#        (ball_x, ball_y),
#        20
#    )
#    pygame.display.update()
#
# WIDTH = 800
# HEIGHT = 800
#
# pygame.init()
# main_screen=pygame.display.set_mode((WIDTH,HEIGHT))
#
# ball_x = ball_y = 0
# score=0
#
# clock = pygame.time.Clock()
# my_font = pygame.font.SysFont("roboto",16)
#
# while True:
#     main_screen.fill((0,0,0))
#     clock.tick(1)
#     for event in pygame.event.get():
#         # print(event)
#         if event.type == pygame.QUIT:
#             pygame.quit()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_x=event.pos[0]
#             mouse_y=event.pos[1]
#             print(mouse_x, mouse_y,score)
#             if ball_x - 20 <=mouse_x <= ball_x + 20 and ball_y - 20 <=mouse_y <= ball_y + 20:
#                 score+=1
#                 generate_ball()
#     score_text=my_font.render(f"Score: {score}", True, (255,0,0))
#     main_screen.blit(score_text,(20,20))
#
#
#
#
#
#     generate_ball()
#     pygame.display.update()
from ctypes import c_char_p, c_short
from distutils.command.clean import clean

# import json
#
#
# def add_book():
#     global new_book_id          # будем изменять глобальную переменную
#     global all_books_data
#     print("\n\n")
#     print("-" * 100)
#     title = input("Название книги: ")
#     author = input("Автор книги: ")
#     year = int(input("Год издания книги: "))
#     all_books_data[str(new_book_id)] = {
#         "title": title,
#         "author": author,
#         "year": year
#     }
#     new_book_id += 1        # следующая книга будет иметь id на 1 больше
#     print(f"Книга '{title}' успешно добавлена в библиотеку.")
#     print("-" * 100)
#     save_data()
#     """
#      0: {
#         "title": "Война и мир",
#         "author": "Толстой Л.Н.",
#         "year": 1962
#     },
#     1: {
#         "title": "Анна Каренина",
#         "author": "Толстой Л.Н.",
#         "year": 1965
#     }
#     """
#
#
# def delete_book():
#     print("\n\n")
#     print("-" * 100)
#     show_data()
#     book_id=input("Введите id книги, которую надо удалить: ")
#     all_books_data.pop(book_id)
#     print("Книга успешно удалена.")
#
# def search_book():
#     print("\n\n")
#     print("-" * 100)
#     search_year=int(input("Пойск по году издания. Введите год: "))
#     for id, book_data in all_books_data.items():
#         title=book_data["title"]
#         author=book_data["author"]
#         year=book_data["year"]
#         if year == search_year:
#             print(f"{id}) {title}'; {author}; {year} r.")
#
# def change_book_data():
#     print("\n\n")
#     print("-" * 100)
#     show_data()
#     book_id=input("Введите id книги, которую надо изменить: ")
#     name=input("Новое название: ")
#     author=input("Новый автор: ")
#     year=input("Новый год: ")
#     all_books_data[book_id] = {
#         "title": name,
#         "author": author,
#         "year": year
#     }
#
# def save_data():
#     with open("book_database.json","w",encoding="utf-8") as file:
#         json.dump(all_books_data, file, ensure_ascii=False,indent=4)
#     with open("book_id_info.txt", "w", encoding="utf-8") as id_file:
#         id_file.write(str(new_book_id))
#
# def show_data():
#     print("\n\n")
#     print("-" * 100)
#     for id, book_data in all_books_data.items():
#         title=book_data["title"]
#         author=book_data["author"]
#         year=book_data["year"]
#         print(f"{id}) {title}'; {author}; {year} r.")
#         print("-" * 100)
#         print("\n\n")
#
# try:
#     with open("book_database.json","r",encoding="utf-8") as file:
#         all_books_data = json.load(file)     # тут будем держать словарь о все книгах.
#     with open("book_id_info.txt", "r", encoding="utf-8") as id_file:
#         new_book_id=int(id_file.read())      #
# except:
#     all_books_data = {}     # тут будем держать словарь о все книгах.
#     new_book_id = 0           # id новой будущей книги при добавлении
#
#
# while True:
#     print("1. Показать все книги.")
#     print("2. Добавить книгу.")
#     print("3. Удалить книгу.")
#     print("4. Найти книгу.")
#     print("5. Изменить данные у книги.")
#     print("0. Выход.")
#     user_choice = input("Ваш выбор(номер): ")
#     match user_choice:
#         case "1": show_data()
#         case "2": add_book()
#         case "3": delete_book()
#         case "4": search_book()
#         case "5": change_book_data()
#         case "0": break
#         case _: print("Неизвестная команда. Требуется только номер.")


# rus_to_eng = {
#     "а": "a",
#     "б": "b",
#     "в": "v",
#     "г": "g",
#     "д": "d",
#     "е": "e",
#     "ё": "yo",
#     "ж": "zh",
#     "з": "z",
#     "и": "i",
#     "й": "j",
#     "к": "k",
#     "л": "l",
#     "м": "m",
#     "н": "n",
#     "о": "o",
#     "п": "p",
#     "р": "r",
#     "с": "s",
#     "т": "t",
#     "у": "u",
#     "ф": "f",
#     "х": "h",
#     "ц": "c",
#     "ч": "ch",
#     "ш": "sh",
#     "щ": "shh",
#     "ъ": "'",
#     "ы": "y",
#     "ь": "'",
#     "э": "e",
#     "ю": "yu",
#     "я": "ya"
# }
#
# some_text="Вася пришёл, маше - место свое жене с детьми."
# translit_text=""
#
#
# for char in some_text:
#     new_char=rus_to_eng.get(char.lower(), char)
#     if char.islower():
#         translit_text+=new_char
#     else:
#         translit_text+=new_char
# print(translit_text)


# def bubbble_sort(arr: list) -> list:
#     n = len(arr)
#     for step in range(1,n):
#         for bubble in range(0,n-step):
#             if arr[bubble] > arr [bubble +1]:
#                 arr[bubble], arr[bubble + 1] = arr [bubble +1], arr[bubble]
#     return arr
#
#
# def bubbble_smart_sort(arr: list) -> list:
#     n = len(arr)
#     for step in range(1,n):
#         is_sorted = True
#         for bubble in range(0,n-step):
#             if arr[bubble] > arr [bubble +1]:
#                 arr[bubble], arr[bubble + 1] = arr [bubble +1], arr[bubble]
#                 is_sorted=False
#         if is_sorted:
#             break
#     return arr
#
#
# def selection_sort(arr: list) -> list:
#     n = len(arr)
#     for lowest_item in range(0,n-1):
#         for position in range(lowest_item+1,n):
#             if arr[lowest_item] > arr[position]:
#                 arr[lowest_item], arr[position] = arr[position], arr[lowest_item]
#     return arr
#
#
# def insert_sort(arr: list) -> list:
#     n = len(arr)
#     for step in range(1,n):
#         new_item_idex=step
#         while new_item_idex > 0 and arr[new_item_idex] < arr[new_item_idex-1]:
#             arr[new_item_idex], arr[new_item_idex-1] = arr[new_item_idex-1], arr[new_item_idex]
#             new_item_idex -=1
#     return arr
#
#
# def quick_soft(arr: list) -> list:
#     less=[]
#     equals=[]
#     bigger=[]
#     pivot=arr[0]
#     for elem in arr:
#         if elem < pivot:
#             less.append(elem)
#         elif elem > pivot:
#             bigger.append(elem)
#         else:
#             equals.append(elem)
#     return arr
#
#
# def count_sort(arr: list) -> list:
#     mimimal=min(arr)
#     maximal=max(arr)
#     result_list=[]
#     count_table= dict.fromkeys([i for i in range(mimimal,maximal+1)], 0)
#
#     for number in arr:
#         count_table[number]+=1
#
#     for n, count in count_table.items():
#         result_list.extend([n]*count)
#
#     return arr
#
#
#
#
#
#
# arr = [3,1,5,4,6,9,8,7,2]
#
# print(*arr)
# print(*bubbble_sort(arr))
# arr = [3,1,5,4,6,9,8,7,2]
# print(*bubbble_smart_sort(arr))
# arr = [3,1,5,4,6,9,8,7,2]
# print(*selection_sort(arr))
# arr = [3,1,5,4,6,9,8,7,2]
# print(*insert_sort(arr))
# arr = [3,1,5,4,6,9,8,7,2]
# print(*quick_soft(arr))
# arr = [3,1,5,4,6,9,8,7,2]
# print(*count_sort(arr))
# arr = [3,1,5,4,6,9,8,7,2]
# print(*arr)


# with open("ban_word.txt", "r",encoding="utf-8") as ban_word_file:
#     with open("shat.txt", "r", encoding="utf-8") as shat_file:
#         with open("clean.txt", "w", encoding="utf-8") as clean_file:
#             all_ban_word=set(ban_word_file.read().split("\n"))
#             chat_text=shat_file.read()
#             current_word=""
#             for char in chat_text:
#                 if char.isalpha():
#                     current_word+=char
#                 else:
#                     if current_word in all_ban_word:
#                         clean_file.write("*"*len(current_word+char))
#                     else:
#                         clean_file.write(current_word + char)
#                     current_word=""
#             if current_word in all_ban_word:
#                 clean_file.write("*" * len(current_word + char))

##############################################################################################################################

# class Photo:
#
#     @staticmethod
#     def make_photo():
#         print("making photo")
#
# class VideoPlayer:
#
#     @staticmethod
#     def play_video():
#         print("playing video")
#
#
# class SmartPhone(Photo, VideoPlayer):
#
#     @staticmethod
#     def call():
#         print("phone is calling")
#
#
# Photo.make_photo()
# VideoPlayer.play_video()
# SmartPhone.call()
# SmartPhone.play_video()
# SmartPhone.make_photo()
#
# s25 = SmartPhone
# s25.make_photo()


# class A:
#
#     @staticmethod
#     def a_method():
#         print("this is A method")
#
#
# class B(A):
#
#     @staticmethod
#     def b_method():
#         print("this is B method")
#
#
# class C(B):
#
#     @staticmethod
#     def c_method():
#         print("this is C method")
#
#
#
# C.a_method()


# class A:
#     @staticmethod
#     def test_method():
#         print("this is A method")
#
#
# class B:
#     @staticmethod
#     def test_method():
#         print("this is B method")
#
# class C(A, B):
#     @staticmethod
#     def test():
#         pass
#
#
# C.test()
# C.test_method()



# class Animal:
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight
#
#     def get_info(self):
#         return f"{self.__class__}{self.name}{self.age}{self.weight}"
#
#
#     def say(self):
#         print("animal say something")
#
#
# class Tiger(Animal):
#     def __init__(self, name, age, weight, height):
#         super().__init__(name, age, weight)
#         self.height = height
#
#     def say(self):
#         print("ARRRRRRRRRRRRRRRR MEEEEEEEEEEEEEEEEEOOOOOOOOOOOOOOOOOW!")
#
#
# class Crocodile(Animal):
#     def __init__(self, name, age, weight, height):
#         super().__init__(name, age, weight)
#         self.height = height
#
#     def say(self):
#         print("ARRRRRRRRRRRRRRRR MEEEEEEEEEEEEEEEEEOOOOOOOOOOOOOOOOOW!")
#
#
# sherhan = Tiger("sher Han", 25, 400, 200)
# sherhan.say()
# print(sherhan.get_info())
#
# sherhan = Tiger("sher Han", 25, 400, 200)
# sherhan.say()
# print(sherhan.get_info())
#
# sherhan = Tiger("sher Han", 25, 400, 200)
# sherhan.say()
# print(sherhan.get_info())

# import math
#
#
# class Figure:
#     def __init__(self, side=1, is_evklid_geometry=True):
#         self.is_evklid_geometry = is_evklid_geometry
#
#     def area(self):
#         return self.side**2
#
#     def perimeter(self):
#         return self.side * 4
#
#
# class Circle(Figure):
#     def __init__(self, radius=1  , is_evklid_geometry=True):
#         super().__init__(is_evklid_geometry)
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius**2
#
#     def perimeter(self):
#         return math.pi * self.radius * 2
#
#
# class Squre(Figure):
#     def __init__(self, side=1, is_evklid_geometry=True):
#         super().__init__(is_evklid_geometry)
#         self.side = side
#
#     def area(self):
#         return self.side**2
#
#     def perimeter(self):
#         return self.side * 4
#
#
# kolobok = Circle(25)
# print(kolobok.area())                   # 1963.4954084936207
# print(kolobok.perimeter())              # 157.07963267948966
#
# test_cpickle = Circle(50)
# print(test_cpickle.area())              # 7853.981633974483
# print(test_cpickle.perimeter())         # 314.1592653589793


# from abc import ABC, abstractmethod
#
#
# class Weapon(ABC):
#     def __init__(self, name, damage, price):
#         self.name = name
#         self.damage = damage
#         self.price = price
#
#     @abstractmethod
#     def fire(self):
#         pass
#
#     @abstractmethod
#     def reload(self):
#         pass
#
#
# class Rifle(Weapon):
#     def __init__(self, name, damage, price, rate_of_fire, count_of_bullets):
#         super().__init__(name, damage, price)
#         self.rate_of_fire = rate_of_fire
#         self.count_of_bullets = count_of_bullets
#
#     def fire(self):
#         if self.count_of_bullets > 0:
#             print(f"{self.name} is shooting on target! Damage is {self.damage}")
#             self.count_of_bullets-=1
#         else:
#             print("Empty bullets.")
#
#     def reload(self):
#         self.count_of_bullets=30
#         print(f"{self.name} is reloading. Current bullet count is {self.count_of_bullets}")
#
#
# class LaserGun(Weapon):
#     def __init__(self, name, damage, price, rate_of_fire, energy_charge):
#         super().__init__(name, damage, price)
#         self.rate_of_fire = rate_of_fire
#         self.energy_charge = energy_charge
#
#     def fire(self):
#         print(f"{self.name} fire with laser to target.")
#
#     def reload(self):
#         print(f"{self.name} is overheating. Stop shooting")
#
#
# class Sword(Weapon):
#     def __init__(self, name, damage, price, length, is_two_handed=False):
#         super().__init__(name, damage, price)
#         self.length = length
#         self.is_two_handed = is_two_handed
#
#     def fire(self):
#         print(f"Attack with {self.name}. Target damaged {self.damage} hp.")
#
#     def reload(self):
#         print(f"new swing.")
#
#
# ak_47 = Rifle(name="AK-47", damage=60, price=50_000, rate_of_fire=80, count_of_bullets=3)
#
# ak_47.fire()
# ak_47.fire()
# ak_47.fire()
# ak_47.fire()
# ak_47.fire()
# ak_47.fire()
# ak_47.fire()
# ak_47.fire()
# ak_47.reload()
#
# m16 = Rifle(name="M16", damage=60, price=50_000, rate_of_fire=90, count_of_bullets=4)
#
# m16.fire()
# m16.fire()
# m16.fire()
# m16.fire()
# m16.fire()
# m16.fire()
# m16.fire()
# m16.fire()
# m16.reload()
#
# death_star = LaserGun("death_star", 1_000_000_000, 100_000_000_000, 0.0001, 100_000_000_000)
#
# death_star.fire()
# death_star.fire()
# death_star.fire()
# death_star.fire()
# death_star.fire()
# death_star.fire()
# death_star.fire()
# death_star.fire()
# death_star.reload()
#
#
# claymore = Sword(name="claymore", damage=15, price=15_000, length=1.5, is_two_handed=True)
#
# claymore.fire()
# claymore.fire()
# claymore.reload()




class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if isinstance(numerator, int) is False or isinstance(denominator, int) is False:
            raise TypeError("Numerator and denominator must be only integer value")

        if denominator == 0:
            raise  ValueError("Denominator must not be equal 0.")


        self.a = numerator
        self.b = denominator

    def __str__(self):
        return f"{self.a}/{self.b}"

    def plus(self, other):
        """
        Вернёт новую дробь.
        :param other:  другой обект
        :return: новый обект
        """
        return Fraction(self.a * other.b + self.b * other.a, self.b * other.b)

    def minus(self, other):
        """
        Вернёт новую дробь.
        :param other:  другой обект
        :return: новый обект
        """
        return Fraction(self.a * other.b + self.b * other.a, self.b * other.b)

    def multiplication(self, other):
        """
        Вернёт новую дробь.
        :param other:  другой обект
        :return: новый обект
        """
        return Fraction(self.a * other.b, self.b * other.a)

    def divide(self, other):
        """
        Вернёт новую дробь.
        :param other:  другой обект
        :return: новый обект
        """
        return Fraction(self.a * other.b, self.b * other.a)


first_number = Fraction(1,4)
second_number = Fraction(3,5)
print(first_number)
print(second_number)
print(first_number.plus(second_number))












