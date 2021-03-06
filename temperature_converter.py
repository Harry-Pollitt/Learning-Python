# This is a simple temperature conversion tool
# Created using what I learnt about functions
import sys

if len(sys.argv) == 1:  # no arguments, so print help message
    print('''
    This is a simple temperature converter that can convert between Kelvin, Celsius and Fahrenheit.

    temperature_converter(unit_1, unit_2, temp)

    Program first converts input temperature to Kelvin
    Then converts to second unit from Kelvin

    Example
    -------
    >> temperature_converter(F, C, 67)
    19.444444444444457
    ''')
    exit()

unit1 = str(sys.argv[1])
unit2 = str(sys.argv[2])
temperature = float(sys.argv[3])


def temperature_converter(unit_1, unit_2, input_temp):
    if unit_1 == 'F':
        kelvin = fahr_to_kelvin(input_temp)
    if unit_1 == 'C':
        kelvin = celsius_to_kelvin(input_temp)
    if unit_1 == 'K':
        kelvin = input_temp
    if unit_2 == 'K':
        return kelvin
    if unit_2 == 'C':
        return kelvin_to_celsius(kelvin)
    if unit_2 == 'F':
        return kelvin_to_fahr(kelvin)


def celsius_to_kelvin(temp_c):
    return temp_c + 273.15


def fahr_to_kelvin(temp_f):
    return (temp_f - 32) * (5 / 9) + 273.15


def kelvin_to_celsius(temp_k):
    return temp_k - 273.15


def kelvin_to_fahr(temp_k):
    return (temp_k - 273.15) * 9 / 5 + 32


print(temperature_converter(unit1, unit2, temperature))
