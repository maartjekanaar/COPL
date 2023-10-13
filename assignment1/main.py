import lexing.py
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        open_file(input_file)
    else:
        print("Input invalid. Please use: python main.py <inputFile>\n")
        sys.exit(1)
