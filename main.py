#. Дано натуральное число. Определить: а ) наименьшее из нихб) наибольшие из них.

num = int(input('Введите число a\n'))
if num > 99 and num < 1000:
  num1 = num // 100
  num2 = num % 100 // 10
  num3 = num % 10
  if num1 > num2 and num1 > num3:
      print(num1)
  elif num2 > num1 and num2 > num3:
      print(num2)
  elif num3 > num1 and num3 > num2:
      print(num3)
  else:
      print('=')
else:
  print("error")

num = int(input('Введите число a\n'))
if num > 99 and num < 1000:
  num1 = num // 100
  num2 = num % 100 // 10
  num3 = num % 10
  if num1 < num2 and num1 < num3:
      print(num1)
  elif num2 < num1 and num2 < num3:
      print(num2)
  elif num3 < num2 and num3 < num1:
      print(num3)
  else:
      print("=")
else:
  print('error')
num = int(input('Введите первое число\n'))
num1 = int(input('Введите первое число\n'))
if num >= 0 and num1 >= 0:
    if num > num1:
        num3 = num // 2
        print(num3)
    else:
        print("-")
else:
    print('error')
num = int(input('Введите первое число\n'))
num1 = int(input('Введите первое число\n'))
num2 = int(input('Введите первое число\n'))
if num > 0 and num1 > 0 and num2 > 0:
     if num % 2 == 0 and num1 % 2 == 0 and num2 % 2 == 0:
         print(num,num1,num2)
     elif num % 2 == 0 and num1 % 2 == 0:
         print(num,num1)
     elif num1 % 2 == 0 and num2 % 2 == 0:
         print(num1,num2)
     elif num % 2 == 0 and num2 % 2 == 0:
         print(num,num2)
     elif num % 2 == 0:
         print(num)
     elif num1 % 2 == 0:
         print(num1)
     elif num2 % 2 == 0:
         print(num2)
     else:
         print('-')

else:
    print('error')
num = int(input('Введите число\n'))
num1 = int(input('Введите число\n'))
num2 = int(input('Введите число\n'))
num3 = int(input('Введите число\n'))
if num > 0 and num1 > 0 and num2 > 0 and num3 > 0:
    if num > 5 and num1 > 5 and num2 > 5 and num3 > 5:
        res = num + num1 + num2 + num3
        print(res)
    elif num > 5 and num1 > 5 and num2 > 5:
        res1 = num + num1 + num2
        print(res1)
    elif num > 5 and num1 > 5:
        res2 = num + num1
        print(res2)
    elif num1 > 5 and num2 > 5 and num3 > 5:
        res3 = num1 + num2 + num3
        print(res3)
    elif num2 > 5 and num3 > 5:
        res4 = num2 + num3
        print(res4)
    elif num > 5 and num3 > 5:
        res5 = num + num3
        print(res5)
    elif num1 > 5 and num3:
        res6 = num1 + num3
        print(res6)
    else:
        print('-')
else:
    print('error')

