# # # # # # # # import json
# # # # # # # #
# # # # # # # #
# # # # # # # # def add_book():
# # # # # # # #     global new_book_id          # будем изменять глобальную переменную
# # # # # # # #     global all_books_data
# # # # # # # #     print("\n\n")
# # # # # # # #     print("-" * 100)
# # # # # # # #     title = input("Название книги: ")
# # # # # # # #     author = input("Автор книги: ")
# # # # # # # #     year = int(input("Год издания книги: "))
# # # # # # # #     all_books_data[str(new_book_id)] = {
# # # # # # # #         "title": title,
# # # # # # # #         "author": author,
# # # # # # # #         "year": year
# # # # # # # #     }
# # # # # # # #     new_book_id += 1        # следующая книга будет иметь id на 1 больше
# # # # # # # #     print(f"Книга '{title}' успешно добавлена в библиотеку.")
# # # # # # # #     print("-" * 100)
# # # # # # # #     save_data()
# # # # # # # #     """
# # # # # # # #      0: {
# # # # # # # #         "title": "Война и мир",
# # # # # # # #         "author": "Толстой Л.Н.",
# # # # # # # #         "year": 1962
# # # # # # # #     },
# # # # # # # #     1: {
# # # # # # # #         "title": "Анна Каренина",
# # # # # # # #         "author": "Толстой Л.Н.",
# # # # # # # #         "year": 1965
# # # # # # # #     }
# # # # # # # #     """
# # # # # # # #
# # # # # # # #
# # # # # # # # def delete_book():
# # # # # # # #     print("\n\n")
# # # # # # # #     print("-" * 100)
# # # # # # # #     show_data()
# # # # # # # #     book_id=input("Введите id книги, которую надо удалить: ")
# # # # # # # #     all_books_data.pop(book_id)
# # # # # # # #     print("Книга успешно удалена.")
# # # # # # # #
# # # # # # # # def search_book():
# # # # # # # #     print("\n\n")
# # # # # # # #     print("-" * 100)
# # # # # # # #     search_year=int(input("Пойск по году издания. Введите год: "))
# # # # # # # #     for id, book_data in all_books_data.items():
# # # # # # # #         title=book_data["title"]
# # # # # # # #         author=book_data["author"]
# # # # # # # #         year=book_data["year"]
# # # # # # # #         if year == search_year:
# # # # # # # #             print(f"{id}) {title}'; {author}; {year} r.")
# # # # # # # #
# # # # # # # # def change_book_data():
# # # # # # # #     print("\n\n")
# # # # # # # #     print("-" * 100)
# # # # # # # #     show_data()
# # # # # # # #     book_id=input("Введите id книги, которую надо изменить: ")
# # # # # # # #     name=input("Новое название: ")
# # # # # # # #     author=input("Новый автор: ")
# # # # # # # #     year=input("Новый год: ")
# # # # # # # #     all_books_data[book_id] = {
# # # # # # # #         "title": name,
# # # # # # # #         "author": author,
# # # # # # # #         "year": year
# # # # # # # #     }
# # # # # # # #
# # # # # # # # def save_data():
# # # # # # # #     with open("book_database.json","w",encoding="utf-8") as file:
# # # # # # # #         json.dump(all_books_data, file, ensure_ascii=False,indent=4)
# # # # # # # #     with open("book_id_info.txt", "w", encoding="utf-8") as id_file:
# # # # # # # #         id_file.write(str(new_book_id))
# # # # # # # #
# # # # # # # # def show_data():
# # # # # # # #     print("\n\n")
# # # # # # # #     print("-" * 100)
# # # # # # # #     for id, book_data in all_books_data.items():
# # # # # # # #         title=book_data["title"]
# # # # # # # #         author=book_data["author"]
# # # # # # # #         year=book_data["year"]
# # # # # # # #         print(f"{id}) {title}'; {author}; {year} r.")
# # # # # # # #         print("-" * 100)
# # # # # # # #         print("\n\n")
# # # # # # # #
# # # # # # # # try:
# # # # # # # #     with open("book_database.json","r",encoding="utf-8") as file:
# # # # # # # #         all_books_data = json.load(file)     # тут будем держать словарь о все книгах.
# # # # # # # #     with open("book_id_info.txt", "r", encoding="utf-8") as id_file:
# # # # # # # #         new_book_id=int(id_file.read())      #
# # # # # # # # except:
# # # # # # # #     all_books_data = {}     # тут будем держать словарь о все книгах.
# # # # # # # #     new_book_id = 0           # id новой будущей книги при добавлении
# # # # # # # #
# # # # # # # #
# # # # # # # # while True:
# # # # # # # #     print("1. Показать все книги.")
# # # # # # # #     print("2. Добавить книгу.")
# # # # # # # #     print("3. Удалить книгу.")
# # # # # # # #     print("4. Найти книгу.")
# # # # # # # #     print("5. Изменить данные у книги.")
# # # # # # # #     print("0. Выход.")
# # # # # # # #     user_choice = input("Ваш выбор(номер): ")
# # # # # # # #     match user_choice:
# # # # # # # #         case "1": show_data()
# # # # # # # #         case "2": add_book()
# # # # # # # #         case "3": delete_book()
# # # # # # # #         case "4": search_book()
# # # # # # # #         case "5": change_book_data()
# # # # # # # #         case "0": break
# # # # # # # #         case _: print("Неизвестная команда. Требуется только номер.")
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # # ##############################################################################################################################
# # # # # # #
# # # # # # # # class Photo:
# # # # # # # #
# # # # # # # #     @staticmethod
# # # # # # # #     def make_photo():
# # # # # # # #         print("making photo")
# # # # # # # #
# # # # # # # # class VideoPlayer:
# # # # # # # #
# # # # # # # #     @staticmethod
# # # # # # # #     def play_video():
# # # # # # # #         print("playing video")
# # # # # # # #
# # # # # # # #
# # # # # # # # class SmartPhone(Photo, VideoPlayer):
# # # # # # # #
# # # # # # # #     @staticmethod
# # # # # # # #     def call():
# # # # # # # #         print("phone is calling")
# # # # # # # #
# # # # # # # #
# # # # # # # # Photo.make_photo()
# # # # # # # # VideoPlayer.play_video()
# # # # # # # # SmartPhone.call()
# # # # # # # # SmartPhone.play_video()
# # # # # # # # SmartPhone.make_photo()
# # # # # # # #
# # # # # # # # s25 = SmartPhone
# # # # # # # # s25.make_photo()
# # # # # # #
# # # # # # #
# # # # # # # # class A:
# # # # # # # #
# # # # # # # #     @staticmethod
# # # # # # # #     def a_method():
# # # # # # # #         print("this is A method")
# # # # # # # #
# # # # # # # #
# # # # # # # # class B(A):
# # # # # # # #
# # # # # # # #     @staticmethod
# # # # # # # #     def b_method():
# # # # # # # #         print("this is B method")
# # # # # # # #
# # # # # # # #
# # # # # # # # class C(B):
# # # # # # # #
# # # # # # # #     @staticmethod
# # # # # # # #     def c_method():
# # # # # # # #         print("this is C method")
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # # C.a_method()
# # # # # # #
# # # # # # #
# # # # # # # # class A:
# # # # # # # #     @staticmethod
# # # # # # # #     def test_method():
# # # # # # # #         print("this is A method")
# # # # # # # #
# # # # # # # #
# # # # # # # # class B:
# # # # # # # #     @staticmethod
# # # # # # # #     def test_method():
# # # # # # # #         print("this is B method")
# # # # # # # #
# # # # # # # # class C(A, B):
# # # # # # # #     @staticmethod
# # # # # # # #     def test():
# # # # # # # #         pass
# # # # # # # #
# # # # # # # #
# # # # # # # # C.test()
# # # # # # # # C.test_method()
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # # # class Animal:
# # # # # # # #     def __init__(self, name, age, weight):
# # # # # # # #         self.name = name
# # # # # # # #         self.age = age
# # # # # # # #         self.weight = weight
# # # # # # # #
# # # # # # # #     def get_info(self):
# # # # # # # #         return f"{self.__class__}{self.name}{self.age}{self.weight}"
# # # # # # # #
# # # # # # # #
# # # # # # # #     def say(self):
# # # # # # # #         print("animal say something")
# # # # # # # #
# # # # # # # #
# # # # # # # # class Tiger(Animal):
# # # # # # # #     def __init__(self, name, age, weight, height):
# # # # # # # #         super().__init__(name, age, weight)
# # # # # # # #         self.height = height
# # # # # # # #
# # # # # # # #     def say(self):
# # # # # # # #         print("ARRRRRRRRRRRRRRRR MEEEEEEEEEEEEEEEEEOOOOOOOOOOOOOOOOOW!")
# # # # # # # #
# # # # # # # #
# # # # # # # # class Crocodile(Animal):
# # # # # # # #     def __init__(self, name, age, weight, height):
# # # # # # # #         super().__init__(name, age, weight)
# # # # # # # #         self.height = height
# # # # # # # #
# # # # # # # #     def say(self):
# # # # # # # #         print("ARRRRRRRRRRRRRRRR MEEEEEEEEEEEEEEEEEOOOOOOOOOOOOOOOOOW!")
# # # # # # # #
# # # # # # # #
# # # # # # # # sherhan = Tiger("sher Han", 25, 400, 200)
# # # # # # # # sherhan.say()
# # # # # # # # print(sherhan.get_info())
# # # # # # # #
# # # # # # # # sherhan = Tiger("sher Han", 25, 400, 200)
# # # # # # # # sherhan.say()
# # # # # # # # print(sherhan.get_info())
# # # # # # # #
# # # # # # # # sherhan = Tiger("sher Han", 25, 400, 200)
# # # # # # # # sherhan.say()
# # # # # # # # print(sherhan.get_info())
# # # # # # #
# # # # # # # # import math
# # # # # # # #
# # # # # # # #
# # # # # # # # class Figure:
# # # # # # # #     def __init__(self, side=1, is_evklid_geometry=True):
# # # # # # # #         self.is_evklid_geometry = is_evklid_geometry
# # # # # # # #
# # # # # # # #     def area(self):
# # # # # # # #         return self.side**2
# # # # # # # #
# # # # # # # #     def perimeter(self):
# # # # # # # #         return self.side * 4
# # # # # # # #
# # # # # # # #
# # # # # # # # class Circle(Figure):
# # # # # # # #     def __init__(self, radius=1  , is_evklid_geometry=True):
# # # # # # # #         super().__init__(is_evklid_geometry)
# # # # # # # #         self.radius = radius
# # # # # # # #
# # # # # # # #     def area(self):
# # # # # # # #         return math.pi * self.radius**2
# # # # # # # #
# # # # # # # #     def perimeter(self):
# # # # # # # #         return math.pi * self.radius * 2
# # # # # # # #
# # # # # # # #
# # # # # # # # class Squre(Figure):
# # # # # # # #     def __init__(self, side=1, is_evklid_geometry=True):
# # # # # # # #         super().__init__(is_evklid_geometry)
# # # # # # # #         self.side = side
# # # # # # # #
# # # # # # # #     def area(self):
# # # # # # # #         return self.side**2
# # # # # # # #
# # # # # # # #     def perimeter(self):
# # # # # # # #         return self.side * 4
# # # # # # # #
# # # # # # # #
# # # # # # # # kolobok = Circle(25)
# # # # # # # # print(kolobok.area())                   # 1963.4954084936207
# # # # # # # # print(kolobok.perimeter())              # 157.07963267948966
# # # # # # # #
# # # # # # # # test_cpickle = Circle(50)
# # # # # # # # print(test_cpickle.area())              # 7853.981633974483
# # # # # # # # print(test_cpickle.perimeter())         # 314.1592653589793
# # # # # # #
# # # # # # #
# # # # # # # # from abc import ABC, abstractmethod
# # # # # # # #
# # # # # # # #
# # # # # # # # class Weapon(ABC):
# # # # # # # #     def __init__(self, name, damage, price):
# # # # # # # #         self.name = name
# # # # # # # #         self.damage = damage
# # # # # # # #         self.price = price
# # # # # # # #
# # # # # # # #     @abstractmethod
# # # # # # # #     def fire(self):
# # # # # # # #         pass
# # # # # # # #
# # # # # # # #     @abstractmethod
# # # # # # # #     def reload(self):
# # # # # # # #         pass
# # # # # # # #
# # # # # # # #
# # # # # # # # class Rifle(Weapon):
# # # # # # # #     def __init__(self, name, damage, price, rate_of_fire, count_of_bullets):
# # # # # # # #         super().__init__(name, damage, price)
# # # # # # # #         self.rate_of_fire = rate_of_fire
# # # # # # # #         self.count_of_bullets = count_of_bullets
# # # # # # # #
# # # # # # # #     def fire(self):
# # # # # # # #         if self.count_of_bullets > 0:
# # # # # # # #             print(f"{self.name} is shooting on target! Damage is {self.damage}")
# # # # # # # #             self.count_of_bullets-=1
# # # # # # # #         else:
# # # # # # # #             print("Empty bullets.")
# # # # # # # #
# # # # # # # #     def reload(self):
# # # # # # # #         self.count_of_bullets=30
# # # # # # # #         print(f"{self.name} is reloading. Current bullet count is {self.count_of_bullets}")
# # # # # # # #
# # # # # # # #
# # # # # # # # class LaserGun(Weapon):
# # # # # # # #     def __init__(self, name, damage, price, rate_of_fire, energy_charge):
# # # # # # # #         super().__init__(name, damage, price)
# # # # # # # #         self.rate_of_fire = rate_of_fire
# # # # # # # #         self.energy_charge = energy_charge
# # # # # # # #
# # # # # # # #     def fire(self):
# # # # # # # #         print(f"{self.name} fire with laser to target.")
# # # # # # # #
# # # # # # # #     def reload(self):
# # # # # # # #         print(f"{self.name} is overheating. Stop shooting")
# # # # # # # #
# # # # # # # #
# # # # # # # # class Sword(Weapon):
# # # # # # # #     def __init__(self, name, damage, price, length, is_two_handed=False):
# # # # # # # #         super().__init__(name, damage, price)
# # # # # # # #         self.length = length
# # # # # # # #         self.is_two_handed = is_two_handed
# # # # # # # #
# # # # # # # #     def fire(self):
# # # # # # # #         print(f"Attack with {self.name}. Target damaged {self.damage} hp.")
# # # # # # # #
# # # # # # # #     def reload(self):
# # # # # # # #         print(f"new swing.")
# # # # # # # #
# # # # # # # #
# # # # # # # # ak_47 = Rifle(name="AK-47", damage=60, price=50_000, rate_of_fire=80, count_of_bullets=3)
# # # # # # # #
# # # # # # # # ak_47.fire()
# # # # # # # # ak_47.fire()
# # # # # # # # ak_47.fire()
# # # # # # # # ak_47.fire()
# # # # # # # # ak_47.fire()
# # # # # # # # ak_47.fire()
# # # # # # # # ak_47.fire()
# # # # # # # # ak_47.fire()
# # # # # # # # ak_47.reload()
# # # # # # # #
# # # # # # # # m16 = Rifle(name="M16", damage=60, price=50_000, rate_of_fire=90, count_of_bullets=4)
# # # # # # # #
# # # # # # # # m16.fire()
# # # # # # # # m16.fire()
# # # # # # # # m16.fire()
# # # # # # # # m16.fire()
# # # # # # # # m16.fire()
# # # # # # # # m16.fire()
# # # # # # # # m16.fire()
# # # # # # # # m16.fire()
# # # # # # # # m16.reload()
# # # # # # # #
# # # # # # # # death_star = LaserGun("death_star", 1_000_000_000, 100_000_000_000, 0.0001, 100_000_000_000)
# # # # # # # #
# # # # # # # # death_star.fire()
# # # # # # # # death_star.fire()
# # # # # # # # death_star.fire()
# # # # # # # # death_star.fire()
# # # # # # # # death_star.fire()
# # # # # # # # death_star.fire()
# # # # # # # # death_star.fire()
# # # # # # # # death_star.fire()
# # # # # # # # death_star.reload()
# # # # # # # #
# # # # # # # #
# # # # # # # # claymore = Sword(name="claymore", damage=15, price=15_000, length=1.5, is_two_handed=True)
# # # # # # # #
# # # # # # # # claymore.fire()
# # # # # # # # claymore.fire()
# # # # # # # # claymore.reload()
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # # class Fraction:
# # # # # # #     def __init__(self, numerator: int, denominator: int):
# # # # # # #         if isinstance(numerator, int) is False or isinstance(denominator, int) is False:
# # # # # # #             raise TypeError("Numerator and denominator must be only integer value")
# # # # # # #
# # # # # # #         if denominator == 0:
# # # # # # #             raise  ValueError("Denominator must not be equal 0.")
# # # # # # #
# # # # # # #
# # # # # # #         self.a = numerator
# # # # # # #         self.b = denominator
# # # # # # #
# # # # # # #     def __str__(self):
# # # # # # #         return f"{self.a}/{self.b}"
# # # # # # #
# # # # # # #     def plus(self, other):
# # # # # # #         """
# # # # # # #         Вернёт новую дробь.
# # # # # # #         :param other:  другой обект
# # # # # # #         :return: новый обект
# # # # # # #         """
# # # # # # #         return Fraction(self.a * other.b + self.b * other.a, self.b * other.b)
# # # # # # #
# # # # # # #     def minus(self, other):
# # # # # # #         """
# # # # # # #         Вернёт новую дробь.
# # # # # # #         :param other:  другой обект
# # # # # # #         :return: новый обект
# # # # # # #         """
# # # # # # #         return Fraction(self.a * other.b + self.b * other.a, self.b * other.b)
# # # # # # #
# # # # # # #     def multiplication(self, other):
# # # # # # #         """
# # # # # # #         Вернёт новую дробь.
# # # # # # #         :param other:  другой обект
# # # # # # #         :return: новый обект
# # # # # # #         """
# # # # # # #         return Fraction(self.a * other.b, self.b * other.a)
# # # # # # #
# # # # # # #     def divide(self, other):
# # # # # # #         """
# # # # # # #         Вернёт новую дробь.
# # # # # # #         :param other:  другой обект
# # # # # # #         :return: новый обект
# # # # # # #         """
# # # # # # #         return Fraction(self.a * other.b, self.b * other.a)
# # # # # # #
# # # # # # #     def __add__(self, other):
# # # # # # #         """
# # # # # # #         Вернёт новую дробь.
# # # # # # #         :param other:  другой обект
# # # # # # #         :return: новый обект
# # # # # # #         """
# # # # # # #         return Fraction(self.a * other.b + self.b * other.a, self.b * other.b)
# # # # # # #
# # # # # # #     def __sub__(self, other):
# # # # # # #         """
# # # # # # #         Вернёт новую дробь.
# # # # # # #         :param other:  другой обект
# # # # # # #         :return: новый обект
# # # # # # #         """
# # # # # # #         return Fraction(self.a * other.b - self.b * other.a, self.b * other.b)
# # # # # # #
# # # # # # #     def __ne__(self, other):
# # # # # # #         return self.a != other.a or self.b != other.b
# # # # # # #
# # # # # # #     def __gt__(self, other):
# # # # # # #         return self.a * other.b > self.b * other.a
# # # # # # #
# # # # # # #     def __ge__(self, other):
# # # # # # #         return self.a * other.b >= self.b * other.a
# # # # # # #
# # # # # # #     def __lt__(self, other):
# # # # # # #         return self.a * other.b < self.b * other.a
# # # # # # #
# # # # # # #     def __le__(self, other):
# # # # # # #         return self.a * other.b <= self.b * other.a
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # # first_number = Fraction(1,4)
# # # # # # # second_number = Fraction(3,5)
# # # # # # # print(first_number)
# # # # # # # print(second_number)
# # # # # # # print(first_number.plus(second_number))
# # # # # # # print(first_number + second_number)
# # # # # # # print(first_number - second_number)
# # # # # # # print(first_number - second_number)
# # # # # # # print(first_number < second_number)
# # # # # # #
# # # # # # # from decimal import Decimal
# # # # # #
# # # # # #
# # # # # #
# # # # # # class Money:
# # # # # #     def __init__(self, a=0, b=0, valuta="RUB"):
# # # # # #         if isinstance(a, int) is False or isinstance(b, int) is False:
# # # # # #             raise ValueError("Main and secondary value must be integer")
# # # # # #         if isinstance(valuta, str) is False:
# # # # # #             raise ValueError("Valuta must be only str")
# # # # # #         self.__a = a
# # # # # #         self.__b = b
# # # # # #         if self.__b >= 100:
# # # # # #             self.__a += self.__b // 100
# # # # # #             self.__b = self.__b % 100
# # # # # #         self.__valuta = valuta
# # # # # #
# # # # # #     def __str__(self):
# # # # # #         if self.__b < 10:
# # # # # #             return f"{self.__a}.0{self.__b}; {self.__valuta};"
# # # # # #         return f"{self.__a}.{self.__b}; {self.__valuta};"
# # # # # #
# # # # # #     def set_main_valua(self, valua):
# # # # # #         if isinstance(valua, int) is False or isinstance(b, int) is False:
# # # # # #             raise ValueError("Main and secondary value must be integer")
# # # # # #         self.__a = valua
# # # # # #
# # # # # #     def set_secondary_value(self, valua):
# # # # # #         if isinstance(valua, int) is False or isinstance(b, int) is False:
# # # # # #             raise ValueError("Main and secondary value must be integer")
# # # # # #         if value >= 100:
# # # # # #             self.__a += value //100
# # # # # #             self.__b = value % 100
# # # # # #         else:
# # # # # #             self.__b = value
# # # # # #
# # # # # #     def change_valuta(self, new_valuta: str):
# # # # # #         if isinstance(new_valuta, str) is False:
# # # # # #             raise ValueError("Valuta must be only string")
# # # # # #         self.__valuta = new_valuta
# # # # # #
# # # # # #     def __add__(self, other):
# # # # # #         if self.__valuta != other.__valuta:
# # # # # #             raise ValueError("Difference valuta! Cannot summ")
# # # # # #         total_secondary_value = self.__b + other.__b
# # # # # #
# # # # # #
# # # # # #
# # # # # # vasyas_pocket = Money(15,20, "USD")
# # # # # # petyas_pocket = Money(15,20,)
# # # # # # bob_pocket = Money(2,4)
# # # # # # john_pocket = Money(10,520, "USD")
# # # # # #
# # # # # # print(vasyas_pocket)
# # # # # # print(bob_pocket)
# # # # # #
# # # # # # bob_pocket.set_main_valua(100)
# # # # # #
# # # # # # print(bob_pocket)
# # # # # # print(john_pocket)
# # # # # from abc import ABC, abstractmethod
# # # # # from multiprocessing.managers import all_methods
# # # # #
# # # # #
# # # # # class Ship(ABC):
# # # # #     def __init__(self, name: str, mass: int, length: int, country: str, year: int):
# # # # #         self.name = name
# # # # #         self.mass = mass
# # # # #         self.length = length
# # # # #         self.country = country
# # # # #         self.year = year
# # # # #
# # # # #     @abstractmethod
# # # # #     def moving(self):
# # # # #         pass
# # # # #
# # # # #     @abstractmethod
# # # # #     def shot(self):
# # # # #         pass
# # # # #
# # # # # class Frigate(Ship):
# # # # #     def __init__(self, name: str, mass: int, length: int, country: str, year: int, torpedoes_type: str, ammo: int):
# # # # #         super().__init__(name, mass, length, country, year)
# # # # #         self.torpedoes_type = torpedoes_type
# # # # #         self.ammo = ammo
# # # # #
# # # # #     def moving(self):
# # # # #         print(f"Frigate {self.name} is moving to fast!")
# # # # #
# # # # #     def shot(self):
# # # # #         if self.ammo > 0:
# # # # #             print(f"frigate {self.name} is shooting! Torpedoes moving to target.")
# # # # #         else:
# # # # #             print("Empty ammo!!!")
# # # # #
# # # # # class Destroyer(Ship):
# # # # #     def __init__(self, name: str, mass: int, length: int, country: str, year: int, anti_submarines_bombs: str, ammo: int):
# # # # #         super().__init__(name, mass, length, country, year)
# # # # #         self.anti_submarines_bombs = anti_submarines_bombs
# # # # #         self.ammo = ammo
# # # # #
# # # # #     def moving(self):
# # # # #         print(f"Frigate {self.name} is moving very fast!")
# # # # #
# # # # #     def shot(self):
# # # # #         if self.ammo > 0:
# # # # #             print(f"frigate {self.name} is shooting with {self.anti_submarines_bombs}! Bombs exploding")
# # # # #         else:
# # # # #             print("Empty ammo!!!")
# # # # #
# # # # # class Cruiser(Ship):
# # # # #     def __init__(self, name: str, mass: int, length: int, country: str, year: int, wings_rocket: str, ammo: int):
# # # # #         super().__init__(name, mass, length, country, year)
# # # # #         self.wings_rocket = wings_rocket
# # # # #         self.ammo = ammo
# # # # #
# # # # #     def moving(self):
# # # # #         print(f"Frigate {self.name} is moving to slow!")
# # # # #
# # # # #     def shot(self):
# # # # #         if self.ammo > 0:
# # # # #             print(f"frigate {self.name} is shooting with {self.wings_rocket}! To target")
# # # # #         else:
# # # # #             print("Empty ammo!!!")
# # # # #
# # # # # cruiser_moscow = Cruiser(
# # # # #     name="moscow",
# # # # #     mass=20_000,
# # # # #     length=250,
# # # # #     country="Rassia",
# # # # #     year=1970,
# # # # #     wings_rocket="kaliber",
# # # # #     ammo=50
# # # # # )
# # # # # cruiser_moscow.moving()
# # # # # cruiser_moscow.moving()
# # # # # cruiser_moscow.moving()
# # # # #
# # # # # cruiser_moscow.shot()
# # # # # cruiser_moscow.shot()
# # # # class ConverterMetricImperial:
# # # #     @staticmethod
# # # #     def miles_to_kilomers(miles):
# # # #         return miles / 1.60934
# # # #
# # # import pickle
# # #
# # #
# # # class Book:
# # #     def __init__(self, title, author, year):
# # #         self.title = title
# # #         self.author = author
# # #         self.year = year
# # #
# # #     def __str__(self):
# # #         return f"{self.title}; {self.author}; {self.year};"
# # #
# # # class Reader:
# # #     def __init__(self, full_name, reader_id):
# # #         self.full_name = full_name
# # #         self.reader_id = reader_id
# # #         self.all_books = []
# # #
# # #     def __str__(self):
# # #         return f"{self.full_name}; {self.reader_id};"
# # #
# # #     def add_book(self, book):
# # #         self.all_books.append(book)
# # #
# # #     def books_on_hand_info(self):
# # #         for book in self.all_books:
# # #             print(book)
# # #
# # #
# # # class Library:
# # #     def __init__(self, name, address):
# # #         self.name = name
# # #         self.address = address
# # #         self.all_books = []
# # #         self.all_readers = []
# # #
# # #     def add_book_to_library(self):
# # #         title = input("название книги; ")
# # #         auther = input("Автор книги; ")
# # #         year = input("Год издания; ")
# # #         self.all_books.append(Book(title, auther, year))
# # #         print("\(@^0^@)/")
# # #         self.save_data()
# # #
# # #     def add_new_reader(self):
# # #         pass
# # #
# # #     def show_all_books(self):
# # #         for book in self.all_books:
# # #             print(book)
# # #
# # #     def show_all_readers(self):
# # #         pass
# # #
# # #     def show_reader_books(self):
# # #         pass
# # #
# # #     def run(self):
# # #         while True:
# # #             self.load_data()
# # #             print("1. -добавить новую книгу")
# # #             print("2. -добавить нового читателя")
# # #             print("3. -показ всех книг")
# # #             print("4. -показ всех чита")
# # #             print("5. -показ книг")
# # #             print("6. -")
# # #             print("0. -")
# # #             user_chouce = input("Ваш выбор; ")
# # #             match user_chouce:
# # #                 case "1": self.add_book_to_library()
# # #                 case "2": self.add_new_reader()
# # #                 case "3": self.show_all_books()
# # #                 case "4": self.show_all_readers()
# # #                 case "5": self.show_reader_books()
# # #                 case "6": pass
# # #                 case "0": return
# # #                 case "-": print("(｀O′)")
# # #
# # #     def save_data(self):
# # #         with open(f"{self.name}_library.pkl", "wb") as ffile:
# # #             pickle.dump(self, file=ffile)
# # #
# # #     def load_data(self):
# # #         with open(f"{self.name}_library.pkl", "rb") as ffile:
# # #             data = pickle.load(ffile)
# # #             self.all_books = data.ffile
# # #             self.all_readers = data.all_readers
# # #             print("(￣o￣) . z Z")
# # #
# # #
# # #
# # #
# # # # war_and_peace = Book(
# # # #     title="Война и мир",
# # # #     author="Толстой Лев Николаев",
# # # #     year=1962
# # # # )
# # # # anna_karenina = Book(
# # # #     title="Анна Кареина",
# # # #     author="Толстой Лев Николаев",
# # # #     year=1967
# # # # )
# # # #
# # # # vasya = Reader(
# # # #     full_name="Вася Васин",
# # # #     reader_id=0
# # # # )
# # # best_library = Library("hz","dfgtxd")
# # # best_library.run()
# # #
# # #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # class MyStack:
# #     def __init__(self):
# #         self.__stack = []
# #         self.__length = 0
# #
# #     def add(self, value):
# #         """
# #         добавляет
# #         :param value:
# #         :return:
# #         """
# #         self.__stack.append(value)
# #         self.__length += 1
# #
# #     def pop(self):
# #         if self.__length > 0:
# #             value = self.__stack.pop()
# #             self.__length -=1
# #             return value
# #         raise IndexError("Stack is empty!")
# #
# #     def __len__(self):
# #         return self.__length
# #
# #
# #
# # simple_stack = MyStack()
# # simple_stack.add("Vasya")
# # simple_stack.add("Petya")
# # simple_stack.add("Bob")
# #
# # print(simple_stack.pop())
# # print(simple_stack.pop())
# # print(simple_stack.pop())
# #
# # print(len(simple_stack))
#
#
#
#
# # from collections import Counter
# #
# #
# # some_list = ["apple", "banana", "orange", "^_~", "U_U", "banana", "orange", "^_~", "U_U", "banana", "^_~", "U_U"]
# # """
# # aasdsa;j
# # dsf
# # sdf
# # sd
# # """
# # result = {}
# # for elen in some_list:
# #     if elen in result:
# #         result[elen] += 1
# #     else:
# #         result[elen] = 1
# #
# # print(some_list)
# # print(result)
# #
# #
# # print()
# # result = Counter(some_list)
# #
# # print(some_list)
# # print(result)
#
#
#
# # from queue import Queue
# #
# #
# #
# # my_queue = Queue()
# # my_queue.put("vasya")
# # my_queue.put("Petya")
# # my_queue.put("Bob")
# #
# # print(my_queue.get())
# # print(my_queue.get())
# # print(my_queue.get())
#
#
#
# class Node:
#     def __init__(self, value, prev=None, next=None):
#         self.value = value
#         self.prev = prev
#         self.next = next
#
#
# class LinkedList:
#     def __init__(self, value):
#         self.last = Node(value)
#         self.start = self.last
#         self.length = 1
#
#     def add_right(self, value):
#         new_node = Node(value)
#         new_node.prev = self.last
#         self.last.next = new_node
#         self.last = new_node
#         self.length += 1
#
#     def add_left(self, value):
#         new_node = Node(value)
#         new_node.prev = self.start
#         self.last.prev = new_node
#         self.last = new_node
#         self.length += 1
#
#     def pop_left(self, value):
#         if self.length ==0:
#             raise IndexError("dsfsdfs")
#         value = self.last.value
#         if
#         self.last = self.last.value
#         self.last.next = None
#         self.length -= 1
#
#
#     def pop_left(self, value):
#         new_node = Node(0)
#
#
#
#
# my_linked_list = LinkedList(5)
# my_linked_list.add_right(10)
# my_linked_list.add_left(15)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


from collections import deque




























