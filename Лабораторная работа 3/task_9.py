salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
def live(sal, sp, mon, inc):
    need = 0
    for i in range(mon):
        need += sp - sal
        sp *= 1 + inc
    return need

need_money = live(salary, spend, months, increase)

print(round(need_money))
