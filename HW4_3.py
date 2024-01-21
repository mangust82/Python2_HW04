# 3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

import decimal

decimal.getcontext().prec = 2
MULTIPLICITY = 50
PERCENT = decimal.Decimal(15) / decimal.Decimal(1000)
PERCENT_BONUS = decimal.Decimal(3) / decimal.Decimal(100)
COUNT_PERC = 3
MIN_LIMIT = decimal.Decimal(30)
MAX_LIMIT = decimal.Decimal(600)
PERCENT_RICHNESS = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_AMOUNT = 5_000_000
CMD_DEPOSIT = "1"
CMD_WITHDRAW = "2"
CMD_EXIT = "3"

def greetings() -> int:
    """Menu of greetings"""
    action = input(
        f"пополнить-{CMD_DEPOSIT}\n"
        f"снять-{CMD_WITHDRAW}\n"
        f"выход-{CMD_EXIT}\n"
        f"Введите действие: "
    )
    return action


def chek_multiplicity(amount: float) -> float:
    while amount % MULTIPLICITY != 0:
        amount = int(input(f"Введите сумму кратную {MULTIPLICITY}: "))
    return amount


def deposit(operations: int, balance: float, amount: float) -> (int, float):
    operations += 1
    balance += amount
    return operations, balance


def percent_rich(balance:float) -> (float, float):
    sum_percent = balance * PERCENT_RICHNESS
    balance -= sum_percent
    print(f"Вычтен налог на богатство в размере {sum_percent}")
    print(f"Текущий баланс {balance}")
    return balance, sum_percent


def comisiion(amount:float, balance:float, operations:int) -> (float, int, float):
    comission = amount * PERCENT
    if comission < MIN_LIMIT:
        comission = MIN_LIMIT
    elif comission > MAX_LIMIT:
        comission = MAX_LIMIT
    if comission + amount > balance:
        print("На балансе недостаточно средств")
        comission = 0
        return balance, operations, comission
    else:
        operations += 1
        balance -= (amount + comission)
        print(f"Сумма снятия {amount}, комиссия {comission}, общая сумма {amount + comission}")
        return balance, operations, comission


def bonus(balance: float) -> (float, float):
    bonus_sum = balance * PERCENT_BONUS
    balance += bonus_sum
    print(f"Сумма бонуса {bonus_sum}")
    return balance, bonus_sum


balance = 0
operations = 0
list_oper = []

while True:
    action = greetings()
    if balance > RICHNESS_AMOUNT and action != "3":
        balance, sum_percent = percent_rich(balance * (-1))
        list_oper.append(sum_percent)
    if action == "1" or action == "2":
        amount = 1
        amount = chek_multiplicity(amount)
        if action == "1":
            operations, balance = deposit(operations, balance, amount)
            list_oper.append(amount)
        else:
            balance, operations, comission = comisiion(amount, balance, operations)
            if comission ==0:
                pass
            else:
                list_oper.append(amount* (-1))
                list_oper.append(comission * (-1))
        if operations % COUNT_PERC == 0:
            balance, bonus = bonus(balance)
            list_oper.append(bonus)
        print(f"Текущий баланс {balance}")
    elif action == "3":
        break
    else:
        print("Введена неверная команда")
    print(f'История операций: {list_oper}')




# while True:
#     action = input(
#         f"пополнить-{CMD_DEPOSIT}\n"
#         f"снять-{CMD_WITHDRAW}\n"
#         f"выход-{CMD_EXIT}\n"
#         f"Введите действие: "
#     )
#     if balance > RICHNESS_AMOUNT and action != "3":
#         sum_percent = balance * PERCENT_RICHNESS
#         balance -= sum_percent
#         print(f"Вычтен налог на богатство в размере {sum_percent}")
#         print(f"Текущий баланс {balance}")
#     if action == "1" or action == "2":
#         amount = 1
#         while amount % MULTIPLICITY != 0:
#             amount = int(input(f"Введите сумму кратную {MULTIPLICITY}: "))
#         if action == "1":
#             operations += 1
#             balance += amount
#         else:
#             comission = amount * PERCENT
#             if comission < MIN_LIMIT:
#                 comission = MIN_LIMIT
#             elif comission > MAX_LIMIT:
#                 comission = MAX_LIMIT
#             if comission + amount > balance:
#                 print("На балансе недостаточно средств")
#             else:
#                 operations += 1
#                 balance -= (amount + comission)
#             print(f"Сумма снятия {amount}, комиссия {comission}, общая сумма {amount + comission}")
#     # print(f"Текущий баланс {balance}")
#         if operations % COUNT_PERC == 0:
#             bonus_sum = balance * PERCENT_BONUS
#             balance += bonus_sum
#             print(f"Сумма бонуса {bonus_sum}")
#         print(f"Текущий баланс {balance}")
#     elif action == "3":
#         break
#     else:
#         print("Введена неверная команда")