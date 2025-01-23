#Ввод пергого числа
print('Введите число.')
inp2 = float(input('>'))
print(inp2)
#--------------------

#Ввод операций и его проверка на правильность а иначе, ввод второго числа
print('Операции: +, -, *, /, %')
inp = input('>')
if inp != '+' and inp != '-' and inp != '*' and inp != '/':
    print('Ошибка: Ввод не содержит символов показанных выше. ПЖ повторите попытку :(')
else:
    print(inp2, inp)
    print('Введите число.')
    inp3 = float(input('>'))
    print(inp2, inp, inp3)
#--------------------

#Функции операций
def plus(inp2, inp3):
    sum_ = inp2 + inp3
    print('=', sum_)
    return sum_

def minus(inp2, inp3):
    sum_ = inp2 - inp3
    print('=', sum_)
    return sum_

def multiply(inp2, inp3):
    sum_ = inp2 * inp3
    print('=', sum_)
    return sum_

def devide(inp2, inp3):
    sum_ = inp2 / inp3
    print('=', sum_)
    return sum_
    
def remainder(inp2, inp3):
    sum_ = inp2 % inp3
    print('=', sum_)
    return sum_
#--------------------

#Условия операций
if inp == '+':
    plus(inp2, inp3)

if inp == '-':
    minus(inp2, inp3)

if inp == '*':
    multiply(inp2, inp3)

if inp == '/':
    devide(inp2, inp3)
    
if inp == '%'
    remainder(inp2, inp3)
#--------------------
