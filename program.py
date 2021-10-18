#!/usr/bin/env python3

# Created by: Igor
# Created on: Oct 2021
# This is math_program


def main():
    # input
    integer1 = input("Enter the first number: ")
    integer2 = input("Enter the second number: ")
    try:
        number1 = float(integer1)
        number2 = float(integer2)
        if number1 == number2:
            print("{0} = {1}".format(number1, number2))
        elif number1 < number2:
            print("{0} < {1}".format(number1, number2))
        else:
            print("{0} > {1}".format(number1, number2))

    except Exception:
        print("This was not a number")
    finally:
        print("")
        print("Done.")


if __name__ == "__main__":
    main()
