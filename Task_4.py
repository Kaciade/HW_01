print("\nПетя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?\n")

cranes = int(input("Введите число S: "))
P = int(cranes/6)
K = int(cranes/1.5)
S = int(cranes/6)

print(f"Если общее количество сделанных журавликов = {S}, то:\nПетя сделал {P}.\nСерёжа сделал {S}.\nА Катя сделала {K}.")