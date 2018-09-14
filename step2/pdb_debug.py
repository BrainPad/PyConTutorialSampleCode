# -*- coding: utf-8 -*-


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        import pdb; pdb.set_trace()
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)

for num in range(1, 21):
    print(fizzbuzz(num))
