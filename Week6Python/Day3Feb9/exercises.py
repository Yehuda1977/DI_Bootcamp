list1 = [5, 10, 15, 20, 25, 50, 20]

for i in range(len(list1)):
    if list1[i] == 20:
        list1[i] = 200
        break

print(list1)

list1[list1.index(20)] = 200

print(list1)


aTuple = (10, 20, 30, 40)

a, b, c, d = aTuple

print(a, b, c, d)


for i in range(1,11):
    print(i)
