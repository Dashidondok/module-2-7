import random

random_number = random.randint(3,21)
print('Случайное число: ', random_number)
def paroli(n):
    paroli = {}
    paroli.update({3: 12,
                    4: 13,
                    5: 1423,
                    6: 121524,
                    7: 162534,
                    8: 13172635,
                    9: 1218273645,
                    10: 141923283746,
                    11: 11029384756,
                    12: 12131511124210394857,
                    13: 112211310495867,
                    14: 1611325212343114105968,
                    15: 1214114232133124115106978,
                    16: 1317115262143531341251161079,
                    17: 11621531441351261171089,
                    18: 12151811724272163631545414513612711810,
                    19: 118217316415514613712811910,
                    20: 13141911923282183731746416515614713812911})
    chislo = paroli.get(n)
    return chislo

n = random_number

num1 = list(range(1, n))
num2 = list(range(1, n))
kodi = []
result = ''

for i in num1:
    for j in num2:
        if i >= j:
            continue
        else:
            kratno = n % (i + j)
            if kratno == 0:
                kodi.append([i, j])
                result = result + str(i) + str(j)
print('Пары чисел: ', *kodi)