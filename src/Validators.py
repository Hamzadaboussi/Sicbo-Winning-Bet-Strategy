
import pandas as pd

from src.Cases import Types, Cases, Result


def validate_type(number):
    if is_big(number):
        return Types.BIG
    if is_small(number):
        return Types.SMALL
    return Types.TIE


def validate_case(number, number1, number2, number3):
    if is_odd(number) and is_big(number) and not is_triple(number1, number2, number3):
        return Cases.ODD_AND_BIG
    if is_odd(number) and is_small(number) and not is_triple(number1, number2, number3):
        return Cases.ODD_AND_SMALL
    if not is_odd(number) and is_small(number) and not is_triple(number1, number2, number3):
        return Cases.EVEN_AND_SMALL
    if not is_odd(number) and is_big(number) and not is_triple(number1, number2, number3):
        return Cases.EVEN_AND_BIG
    return Cases.TIE


def is_odd(number):
    return number % 2 != 0


def is_small(number):
    return number in range(4, 11)


def is_big(number):
    return number in range(11, 18)


def is_triple(number1, number2, number3):
    return number1 == number2 == number3


def bet(case, type):
    if (case == Cases.ODD_AND_BIG.value or case == Cases.EVEN_AND_BIG.value) and type == Types.BIG.value:
        return Result.WIN
    if (case == Cases.ODD_AND_SMALL.value or case == Cases.EVEN_AND_SMALL.value) and type == Types.SMALL.value:
        return Result.WIN
    return Result.LOST


def bet2(type, p1, p2):
    if (p1 > p2) and type == Types.BIG.value:
        return Result.WIN
    if (p2 > p1) and type == Types.SMALL.value:
        return Result.WIN
    return Result.LOST


def save_data(time, case, bet_price, result, repeated_data, my_profile):
    repeated_data = pd.concat([repeated_data, pd.DataFrame({'time': [time], 'case': [case],

                                                            'betprice': [bet_price],
                                                            'result': [validate_type(result).value],
                                                            'bet': bet(case, validate_type(result).value).value,
                                                            "balance": my_profile.get_balance(),
                                                            "profits": my_profile.get_profit_balance(),

                                                            })], ignore_index=True)
    return repeated_data


def save_data_number(time, case, bet_price, result, bet, repeated_data, my_profile):
    repeated_data = pd.concat([repeated_data, pd.DataFrame({'time': [time], 'DiceF1': [case],

                                                            'betprice': [bet_price],
                                                            'DiceR': [result],
                                                            'bet': [bet],
                                                            "balance": my_profile.get_balance(),
                                                            "profits": my_profile.get_profit_balance(),

                                                            })], ignore_index=True)
    return repeated_data
