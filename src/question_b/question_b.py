    """Return the sum of even numbers from 1 to num (inclusive)"""
    total = 0
    for i in range(2, num + 1, 2):  # Start from 2, step by 2 (even numbers)
        total += i
    return total 
