# FizzBuzz

n = int(input('Type a number bigger than 0: '))

i = 1
while i <= n:
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)
    i += 1
print()
