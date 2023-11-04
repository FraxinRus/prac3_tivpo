#0 - СИ
#1 - Американская система
#2 - Старорусская система

def length_converter(value, from_system, to_system):
    if from_system == 0 and to_system == 1:  # СИ в американскую систему
        return value * 0.39
    elif from_system == 0 and to_system == 2:  # СИ в старорусскую систему
        return value * 0.82
    elif from_system == 1 and to_system == 0:  # Американская система в СИ
        return value * 2.54
    elif from_system == 1 and to_system == 2:  # Американская система в старорусскую систему
        return value * 2.11
    elif from_system == 2 and to_system == 0:  # Старорусская система в СИ
        return value * 1.22
    elif from_system == 2 and to_system == 1:  # Старорусская система в американскую систему
        return value * 0.47
    else:
        return value  # Если системы совпадают или ключи некорректны, возвращаем исходное значение