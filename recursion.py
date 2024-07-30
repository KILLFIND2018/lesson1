stack = []
#сначала собираем пирамидку
stack.append(1)
print("Insert element:", stack)
stack.append(2)
print("Insert element:", stack)
stack.append(3)
print("Insert element:", stack)
print(stack)
#разбираем
stack.pop()
print("remove element:")
stack.pop()
print("remove element:")
stack.pop()
print("remove element:")
print(stack)