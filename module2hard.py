def generator_password(n):
    result = ""
    for i in range(1, n):
        #Сумма пары
        for j in range(i+1, n):
            #деление на остаток
            if (i + j) % n == 0:
                result += str(i) + str(j)
    return result

random_number = 0
while random_number < 3 or random_number > 20:
    random_number = int(input("Введите число для пароля от 3 до 20: "))

password_maker = generator_password(random_number)
print(f"Пароль для введенного числа {random_number}: {password_maker}")
print("Поздравляю,вы сбежали")