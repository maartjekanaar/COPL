# Implementation of lexing.

from parsing import *


def isPrintableASCII(character):
    ASCII = ord(character)
    return 33 <= ASCII <= 126


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
    expressions = []
    expression = ""

    for character in input:
        if character != "\n":
            if not (isPrintableASCII(character) or isWhitespace(character)):
                print(
                    "File contains non-printable ASCII character that is not white-space.\n"
                )
                exit(1)

            expression += character

        else:
            expressions.append(expression)
            expression = ""

    transformToTokens(expressions)


def transformToTokens(expressions):
    tokens = []
    expressionList = []

    for expression in expressions:
        token = ""

        for character in expression:
            if isParenthesis(character) or isBackslash(character):
                if token:
                    tokens.append(token)
                    token = ""
                token += character
                tokens.append(token)
                token = ""
            elif isLetter(character):
                token += character
            elif isDigit(character):
                if not token:
                    print("Variable name can not start with a digit.")
                    exit(1)
                token += character
            elif isWhitespace(character):
                if token:
                    tokens.append(token)
                    token = ""
                continue
            else:
                print(f"Token '{character}' is invalid.")
                exit(1)

        if token:
            tokens.append(token)
            token = ""
        expressionList.append(tokens)
        tokens = []

    parseExpressions(expressionList)


def isLetter(character):
    return character.isalpha()


def isDigit(character):
    return character.isdigit()


def isParenthesis(character):
    return character in ("(", ")")


def isBackslash(character):
    return character == "\\"
