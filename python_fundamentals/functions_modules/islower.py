#!/usr/bin/env python3
def islower(letra):
    if len(letra) != 1 or not (97 <= ord(letra) <= 122):
        return False
    else:
        return True

