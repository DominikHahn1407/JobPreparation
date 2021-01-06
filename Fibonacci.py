# 0 1 1 2 3 5 8 13 21 34 55 89

user_input = int(input("How many values do you want to have?"))


def fib(n):
    number_1 = 0
    number_2 = 1
    if n < 0:
        print('Not a valid number please try again')
    elif n == 1:
        print(number_1)
    else:
        print(number_1)
        print(number_2)
        for i in range(2, n):
            result = number_1 + number_2
            number_1 = number_2
            number_2 = result
            print(result)


fib(user_input)
