# -*- coding: utf-8 -*-
import sys

# input a base number from console.
argvs = sys.argv
mini_num = int(argvs[1])
max_num  = int(argvs[2]) 


def get_prime_numbers(mini_num,max_num):
    
    result = []
    print ('The range is between %d to %d.' % (mini_num, max_num))

    for num in range(mini_num,max_num + 1):
        if num > 1:
            for i in range(2,num):
                if (num %i) == 0:
                    break
            else:
                #print(num)
                result.append(num)
    return result


prime_nums = get_prime_numbers(mini_num,max_num)
print(prime_nums)
