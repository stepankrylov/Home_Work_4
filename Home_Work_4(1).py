from sys import argv

script_name, hours, bid, bonus = argv

print("Имя скрипта: ", script_name)
print("Выработка в часах: ", hours)
print("Ставка в час: ", bid)
print("Премия: ", bonus)
wages = int(hours) * int(bid) + int(bonus)
print("Заработная плата сотрудника: ", wages)
