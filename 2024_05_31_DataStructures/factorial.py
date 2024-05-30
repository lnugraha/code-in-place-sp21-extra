# Use the command below to perform doctest
# python3 -m doctest factorial.py -v

def factorial_iteration(n):
    """
    >>> factorial_iteration(3)
    6
    >>> factorial_iteration(0)
    1
    >>> factorial_iteration(1)
    1
    """
    if type(n) is str:
        raise TypeError("Cannot have string factorial")
    
    if type(n) not in [int]:
        raise TypeError("Cannot have non-integer factorial")

    if n < 0:
        raise ValueError("Cannot have negative factorial")

    result = 1;
    for i in range(n, 1, -1):
        result = i*result

    return result

def factorial_dynamic_programming(n):
    if type(n) is str:
        raise TypeError("Cannot have string factorial")
    
    if type(n) not in [int]:
        raise TypeError("Cannot have non-integer factorial")

    if n < 0:
        raise ValueError("Cannot have negative factorial")

    factorial_list = [-1] * (n+1)
    factorial_list[0] = 1

    for i in range(1, n+1, 1):
        factorial_list[i] = factorial_list[i-1] * i

    return factorial_list[n]

def main():
    user_number = int( input("Enter a number to get its factorial result: ") )
    # x = factorial_iteration(user_number)
    x = factorial_dynamic_programming(user_number)
    print("The result of ", user_number, "! is ", x)

if __name__ == "__main__":
    main()
