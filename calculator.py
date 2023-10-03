from consets import P

# Rectangle
def calculat_rectangle(width, height):
    area = width * height
    env = (width + height) * 2

    return env, area


# Circle
def calculat_circle(radius):
    area = round((radius**2)*P, 2)
    env = round((radius*2)*P, 2)

    return env, area