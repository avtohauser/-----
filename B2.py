from scipy.constants import g

# Функция для расчета длины траектории полета мяча (шарика)
def calculate_trajectory_length(v0, angle_deg):
    # Перевод угла из градусов в радианы
    angle_rad = np.radians(angle_deg)
    # Вычисление времени полета
    time_of_flight = 2 * v0 * np.sin(angle_rad) / g
    # Вычисление длины траектории
    trajectory_length = v0 * np.cos(angle_rad) * time_of_flight
    return trajectory_length

# Предположим, что начальная скорость v0 равна 1 м/с для примера.
v0 = 1  # начальная скорость в м/с

# Вычисление длин траекторий для углов 35.5 и 65.8 градусов.
trajectory_length_35 = calculate_trajectory_length(v0, 35.5)
trajectory_length_65 = calculate_trajectory_length(v0, 65.8)

trajectory_length_35, trajectory_length_65
