from random import randint

random_list = [randint(1, 99) for i in range(10)]
random_list_2 = [randint(1, 99) for i in range(10)]
print(random_list)


def multiplication(list_1):
    multiplication_of_list = 1
    for i in list_1:
        multiplication_of_list *= i
    return multiplication_of_list


print("Произведение списка ", multiplication(random_list))


def min_of_list(list_2):
    minimum_of_list = list_2[0]
    for i in list_2:
        if i < minimum_of_list:
            minimum_of_list = i
    return minimum_of_list
    # v2 - min(list2)


print("Минимум списка ", min_of_list(random_list))


def simple_digits(list_3):
    list_of_simple_digits = []
    for i in list_3:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            list_of_simple_digits.append(i)
    return list_of_simple_digits


print("Список простых чисел - ", simple_digits(random_list))



def find_and_delete_num(list_4):
    number_to_del = int(input("Какое число хотите удалить из списка "))
    counter = 0
    for i in list_4:
        if number_to_del == i:
            counter += 1
            list_4.remove(i)
    return counter

print("число найденных и удаленных чисел ", find_and_delete_num(random_list))



def combine_lists(list_1, list_2):
    list_3 = list_1 + list_2
    return list_3


print("Второй список - ", random_list_2)
print("Объедененные списки ", combine_lists(random_list, random_list_2))


