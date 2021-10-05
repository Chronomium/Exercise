oper = eval(input('Enter the number of the operator (1. Addition 2. Subtraction '
             '3. Multiplication 4. Division : '))

num1 = eval(input('Enter the first number: '))
num2 = eval(input('Enter the second number: '))

if oper == 1:
    print(f'{num1} + {num2} is',num1 + num2)
elif oper == 2:
    print(f'{num1} - {num2} is', num1 - num2)
elif oper == 3:
    print(f'{num1} * {num2} is', num1 * num2)
elif oper == 4:
    print(f'{num1} / {num2} is', num1 / num2)