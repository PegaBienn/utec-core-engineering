#!/usr/bin/env python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    clave_max = max(a_dictionary, key = a_dictionary.get)
    return clave_max


