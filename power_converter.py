def power_converter(value, from_system, to_system):
    if from_system == 1 and to_system == 2:  # СИ в американскую систему
        return value * 0.22480894
    elif from_system == 1 and to_system == 3:  # СИ в старорусскую систему
        return value * 0.006225
    elif from_system == 2 and to_system == 1:  # Американская система в СИ
        return value * 4.44822167659
    elif from_system == 2 and to_system == 3:  # Американская система в старорусскую систему
        return value * 0.02769
    elif from_system == 3 and to_system == 1:  # Старорусская система в СИ
        return value * 160.637699
    elif from_system == 3 and to_system == 2:  # Старорусская система в американскую систему
        return value * 36.11323