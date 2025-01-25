import math

def suma(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])

def resta(c1, c2):
    return (c1[0] - c2[0], c1[1] - c2[1])

def producto(c1, c2):
    real = c1[0] * c2[0] - c1[1] * c2[1]
    imaginaria = c1[0] * c2[1] + c1[1] * c2[0]
    return (real, imaginaria)

def division(c1, c2):
    if c2 == (0, 0):
        raise ValueError("No se puede dividir entre cero")
    divisor = c2[0]**2 + c2[1]**2
    real = (c1[0] * c2[0] + c1[1] * c2[1]) / divisor
    imaginaria = (c1[1] * c2[0] - c1[0] * c2[1]) / divisor
    return (round(real, 2), round(imaginaria, 2))

def modulo(c):
    return math.sqrt(c[0]**2 + c[1]**2)

def conjugado(c):
    return (c[0], -c[1])

def polar_a_cartesiano(polar):
    r, theta = polar
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (round(x, 4), round(y, 4))

def cartesiano_a_polar(cartesiano):
    x, y = cartesiano
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return (round(r, 4), round(theta, 4))

def fase(c):
    return round(math.atan2(c[1], c[0]), 4)
