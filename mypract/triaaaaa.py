#text = input("введите предложение")
#print(text.replace("","."))
#print("количество пробелов =", text.count(" "))
# text = input("введите предложение")
#
 for i in range(len(text), 0, -1):
     print(text[:i])
     text = input("введите предложение")
     for i in range(1, len(text) + 1):
         print(text[:i])
# try:
#     number = int(input("введите число: "))
# except:
#     ptint("преобразование прошло неудачно")
# print("завершение программы")
#numbers = list(map(int, input("введите число через пробел:").split()))

#average = sum(numbers) / len(numbers)
#print("среднеарифметическое =", average)