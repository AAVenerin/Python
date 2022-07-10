print('Exercise 1')
a = 'Mother'
b = 'Anarchy'
c = 'Father'
d = 'A glass of port vein'
print(f'{a} - {b}')
print(f'{c} - {d}')
phrase = input('"All happy families are alike; each ')
print('Family is unhappy in its own way". (c) Leo Tolstoi')
num_1 = int(input('Schreiben Sie bitte eine Zahl: '))
num_2 = int(input('Noch einmal bitte: '))
print(f'Die shoene Zahlen {num_1} und {num_2}')
print('Exercise 2')
time = int(input('Write down the time in seconds '))
hours = time // 3600
minutes = time // 60 - hours * 60
seconds = time % 60
print(f'{hours:02}:{minutes:02}:{seconds:02}')
print('Exercise 3')
x = input('Enter an int: ')
print(f'{x} + {x + x} + {x + x + x} = {int(x) + int(x + x) + int (x + x + x)}')
print('Exercise 4')
reference = 0
num = int(input('die Telefonnummer ohne +: '))
while num > 0:
    digit = num % 10
    if digit > reference:
        reference = digit
        if reference == 9:
            break
    num = num // 10
print(f'The biggest number in {num} is {reference}')
print('Exercise 5')
expenses = float(input('Expenses rub: '))
revenue = float(input('Revenue rub: '))
profit = revenue - expenses
if profit > 0:
    print(f'Congratulations! Your profit is {profit:.2f}')
    print(f'Your profit margin is {100 * (profit / revenue):.2f}')
    happiness = int(input('How many happy employees? '))
    print(f'Equal profit distribution: {profit / happiness:.2f}')
elif profit < 0:
    print('Marxism - is your the only way :(')
elif profit == 0:
    print('Zero profit - zero beer and surrogate woman :D')
print('Exercise 6')
while True:
    days = 1
    start_km = float(input('First result: '))
    last_km = float(input('Final result: '))
    if start_km <= 0 or last_km < 0:
        print('Results should be realistic!')
    else:
        while start_km < last_km:
            start_km += start_km * 0.1
            days += 1
        print(f'Days till result {days}')
        break




