#            задание №1


type_List = [8, 5/6, True, [1, 2], "Hi", {"name": "Svetlana", "Michel": "Nadu"}, (1, 2)]
for i in range(len(type_List)):
   print(f"Тип переменной в списке: {type(type_List[i])}")


#            задание №2


q = int(input("сколько элементов вы хотите добавить?\n\t введите количество элементов: "))
my_lst = []
for i in range(q):
    my_lst.append(input(f"Item # {i + 1} : "))
print(f"ваш просмотр списка элементов:\n{my_lst}")
for x in range(0, (len(my_lst) - 1),2):
    my_lst[x], my_lst[x+1] = my_lst[x+1], my_lst[x]
print(f"Ваш изменненый список элементов:\n{my_lst}")

#           задание №3



while True:
   user_month = input('введите номер месяцф от 1 до 12: ')
   if user_month.isdigit() and 0 < int(user_month) <= 12:
      season_1 = ['зима', 'весна', 'лето', 'осень', 'зима']
      season_2 = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень', 4: 'зима'}
      print(f'Список сезонов - {season_1[int(user_month) // 3]}\nСловарь сезонов - {season_2[int(user_month) // 3]}')
      break
   else:
      print("error!!!")

 #         задание №4


text = input("Введите строку из нескольких слов, разделенных пробелами: ")
T = text.split()
for x, y in enumerate (T, start=1) :
    if len(y) > 11 :
        y = y[:10]
        print(x, y)
    else :
       print (x,y)


#         задание №5


my_list = [9, 8, 7, 6, 5, 4, 3, 2]
new_number = ""

while new_number !="t":
    i = 0
    new_number = input("Введите новый элемент рейтинга ввиде натурального числа.\nДля выхода - t\n")

    if new_number.isdigit():
        for n in my_list:
           if int(new_number) <= n:
                i += 1
           else:
               break
        my_list.insert(i, float(new_number))
    print(my_list)









