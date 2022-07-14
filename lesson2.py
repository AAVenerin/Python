print('Exercise 1')
my_list = [1, 2.3, True, False, None, 'Text', {1, 3}, (1, 2, 3), range (10), (0 +10j)]
for i, val in enumerate(my_list, 1):
    print(f'{i}) {val} - {type(val)}')
# and so on
print('Exercise 2')
user_list = input('Numbers with space: ').split()
for i in range(1, len(user_list), 2):
    user_list.insert(i - 1, user_list.pop(i))
print(user_list)
print('Exercise 3')
month = int(input('Enter the number of the month: '))
month_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
if month in month_dict:
    if month == 1:
        print("The" " " f'{month}-st month of the year is {month_dict[month]}!')
    if month == 2:
        print("The" " " f'{month}-nd month of the year is {month_dict[month]}!')
    if month == 3:
        print("The" " " f'{month}-d month of the year is {month_dict[month]}!')
    if month >= 4:
        print("The" " " f'{month}-th month of the year is {month_dict[month]}!')
    if month <= 0:
        print("This month does not exist!")
    if month >= 13:
        print("This month does not exist!")
print('Exercise 4')
words_list = input('Write down words with spaces: ').split()
for i, v in enumerate(words_list, 1):
    print(f'{i}) {v:.10}')
print('Exercise 5')
numb_list = [9, 8, 7, 7, 7, 6, 5, 3, 3, 3, 2, 1]
while True:
    new_number = input('Enter a new number:\n')
    if new_number.isdigit():
        numb_list.append(int(new_number))
        numb_list.sort(reverse=True)
        print(numb_list)
    elif new_number == 'q':
        print(numb_list)
        break
