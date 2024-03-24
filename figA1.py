import sympy as sp

# Определяем символ
x = sp.symbols('x')

# Уравнение параболы
y = x**2

# Вычисляем площадь под кривой от 0 до 1
area = sp.integrate(y, (x, 0, 1))
area.evalf()
