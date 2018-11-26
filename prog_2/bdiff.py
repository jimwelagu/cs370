import argparse


def compare(str1, str2):
    changes = 0;
    for x in range(len(str1)):
        if(str1[x] != str2[x]):
            changes = changes+1

#    if(len(str1) < len(str2)):
 #       changes = changes + (len(str2) - len(str1))

    return changes

def add_padding(binary, x):
    for i in range(x):
        binary = "0" + binary

    return binary

def main():
    string1 = raw_input("s1: ")
    string2 = raw_input("s2: ")
    
    if(len(string1) > len(string2)):
        diff = len(string1) - len(string2)
        print("Padding added to str2...")
        string2 = add_padding(string2, diff)
    elif(len(string2) > len(string1)):
        diff = len(string2) - len(string1)
        print("Padding added to str1...")
        string1 = add_padding(string1, diff)
        
    print(compare(string1, string2))

    return 


main()
