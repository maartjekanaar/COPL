# Main program.

from lexing import *
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        inputFile = sys.argv[1]
        openFile(inputFile)
    else:
        print("Input invalid. Please use: python main.py <inputFile>\n")
        sys.exit(1)
