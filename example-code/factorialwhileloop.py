


def factorial_while(n):
    product = 1

    iterator = n
    while iterator >= 1:
        product *= iterator

        iterator = iterator - 1
        
        print(iterator)
    
    return product


if __name__ == "__main__":
    print(factorial_while(10))