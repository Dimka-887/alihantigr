# import message
#
# print(message.hello)
#
# message.print_message("Hello work")

# from message import print_message
# from message import hello
#
#
# print_message("Hello work")
#
#
# print(hello)
# from message import *
#
#
# print_message("Hello work")
#
#
# print(hello)
# from message import *
#
# print_message("Hello work")
#
#
# def print_message(some_text):
#     print(f"Text: {some_text}")
#
#
# print_message("Hello work")
# import message as mes
#
#
# print(mes.hello)
#
# mes.print_message("Hello work")
# from message import print_message as display
# from message import hello as welcome
#
# print(welcome)
# display("Hello work")
# myfile = open("hello.txt", "w")
#
# try:
#     myfile = open("hello.txt", "w")
#     try:
#         print("Работа с файлом")
#     finally:
#         myfile.close()
# except Exception as ex:
#     print(ex)
# Программа подсчета слов в файле
# import os
#
#
# def get_words(filename):
#     with open(filename, encoding="utf8") as file:
#         text = file.read()
#     text = text.replace("\n", " ")
#     text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
#     text = text.lower()
#     words = text.split()
#     words.sort()
#     return words
#
#
# def get_words_dict(words):
#     words_dict = dict()
#
#     for word in words:
#         if word in words_dict:
#             words_dict[word] = words_dict[word] + 1
#         else:
#             words_dict[word] = 1
#     return words_dict
#
#
# def main():
#     filename = input("Введите путь к файлу: ")
#     if not os.path.exists(filename):
#         print("Указанный файл не существует")
#     else:
#         words = get_words(filename)
#         words_dict = get_words_dict(words)
#         print(f"Кол-во слов: {len(words)}")
#         print(f"Кол-во уникальных слов: {len(words_dict)}")
#         print("Все использованные слова:")
#         for word in words_dict:
#             print(word.ljust(20), words_dict[word])
#
#
# if __name__ == "__main__":
#     main()
# def print_hello(language):
#     match language:
#         case "russian":
#             print("Привет")
#         case "english":
#             print("Hello")
#         case "german":
#             print("Hallo")
#
#
# print_hello("english")  # Hello
# print_hello("german")  # Hallo
# print_hello("russian")  # Привет
# case "english":
#     print("Hello")
# def operation(a, b, code):
#     match code:
#         case 1:
#             return a + b
#         case 2:
#             return a - b
#         case 3:
#             return a * b
#         case _:
#             return 0
#
#
# print(operation(10, 5, 1))  # 15
# print(operation(10, 5, 2))  # 5
# print(operation(10, 5, 3))  # 50
# print(operation(10, 5, 4))  # 0
# def print_data(user):
#     match user:
#         case ("Tom", 37):
#             print("default user")
#         case ("Tom", age):
#             print(f"Age: {age}")
#         case (name, 22):
#             print(f"Name: {name}")
#         case (name, age):
#             print(f"Name: {name}  Age: {age}")
#
#
# print_data(("Tom", 37))  # default user
# print_data(("Tom", 28))  # Age: 28
# print_data(("Sam", 22))  # Name: Sam
# print_data(("Bob", 41))  # Name: Bob  Age: 41
# print_data(("Tom", 33, "Google"))  # не соответствует ни одному из шаблонов
# def print_data(user):
#     match user:
#         case (name, age):
#             print(f"Name: {name}  Age: {age}")
#         case (name, age, company):
#             print(f"Name: {name}  Age: {age}  Company: {company}")
#         case (name, age, company, lang):
#             print(f"Name: {name}  Age: {age}  Company: {company} Language: {lang}")
#
#
# print_data(("Tom", 37))  # Name: Tom  Age: 37
# print_data(("Sam", 22, "Microsoft"))  # Name: Sam  Age: 22  Company: Microsoft
# print_data(("Bob", 41, "Google", "english"))
# # Name: Bob  Age: 41  Company: Google Language: english
# def print_people(people):
#     match people:
#         case ["Tom", "Sam", "Bob"]:
#             print("default people")
#         case ["Tom", second, _]:
#             print(f"Second Person: {second}")
#         case [first, second, third]:
#             print(f"{first}, {second}, {third}")
#
#
# print_people(["Tom", "Sam", "Bob"])
# print_people(["Tom", "Mike", "Bob"])
# print_people(["Alice", "Bill", "Kate"])
# print_people(["Tom", "Kate"])
s