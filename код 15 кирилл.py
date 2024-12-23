import math

# Данные задачи
l = 24.000  # значение l в метрах
delta_l = 0.002  # погрешность l в метрах
f_degrees = 5 + 42 / 60  # угол f в градусах
delta_f_seconds = 30  # погрешность f в секундах

# Перевод угла f в радианы
f_radians = math.radians(f_degrees)

# Перевод погрешности f в радианы
delta_f_radians = math.radians(delta_f_seconds / 3600)

# Вычисление cot(f/2) и csc^2(f/2)
f_half = f_radians / 2
cot_f_half = 1 / math.tan(f_half)
csc2_f_half = 1 / (math.sin(f_half) ** 2)

# Относительная погрешность
relative_error_l = delta_l / l
relative_error_f = (delta_f_radians / f_radians) * (0.5 * csc2_f_half)

# Суммарная относительная погрешность
total_relative_error = relative_error_l + relative_error_f

# Знаменатель относительной ошибки
denominator = 1 / total_relative_error

# Вывод результатов
print(f"Относительная погрешность: {total_relative_error:.6f}")
print(f"Знаменатель относительной ошибки: {denominator:.3f}")