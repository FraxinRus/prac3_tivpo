# 0 - км/ч
# 1 - м/c
# 2 - миль/ч

# Функция для конвертации скорости
def speed_converter(value, from_system, to_system):
    if from_system == 0 and to_system == 1:  # км/ч в м/с
        return value * 1000 / 3600
    elif from_system == 0 and to_system == 2:  # км/ч в миль/ч
        return value * 0.621371
    elif from_system == 1 and to_system == 0:  # м/с в км/ч
        return value * 3600 / 1000
    elif from_system == 1 and to_system == 2:  # м/с в миль/ч
        return value * 2.23694
    elif from_system == 2 and to_system == 0:  # миль/ч в км/ч
        return value * 1.60934
    elif from_system == 2 and to_system == 1:  # миль/ч в м/с
        return value * 0.44704
    else:
        return value