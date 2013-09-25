# import arithmetic
#user input
# split it into a list of tokens
# check tokens[0] to see what operation to do 
# call upon corresponding function in arithmetic
# everything in a loop

from arithmetic import *

def main():

    while True:
        user_input = raw_input("> ")
        tokens = user_input.split(" ")

        if tokens[0] == "+":
            result = add(int(tokens[1]), int(tokens[2]))
            print result
        elif tokens[0] == "-":
            result = subtract(int(tokens[1]), int(tokens[2]))
            print result
        elif tokens[0] == "*":
            result = multiply(int(tokens[1]), int(tokens[2]))
            print result
        elif tokens[0] == "/":
            result = divide(float(tokens[1]), float(tokens[2]))
            print result
        elif tokens[0] == "square":
            result = square(int(tokens[1]))
            print result
        elif tokens[0] == "cube":
            result = cube(int(tokens[1]))
            print result
        elif tokens[0] == "pow":
            result = power(int(tokens[1]), int(tokens[2]))
            print result
        elif tokens[0] == "mod":
            result = mod(int(tokens[1]), int(tokens[2]))
            print result
        elif tokens[0] == "q" or tokens[0] == "Q":
            exit()
        else:
            print "We're using infix notation! Fancy eh?"



main()





