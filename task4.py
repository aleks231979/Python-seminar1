# Домашняя задача 4: Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y)

quater = int(input('Введите номер четверти от 1 до 4: '))
if quater == 1:
    print('Диапазон: х > 0 и y > 0')
elif quater == 2:
    print('Диапазон: х < 0 и y > 0')
elif quater == 3:
    print('Диапазон: х < 0 и y < 0')
elif quater == 4:
    print('Диапазон: х > 0 и y < 0')
else:
    print('Существует только 4 координатные четверти')