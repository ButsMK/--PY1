money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

def live(capital, salary, spend, increase):
    count = 0
    while capital >= 0:
        capital = capital + salary - spend
        spend = spend * (1 + increase)
        count += 1
    return count - 1

month = live(money_capital, salary, spend, increase)

print(month)
