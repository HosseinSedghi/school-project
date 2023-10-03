from consets import P

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


def calculate_parall(width, height, h):
    area = width * h
    env = (width + height) * 2
    
    return env, area
