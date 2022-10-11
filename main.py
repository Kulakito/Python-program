while True:
  corner1 = int(input("Введите первый угол: "))
  corner2 = int(input("Введите второй угол: "))
  corner3 = int(input("Введите третий угол: "))
  if corner1 + corner2 + corner3 < 180 or corner1 + corner2 + corner3 > 180:
    print("У треугольника сумма углов должна быть 180 градусов")
    continue
  if corner1 == 90 or corner2 == 90 or corner3 == 90:
    print("Прямоугольный треугольник")
    break
  elif corner1 < 90 and corner2 < 90 and corner3 < 90:
    print("Остроугольный треугольник")
    break
  elif corner1 > 90 or corner2 > 90 or corner3 > 90:
    print("Тупоугольный треугольник")

num = input("Введите номер месяца: ")
months = {
    "1": "Январь",
    "2": "Февраль",
    "3": "Март",
    "4": "Апрель",
    "5": "Май",
    "6": "Июнь",
    "7": "Июль",
    "8": "Август",
    "9": "Сентябрь",
    "10": "Октябрь",
    "11": "Ноябрь",
    "12": "Декабрь"
}
print(f"Это {months[num]}")

x = int(input("Введите координату x: "))
y = int(input("Введите координату y: "))
if x == 0 and y == 0:
  print("Точка находится в центре")
elif x == 0:
  print("Точка находится на оси y")
elif y == 0:
  print("Точка находится на оси x")
elif x > 0 and y > 0:
  print("Точка находится в 1 квадранте")
elif x < 0 and y > 0:
  print("Точка находится в 2 квадранте")
elif x < 0 and y < 0:
  print("Точка находится в 3 квадранте")
elif x > 0 and y < 0:
  print("Точка находится в 4 квадранте")

number = int(input("Введите число: "))
if number < 0:
  print("Число отрицательное")
elif number > 0:
  print("Число положительное")
if number < 10 and number > -10:
  print("Число однозначное")
elif number < 100 and number > -100:
  print("Число двухзначное")
elif number < 1000 and number > -1000:
  print("Число трёхзначное")
elif number >= 1000 and number <= -1000:
  print("Число больше трёхзначного")