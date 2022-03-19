# Задача 1. Склады

small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}

big_storage.update(small_storage)
order = input('Введите название товара: ')

print('Такого товара нет' if big_storage.get(order) is None else big_storage.get(order))
