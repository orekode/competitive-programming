def swap_case(s):
    result = ""
    for letter in s:
        if(letter.isupper()):
            result += letter.lower()
        else:
            result += letter.upper()
    return result
