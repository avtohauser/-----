# Уровень C.
# Функция для вычисления периметра эллипса с помощью численной интеграции
def ellipse_perimeter_numerical(a, b):
    def integrand(theta):
        return np.sqrt(a**2 * np.sin(theta)**2 + b**2 * np.cos(theta)**2)
    # Вычисляем периметр с помощью численного интегрирования
    return 4 * spi.quad(integrand, 0, np.pi / 2)[0]

# Функция для вычисления периметра эллипса по формуле Рамануджана
def ellipse_perimeter_ramanujan(a, b):
    h = ((a - b)**2) / ((a + b)**2)
    # Приближенная формула Рамануджана для вычисления периметра эллипса
    return np.pi * (a + b) * (1 + 3*h / (10 + np.sqrt(4 - 3*h)))

# Заданные значения a и b
a = 2
b = 3

# Вычисление периметров
perimeter_numerical = ellipse_perimeter_numerical(a, b)
perimeter_ramanujan = ellipse_perimeter_ramanujan(a, b)

# Сравнение периметров и вычисление относительной ошибки
error = abs(perimeter_numerical - perimeter_ramanujan) / perimeter_numerical * 100

perimeter_numerical, perimeter_ramanujan, error
