def power_converter(value, from_system, to_system):
    if from_system == 1 and to_system == 2:  # СИ в американскую систему
        return round(value * 0.22480894, 2)
    elif from_system == 1 and to_system == 3:  # СИ в старорусскую систему
        return round(value * 0.006225, 2)
    elif from_system == 2 and to_system == 1:  # Американская система в СИ
        return round(value * 4.44822167659, 2)
    elif from_system == 2 and to_system == 3:  # Американская система в старорусскую систему
        return round(value * 0.02769, 2)
    elif from_system == 3 and to_system == 1:  # Старорусская система в СИ
        return round(value * 160.637699, 2)
    elif from_system == 3 and to_system == 2:  # Старорусская система в американскую систему
        return round(value * 36.11323, 2)
    else:
        return value