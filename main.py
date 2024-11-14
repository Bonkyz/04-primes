# from math import sqrt

#### Fonction secondaire
"""this module create a string of prime numbers"""

def isprime(p):
    """Function to define if the parameter p is prime"""
    premier = True
    for d in range (2, p-1) :
        if p%d == 0 :
            premier = False
            break
    return premier
#    pass

#### Fonction principale


def main():
    """main function printing the prime number in a range"""
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
