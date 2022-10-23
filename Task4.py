# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = 3
koefs = [7, 1, 12, -5]
# k = int(input('Какая степень многочлена? '))


print(koefs)
result = ''
for i in range(len(koefs)):
    if len(result) > 0 and koefs[i] > 0:
        result = result + ' + '
    if koefs[i] == 0:
        continue
    result = result + str(koefs[i]) + 'x^' + str(k - i)
result = result + ' =0'
print(result)

with open('Task4.txt', 'w') as data:
    data.write(result)

