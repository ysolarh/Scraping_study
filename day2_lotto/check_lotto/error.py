class InputError(Exception):
    def __str__(self):
        return "1회차부터 있음"


def input_exception(st):
    if int(st) <= 0:
        raise InputError()
