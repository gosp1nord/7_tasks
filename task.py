
def get_recipes(file_name):
    cook_book = {}
    with open(file_name, "r", encoding="utf-8") as file:
        for item in file:
            count_ingred = int(file.readline().strip())
            temp_list = []
            for i in range(count_ingred):
                ingredient_name, quantity, measure = file.readline().split('|')
                temp_list.append(
                    {'Наименование': ingredient_name.strip(), 'Количество': int(quantity.strip()), 'Единица измерения': measure.strip()}
                )
            file.readline()
            cook_book[item.strip()] = temp_list
        return cook_book


def get_shop_list_by_dishes(dishes, file_name, person_count):
    cook_book = get_recipes(file_name)
    ingredients = {}
    for item in dishes:
        if item in cook_book:
            for i in cook_book[item]:
                if i['Наименование'] in ingredients:
                    ingredients[i['Наименование']]['Количество'] = ingredients[i['Наименование']]['Количество'] + i['Количество']*person_count
                else:
                    ingredients[i['Наименование']] = {'Единица измерения': i['Единица измерения'], 'Количество': i['Количество']*person_count}
        else:
            print(f"Блюда '{item}' нет в книге рецептов")
    return ingredients


def sorting_files(list_files):
    list_names = []
    for item in list_files:
        i = 0
        with open(item, 'r', encoding="utf-8") as file:
            for line in file:
                i += 1
        list_names.append([item, i])

    list_names.sort(key=lambda z: z[1])

    with open('result.txt', 'w', encoding="utf-8") as file_write:
        for item in list_names:
            with open(item[0], 'r', encoding="utf-8") as file_read:
                file_write.write(f'{item[0]}\n')
                file_write.write(f'{item[1]}\n')
                for i in file_read:
                    file_write.write(i)
                file_write.write('\n')


# print(get_recipes("recipes.txt"))

# dishes = ['Утка по-пекински', 'Запеченный картофель']
# print(get_shop_list_by_dishes(dishes, "recipes.txt", 2))

# list_files = ['1.txt', '2.txt', '3.txt', '4.txt']
# sorting_files(list_files)


