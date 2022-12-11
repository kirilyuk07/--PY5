from random import randint

start = -10
stop = 10
count = 15

def get_unique_list_numbers() -> list[int]:
    return set([randint(start, stop) for i in range(count)])

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
# пустая строка