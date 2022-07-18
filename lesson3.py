# ----------------------------------------1-----------------------------------
def division(n_1, n_2):
    try:
        n_1 = int(n_1)
        n_2 = int(n_2)
        result = n_1 / n_2
    except ValueError:
        return 'Enter the correct data'
    except ZeroDivisionError:
        return 'Zero division is forbidden'
    return round(result, 2)
print(division(input('Enter the first number: '), input('Enter the second number: ')))
# ----------------------------------------2-----------------------------------
def info(**kwargs):
    return ' '.join(kwargs.values())
print(info(name=input('Enter your name: '), age=input('Enter your age: '),
           country=input('Enter your country: '), university=input('Enter your university: ')))
# ----------------------------------------3-----------------------------------
def numbers(n_1, n_2, n_3):
    try:
        num_list = list(map(float, [n_1, n_2, n_3]))
        num_list.remove(min(num_list))
        return sum(num_list)
    except (TypeError, ValueError):
        return 'Enter the correct data!'
print(numbers(input('Enter the first number: '),
              input('Enter the second number: '),
              input('Enter the third number: ')))
# ----------------------------------------4-----------------------------------
def pow(n_1, n_2):
    try:
        result = n_1 ** n_2
        return result
    except (TypeError, ValueError):
        return 'Something goes wrong'
print(pow(float(input('Enter the first number: ')),
        float(input('Enter the second negative number: '))))
# ----------------------------------------5-----------------------------------
def num_sum():
    s = 0
    while True:
        error = False
        in_list = input('Enter numbers, use q to quit: ').split()
        for num in in_list:
            if num == 'q':
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    error = True
        if error:
            print('The data was incorrect!')
        print(f'The sum of numbers = {s}')
print(num_sum())
# ----------------------------------------6-----------------------------------
def my_func():
    for word in input('Enter some words with spaces: ').split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
        print(word.title() if chars == len(word) else f'{word} - use only small letters!')
my_func()