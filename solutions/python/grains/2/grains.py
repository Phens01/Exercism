def square(number):
    """Calculate the number of grains on a given square.

    Parameters:
        number (int): The square number (between 1 and 64).

    Returns:
        int: The number of grains on that square.

    Raises:
        ValueError: If number is not between 1 and 64.
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    
    sqr = 2**(number - 1)
    return sqr


def total():
    """Calculate the total number of grains on the chessboard.

    Returns:
        int: The total number of grains.
    """
    all_grains = 0
    for case in range(1, 65):
        all_grains += square(case)
        
    return all_grains