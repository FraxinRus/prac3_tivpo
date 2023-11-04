def area_converter(value, from_system, to_system):
    if from_system == 0 and to_system == 1:  # Квадратный километр в гектар
        return value * 100
    elif from_system == 0 and to_system == 2:  # Квадратный километр в декар
        return value * 1000
    elif from_system == 1 and to_system == 0:  # Гектар в квадратные километры
        return value / 100
    elif from_system == 1 and to_system == 2:  # Гектар в декар
        return value * 10
    elif from_system == 2 and to_system == 0:  # Декар в квадратные километры
        return value / 1000
    elif from_system == 2 and to_system == 1:  # Декар в гектар
        return value / 10
    else:
        return value