a = 5
b = 50
if a > b:
    print(a)
else:
    print(b)


a, b = int(input()), int(input())
if abs(a - b) == 135:
    print('yes')
else:
    print('no')


a = input()
if a == '12' or a == '1' or a == '2':
    print('Зима')
elif a == '3' or a == '4' or a == '5':
    print('Весна')
elif a == '6' or a == '7' or a == '8':
    print('Лето')
elif a == '9' or a == '10' or a == '11':
    print('Осень')
else:
    print('введите число от 1 до 12')



a = int(input())
b = int(input())
c = int(input())

if a > 10 and b > 10 and c > 10:
    print("yes")
else:
    print("no")



