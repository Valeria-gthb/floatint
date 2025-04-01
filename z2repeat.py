num = int(input("Введите пятизначное число: "))

t = (num // 10) % 10 #десятки
u = num % 10 #единицы
h = (num // 100) % 10 #сотни
tt = (num // 10000) #десятки тысяч
th = (num // 1000) % 10 #тысячи

if tt - th == 0:
    print("Ошибка: деление на ноль!")
else:
    result = (t ** u) * h / (tt - th)
    print(result)