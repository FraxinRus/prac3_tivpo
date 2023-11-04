# 1 - СИ литры
# 2 - АС галлоны
# 3 - Старорусская штофы

def volume_converter(value, from_m_system, to_m_system):
    if from_m_system == 1 and to_m_system == 2:
        return round(round(value, 2) * 0.26417205, 2)
    elif from_m_system == 1 and to_m_system == 3:
        return round(round(value, 2) * 0.81307423368, 2)
    elif from_m_system == 2 and to_m_system == 1:
        return round(round(value, 2) * 3.78541181779, 2)
    elif from_m_system == 2 and to_m_system == 3:
        return round(round(value, 2) * 3.0778208129, 2)
    elif from_m_system == 3 and to_m_system == 1:
        return round(round(value, 2) * 1.2299, 2)
    elif from_m_system == 3 and to_m_system == 2:
        return round(round(value, 2) * 0.3249052043, 2)
    else:
        return round(round(value, 2), 2)  # Если системы совпадают или ключи некорректны, возвращаем исходное значение
