#   Напишите программу для решения следующей задачи.
#   Камера наблюдения регистрирует в автоматическом режиме скорость проезжающих мимо нее автомобилей.
# 1. Необходимо определить среднюю зарегистрированную скорость всех автомобилей.
# 2. Если скорость хотя бы одного автомобиля была не меньше 60 км/ч, выведите «YES», иначе выведите «NO».

'''
number_of_cars = int(input())
sum_v = 0 

for i in range (number_of_cars):
    v = int(input())
    sum_v += v

print(f"Средняя скорость автомобилей: {sum_v/number_of_cars} км/ч")

'''

number_of_cars = int(input())
sum_v = 0 
check = 0

for i in range (number_of_cars):
    v = int(input())
    sum_v += v
    if v <= 60:
        check = 1


print(f"Средняя скорость автомобилей: {sum_v/number_of_cars} км/ч")
if check == 1:
    print("YES")
else:
    print("NO")
