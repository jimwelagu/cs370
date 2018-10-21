#
#
#       PASSWORD STRENGTH CHECKER
#       AUTHOR: JIMWELAGUINALDO
#
#

import sys
import io
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
    parser.add_argument('-o', action="store", required=True, dest="output", help="output file")
    args = parser.parse_args()    
    
    bf_3 = bloom_filter.bloom_filter(3224147, 3)
    load_weak_pw_dictionary(args.dictionary, bf_3)
    check_pw(args.input, args.output, bf_3)

if __name__ == '__main__':
    main()
