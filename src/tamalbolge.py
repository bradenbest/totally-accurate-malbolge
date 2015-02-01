#!/usr/bin/python3
# Braden's Totally Accurate Malbolge interpreter

from random import randint
import sys

the_only_valid_program = '(=<`#9]~6ZY32Vx/4Rs+0No-&Jk)"Fh}|Bcy?`=*z]Kw%oG4UUS0/@-ejc(:\'8dc'

outputs = [
    # Errors
    "Stack Overflow",
    "Too many arguments",
    "Not enough arguments",
    "Segmentation Fault.",
    "Invalid Expression",
    "Invalid Syntax",
    # Weird outputs
    "� � � � � � � � � � � � � � � � � � � � � � ",
    "g?HfjkktHHGMMmm,,",
    "YJ^B^jybjyiYHnrth^N^N",
    "^@\n",
    "^A^A^A^A^A^A^A^A^A^A^A^A^A^A^A^A^A^A^A^A^A^A^@",
    "/L,A",
    "/L,R",
    "/L,R...",
    "/..."
]

if len(sys.argv) > 1:
    c_f = open(sys.argv[1],'r')
    code = c_f.read()
    c_f.close()
    if code[:-1] == the_only_valid_program:
        print("Hello World!")
    else:
        i = randint(0,len(outputs)-1)
        if outputs[i][0] == "/":
            command = outputs[i][1:].split(',')
            for cmd in command:
                if cmd == "L":
                    print("")
                elif cmd == "A":
                    while 1: print("^A", end='')
                elif cmd == "R":
                    print(chr(randint(0,255)))
                elif cmd == "R...":
                    while 1: print(chr(randint(0,255)), end='')
                elif cmd == "...":
                    while 1: pass
        else:
            print(outputs[i])
else:
    print("Usage: python3 %s file.mal" % argv[0])
