# -*- coding: utf-8 -*-
import sys
import pprint
import itertools

# input a base number from console.
argvs = sys.argv
mini_num = int(argvs[1])
max_num  = int(argvs[2])


# Set a range and
# get prime numbers by for loops
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


# run
prime_nums = get_prime_numbers(mini_num,max_num)
print("Prime Numbers are: ", prime_nums)


# create duplicated permutations
def get_compositions(prime_nums):

    result = []
    for i in range(len(prime_nums), 0, -1):
        for seq in itertools.product(prime_nums, repeat=i):
            if sum(seq) == max_num:
                result.append(seq)
    return result


pairs = get_compositions(prime_nums);
print('All combinations are:')
pprint.pprint(pairs)
#print(len(pairs))
