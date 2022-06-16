cook_book = {}


def open_file():
    with open('заготовка.txt', 'r', encoding='utf-8') as file:
        # numer_line = 0
        ingredients_list = []
        for lol in file:
            line = lol.strip()
            # numer_line =+ 1
            if line != None:
                if line.isdigit():
                    True
                else:
                    if "|" not in line:
                        name_dictionary = line
                        a = []
                        cook_book[line] = []
                        ingredients_list = []
                    else:
                        list_word = line.split(' | ')
                        ingredient = {'ingredient_name': list_word[0], 'quantity': list_word[1],
                                      'measure': list_word[2]}
                        ingredients_list.append(ingredient)
                        cook_book[name_dictionary] = ingredients_list

        del cook_book['']
        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    ingredients_catalog = {}

    for selected_dish in dishes:
        result = 1
        result_2 = 1
        if selected_dish in cook_book.keys():
            dish_list = cook_book[selected_dish]
            for ingredient_dish in dish_list:
                x = list(ingredient_dish.values())[0]
                # ingredients_catalog[x] = {}
                copy_ingredient_dish = ingredient_dish.copy()
                copy_ingredient_dish.pop('ingredient_name')
                if x not in list(ingredients_catalog.keys()):
                    result = person_count * int(copy_ingredient_dish['quantity'])
                    copy_ingredient_dish['quantity'] = result
                    ingredients_catalog[x] = copy_ingredient_dish
                else:
                    result = person_count * int(copy_ingredient_dish['quantity'])
                    result_2 = list(ingredients_catalog[x].values())[0] + result
                    copy_ingredient_dish['quantity'] = result_2
                    ingredients_catalog[x] = copy_ingredient_dish
                    # print(list(ingredients_catalog[x].values())[0])
                # print(result)
                # print(result_2)
                # print(ingredients_catalog[x])
                # print(ingredi print(ingredients_catalog[x]))ents_catalog[x]))
                # print(x)
                # # print(y)
                # print(result)
                # print(ingredients_catalog)
                # print(ingredient_dish)

            # print(dish_list)
            # print(ingredients_catalog)
    return ingredients_catalog


def input_dishes():
    select_user_dishes = []
    quantity_guest = 0
    while True:
        ff = str(input("Введите название блюда. Если ввод больше не требуется нажмите 0 ")).title()
        if ff in list(cook_book.keys()):
            select_user_dishes.append(ff)
        elif ff == '0':
            break
        elif ff == '':
            print('Некорректный ввод')
        else:
            print('Такого блюда в меню нет')

    while True:
        ff = int(input("Введите количество гостей "))
        if ff != 0:
            if type(ff) == int:
                quantity_guest = ff
                break
            else:
                print('Не корректный ввод ')
        else:
            print('Не корректный ввод ')
    # print(quantity_guest)
    # print(dishes, person_count)
    return select_user_dishes, quantity_guest


# dishes, person_count = input_dishes()

def custom_commands():
    while True:
        user_command = input(str('''Введите одну из команд:
    r - для чтения файла
    w - для ввода названия блюд и количества гостей
    q - выход из программы 
    '''))
        if user_command == 'r':
            print(open_file())
            print('')
        elif user_command == 'w':
            open_file()
            dishes, person_count = input_dishes()
            print(get_shop_list_by_dishes(dishes, person_count))
            print('')
        elif user_command == 'q':
            print('')
            break
        else:
            print('Введена некорректная команда. Повторите запрос.')
            print('')


custom_commands()

# Тут начинается код по 3 заданию

def open_file_zadanie3(file_name):
  with open(file_name, 'r', encoding='utf-8') as file:
    file_name_i = {}
    name = str(file_name)
    data_list = []
    numer_line = 0
    for lol in file:
      numer_line += 1
      data_list.append(lol.strip())
    file_name_i[name] = [numer_line, data_list]
    return name, numer_line, data_list


def dictionary_preparation():
  dict_file = {}

  dict_file[open_file_zadanie3('1.txt')[0]] = [open_file_zadanie3('1.txt')[1], open_file_zadanie3('1.txt')[2]]
  dict_file[open_file_zadanie3('2.txt')[0]] = [open_file_zadanie3('2.txt')[1], open_file_zadanie3('2.txt')[2]]
  dict_file[open_file_zadanie3('3.txt')[0]] = [open_file_zadanie3('3.txt')[1], open_file_zadanie3('3.txt')[2]]

  sorted_values = sorted(dict_file.values())
  sorted_dict = {}
  for i in sorted_values:
      for k in dict_file.keys():
          if dict_file[k] == i:
              sorted_dict[k] = dict_file[k]
              break
  return sorted_dict


def write_file():
  with open('Файл_для_ДЗ', 'w', encoding='utf-8') as file:
    x = dictionary_preparation()
    for element in x:
      file.write(element + '\n')
      file.write(str(x.get(element)[0]) + '\n')
      for element_element in x.get(element)[1]:
        file.write(element_element + '\n')
    return file

write_file()