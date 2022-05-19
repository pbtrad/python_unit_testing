
def power_num(number: float, power: int) -> float:
    if not isinstance(number, int) and not isinstance(number, float):
        raise TypeError("The number can only be int or float")

    if not isinstance(power, int):
        raise TypeError("the power can only be of int type")

    if number >= 0:
        return round(number ** power, 2)
    raise TypeError("The number can only be >= 0")
