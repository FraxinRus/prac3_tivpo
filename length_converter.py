#Исправлена ошибка с плавающей запятой - добавлены round()

# 0 - СИ
# 1 - Американская система
# 2 - Старорусская система
def length_converter(value, from_system, to_system):
    if from_system == 0 and to_system == 1:  # СИ в американскую систему
        return round(round(value, 2) * 0.39, 2)
    elif from_system == 0 and to_system == 2:  # СИ в старорусскую систему
        return round(round(value, 2) * 0.82, 2)
    elif from_system == 1 and to_system == 0:  # Американская система в СИ
        return round(round(value, 2) * 2.54, 2)
    elif from_system == 1 and to_system == 2:  # Американская система в старорусскую систему
        return round(round(value, 2) * 2.11, 2)
    elif from_system == 2 and to_system == 0:  # Старорусская система в СИ
        return round(round(value, 2) * 1.22, 2)
    elif from_system == 2 and to_system == 1:  # Старорусская система в американскую систему
        return round(round(value, 2) * 0.47, 2)
    else:
        return round(round(value, 2), 2)  # Если системы совпадают или ключи некорректны, возвращаем исходное значение
