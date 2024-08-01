salary = [2300, 1800.801235, 5000, 1234.585858, 7500.12848]
print(round(sum(salary)/len(salary), 2))
print(round(max(salary), 2))
print(round(min(salary), 2))

names = ['Денис', 'Антон', 'Егор', 'Катя', 'Женя']

zipped = dict(zip(names, salary))
print(zipped['Денис'])
