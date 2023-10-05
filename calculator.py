from consets import P
from math import sqrt

# Rectangle
def calculate_rectangle(width, height):
    area = width * height
    env = (width + height) * 2

    return env, area


# Circle
def calculate_circle(radius):
    area = round((radius**2)*P, 2)
    env = round((radius*2)*P, 2)

    return env, area


#Parall
def calculate_parall(width, height, h):
    area = width * h
    env = (width + height) * 2
    
    return env, area


#Diamond
def calculate_diamond(small_d, big_d):
    side = round(sqrt(((small_d/2)**2) + ((big_d/2)**2)), 2)

    area = (small_d * big_d) // 2
    env = round(side * 4)

    return env, area