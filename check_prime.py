# -*- coding: utf-8 -*-
import math



def main():

    number = 6
    print(check_prime(number))


def check_prime(number):

    # 0と1は素数ではない
    if number < 2:
        return False
    elif number < 4:
        return True
    elif number % 2 == 0:
        return False
    else:
        print('Something Wrong...')

    odd_numbers = range(3, int(math.sqrt(number)) + 1, 2)
    return not any(number % i == 0 for i in odd_numbers)


if __name__ == "__main__":
    main()




