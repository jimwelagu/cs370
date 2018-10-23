#
#
#       PASSWORD STRENGTH CHECKER
#       AUTHOR: JIMWELAGUINALDO
#
#

import sys
import math
import argparse
import bloom_filter

def bit_filter_size(n, p, k):
    num = n * math.log(p)
    den = math.pow(math.log(2), 2)
    return int(math.ceil((num / den) * -1))

def load_weak_pw_dictionary(filename, b_filter):
    with open(filename, 'r') as file:
        for pw in file:
            b_filter.add(pw.strip())

def check_pw(inputfile, outputfile, b_filter):
    with open(inputfile, 'r') as input:
        with open(outputfile, 'w') as output:
            next(input)
            for pw in input:
                output.write(b_filter.membership_test(pw.strip()) + '\n')

def main():
    parser = argparse.ArgumentParser(description="Check if password is in the list of weak passwords")
    parser.add_argument('-d', action="store", required=True, dest="dictionary", help="dictionary file")
    parser.add_argument('-i', action="store", required=True, dest="input", help="input file")
    parser.add_argument('-o', action="store", nargs=2, required=True, dest="output", help="output file")
    args = parser.parse_args()    
   
    probability = 0.0000001
    num_elements = 623517
    
    bit_3_size = bit_filter_size(num_elements, probability, 3)
    bf_3 = bloom_filter.bloom_filter(bit_3_size, 3)
    print("Bloom Filter with 3 Hash Functions Size: {}".format(bit_3_size))
    load_weak_pw_dictionary(args.dictionary, bf_3)
    check_pw(args.input, args.output[0], bf_3)

    bit_5_size = bit_filter_size(num_elements, probability, 5)
    bf_5 = bloom_filter.bloom_filter(bit_5_size, 5)
    print("Bloom Filter with 5 Hash Functions Size: {}".format(bit_5_size))
    load_weak_pw_dictionary(args.dictionary, bf_5)
    check_pw(args.input, args.output[1], bf_5)

if __name__ == '__main__':
    main()
