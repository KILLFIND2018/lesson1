number = int(input("Введите число: "))

# При and это строгий оператор, or проверять толлько одно из условий
if number % 3 == 0 and number % 5 == 0 :
    print('FuzzBuzz')
# Если делиться на три, то вывод такой
elif number % 3 == 0:
    print('Fizz')

# Если делиться на пять, то вывод такой
elif number % 5 == 0:
    print('Buzz')
# и если все из условий не выполняются, то сделай это
else:
    print("None")


