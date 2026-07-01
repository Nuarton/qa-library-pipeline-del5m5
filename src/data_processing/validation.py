"""
Data validation functions.
"""


# Example function to implement:
def validate_isbn(isbn):
    isbnStringClean = str(isbn).strip().replace("-", "").replace(" ","")

    if len(isbnStringClean) != 13:
        return False
    
    if not isbnStringClean.isdigit():
        return False

    # data_digits = isbnStringClean[:12]
    # checkDigit = isbnStringClean[12]

    # try:
    #     total = sum(
    #         int(digit) * (1 if i % 2 == 0 else 3)
    #         for i, digit in enumerate (data_digits)
    #         )
    #     testCheckDigit = (10 - (total % 10)) % 10

        
    #     elif checkDigit != testCheckDigit:
    #         return False

    #     return True
    # except Exception as e:
    #     print(e)
    return True
    
