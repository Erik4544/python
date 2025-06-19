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



arr = [3,2,1,5,4,6,9,8,7]
