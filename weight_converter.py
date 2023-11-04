def weight_converter(value, from_system, to_system):
    if from_system == 0 and to_system == 1:  # СИ в американскую систему
        return value * 2.2
    elif from_system == 0 and to_system == 2:  # СИ в старорусскую систему
        return value * 2.44
    elif from_system == 1 and to_system == 0:  # Американская система в СИ
        return value * 0.45
    elif from_system == 1 and to_system == 2:  # Американская система в старорусскую систему
        return value * 1.1
    elif from_system == 2 and to_system == 0:  # Старорусская система в СИ
        return value * 0.41
    elif from_system == 2 and to_system == 1:  # Старорусская система в американскую систему
        return value * 0.9
