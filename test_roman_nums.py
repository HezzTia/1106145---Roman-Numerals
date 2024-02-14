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

def test_one():
    assert convert_to_roman(1) == "I"