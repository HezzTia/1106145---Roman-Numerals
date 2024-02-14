# emily cabrera - 1106145

import pytest

#definition of conversion function of the program
def convert_to_roman(num):

    roman_numerals = {
        1000 : "M",
        900 : "CM",
        500 : "D",
        400 : "CD",
        100 : "C",
        90 : "XC",
        50 : "L",
        40 : "XL",
        10 : "X",
        9 : "IX",
        5 : "V",
        4 : "IV",
        1 : "I",
    }

    if num < 1 or num > 3999:
        raise ValueError("Input number must be between 1 and 3999")

    roman_num = ""
    
    for value, numeral in roman_numerals.items():
        while num >= value:
            roman_num += numeral
            num -= value
    return roman_num


#normal behavior of the algorithm 

def test_one():
    assert convert_to_roman(1) == "I"

def test_four():
    assert convert_to_roman(4) == "IV"

def test_five(): 
    assert convert_to_roman(5) == "V"

def test_nine():
    assert convert_to_roman(9) == "IX"

def test_ten():
    assert convert_to_roman(10) == "X"

def test_thirty_nine():
    assert convert_to_roman(39) == "XXXIX"

def test_ninety_nine():
    assert convert_to_roman(99) == "XCIX"

def test_hundred():
    assert convert_to_roman(100) == "C"

def test_three_hundred_ninety_nine():
    assert convert_to_roman(399) == "CCCXCIX"


#behavior of the algorithm in case of exceptions
    
def test_input_negative():
    with pytest.raises(ValueError):
        convert_to_roman(-1)

def test_input_out_range():
    with pytest.raises(ValueError):
        convert_to_roman(4000)