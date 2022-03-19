# Задача 2. Кризис фруктов

incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

min_cost = min(incomes.values())
copy_incomes = incomes.copy()

for item in copy_incomes.keys():
    if incomes[item] == min_cost:
        min_cost_item = item
        incomes.pop(item)

print('Общий доход за год составил {0} рублей.'.format(sum(incomes.values())))
print('Самый маленький доход у {0}. Он составляет {1} рублей.'.format(min_cost_item, min_cost))
print('Итоговый словарь:', incomes)
