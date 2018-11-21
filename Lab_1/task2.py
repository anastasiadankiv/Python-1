import sys

def zero(a, b):
    if a < 0 or b < 0:
        raise Exception("numbers < 0")
    if a % b == 0:
        return True
    else:
        return False
