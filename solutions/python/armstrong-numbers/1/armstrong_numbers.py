def is_armstrong_number(number):
    """Determine if a number is an Armstrong number.

    Parameters:
        number (int): The number to check.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    value = 0
    armstrong_number = False
    digits = str(number)
    num_digits = len(digits)
    
    for n in digits:
        value += int(n) ** num_digits
    
    if number == value:
        armstrong_number = True

    return armstrong_number