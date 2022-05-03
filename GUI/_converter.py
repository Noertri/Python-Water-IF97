def convertT(value, unit):
    if value is not None and unit is not None:
        match unit:
            case "C":
                value += 273.15
                return value
            case "K":
                return value
            case _:
                return None