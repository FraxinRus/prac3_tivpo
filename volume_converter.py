# 1 - СИ литры
# 2 - АС галлоны
# 3 - Старорусская штофы

def volume_converter(value, from_m_system, to_m_system):
    if from_m_system == 1 and to_m_system == 2:
        return value * 0.26417205
    elif from_m_system == 1 and to_m_system == 3:
        return value * 0.81307423368
    elif from_m_system == 2 and to_m_system == 1:
        return value * 3.78541181779
    elif from_m_system == 2 and to_m_system == 3:
        return value * 3.0778208129
    elif from_m_system == 3 and to_m_system == 1:
        return value * 1.2299
    elif from_m_system == 3 and to_m_system == 2:
        return value * 0.3249052043
    else:
        return value  # Если системы совпадают или ключи некорректны, возвращаем исходное значение
