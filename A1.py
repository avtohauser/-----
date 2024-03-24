import scipy.integrate as spi
import numpy as np
def parabola_arc_length(x):
    return np.sqrt(1 + (2*x)**2)
arc_length_A = spi.quad(parabola_arc_length, 0, 1)[0]
arc_length_A
