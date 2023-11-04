# 0 - км/ч
# 1 - м/c
# 2 - миль/ч

# Функция для конвертации скорости
def speed_converter(value, from_system, to_system):
    if from_system == 0 and to_system == 1:  # км/ч в м/с
        return round(value * 1000 / 3600, 2)
    elif from_system == 0 and to_system == 2:  # км/ч в миль/ч
        return round(value * 0.621371, 2)
    elif from_system == 1 and to_system == 0:  # м/с в км/ч
        return round(value * 3600 / 1000, 2)
    elif from_system == 1 and to_system == 2:  # м/с в миль/ч
        return round(value * 2.23694, 2)
    elif from_system == 2 and to_system == 0:  # миль/ч в км/ч
        return round(value * 1.60934, 2)
    elif from_system == 2 and to_system == 1:  # миль/ч в м/с
        return round(value * 0.44704, 2)
    else:
        return round(value, 2)
