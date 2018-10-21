#
#
#       PASSWORD STRENGTH CHECKER
#       AUTHOR: JIMWELAGUINALDO
#
#

import sys
import argparse
import bloom_filter

def load_weak_pw_dictionary(filename, b_filter):
    with open(filename, 'r') as file:
        for pw in file:
            b_filter.add(pw)

def check_pw(inputfile, outputfile, b_filter):
    with open(inputfile, 'r') as input:
        with open(outputfile, 'w') as output:
            next(input)
            for pw in input:
                output.write(b_filter.membership_test(pw) + '\n')

def main():
    parser = argparse.ArgumentParser(description="Check if password is in the list of weak passwords")
    parser.add_argument('-d', action="store", required=True, dest="dictionary", help="dictionary file")
    parser.add_argument('-i', action="store", required=True, dest="input", help="input file")
    parser.add_argument('-o', action="store", nargs=2, required=True, dest="output", help="output file")
    args = parser.parse_args()    
    
    bf_3 = bloom_filter.bloom_filter(3224147, 3)
    load_weak_pw_dictionary(args.dictionary, bf_3)
    check_pw(args.input, args.output[0], bf_3)

    bf_5 = bloom_filter.bloom_filter(3224147, 5)
    load_weak_pw_dictionary(args.dictionary, bf_5)
    check_pw(args.input, args.output[1], bf_5)

if __name__ == '__main__':
    main()
