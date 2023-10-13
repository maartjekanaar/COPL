# Implementation of lexing.

import parsing.py
import string
import io


def isPrintableASCII(character):
    ASCII = ord(character)
    return 32 <= ASCII <= 126


def isWhitespace(character):
    ASCII = ord(character)
    return ASCII in (9, 11, 12, 13, 32)


def openFile(inputFile):
    try:
        with open(inputFile) as input:
            readIn(input)
    except FileNotFoundError:
        print(f"Sorry but your file: {inputFile} cannot be opened.\n")
        exit(1)
    except Exception as e:
        print("An error occurred:", str(e))


def readIn(input):
    expression = []
    character = input.read(1)
    number_of_expression = 0

    while character:
        expressions.append("")
        while character != "\n":
            if not (isPrintableASCII(character) or isWhitespace(character)):
                print(
                    "File contains non-printable ASCII character that is not white-space.\n"
                )
                exit(1)

            expression[numberOfExpression] += character
            character = input.read(1)

            if not character:
                break

        numberOfExpression += 1

    input.close()
    transformToTokens(expression)


def transformToTokens(expressions):
    tokens = []
    expression_list = []

    for expression in expressions:
        size_of_expression = len(expression)
        token = ""
        i = 0

        while i < size_of_expression:
            character = expression[i]

            if is_parenthesis(character):
                if token:
                    tokens.append(token)
                    token = ""
                token += character
                tokens.append(token)
                token = ""
            elif is_backslash(character):
                if token:
                    tokens.append(token)
                    token = ""
                token += character
                tokens.append(token)
                token = ""
            elif is_letter(character):
                token += character
            elif is_digit(character):
                if not token:
                    print("Variable name can not start with a digit.")
                    exit(1)
                token += character
            elif is_whitespace(character):
                if token:
                    tokens.append(token)
                    token = ""
                i += 1
                continue
            else:
                print(f"Token '{character}' is invalid.")
                exit(1)

            i += 1

        if token:
            tokens.append(token)
            token = ""
        expression_list.append(tokens)
        tokens = []

    parse_expressions(expression_list)


def isLetter(character):
    return character.isalpha()


def isDigit(character):
    return character.isdigit()


def isParenthesis(character):
    return character in "()"


def isBackslash(character):
    return character == "\\"
