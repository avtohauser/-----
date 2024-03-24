from scipy.optimize import fsolve
from scipy.integrate import quad
import numpy as np


def f_x(x):
    return x**2

def g_x(x):
    return 4 * np.cos(x)


def h_x(x):
    return f_x(x) - g_x(x)


initial_guesses = [0, 1.0, 1.5]


intersection_points_numerical = [fsolve(h_x, x0=guess)[0] for guess in initial_guesses]


intersection_points_numerical = sorted(set(intersection_points_numerical))


def integrand(x):
    return abs(h_x(x))


area, _ = quad(integrand, 0, intersection_points_numerical[-1])

total_area = 2 * area

intersection_points_numerical, total_area
