numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for i in numbers:
    # нe простое, ни составное и не вносим в списки
    if i == 1:
        continue
    is_prime = True
    # проверяем  что выбранное число не делиться ни начто
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    # если делиться пишем в  список простых, нет в непростые числа
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

print('Primes:', primes)
print('Not Primes:', not_primes)