# Implementation of parsing.

# LL grammar:
# <expr>   ::= <lexpr> <expr1>
# <expr1>  ::= <lexpr> <expr1> | empty
# <lexpr>  ::= <pexpr> | '\' <var> <lexpr>
# <pexpr>  ::= <var> | '(' <expr> ')'


def parseExpressions(expressions):
    for expression in expressions:
        tokens = expression
        numberOfToken = 0
        expr(tokens, numberOfToken)
        if not sameAmountOfParentheses(tokens):
            print("Syntax error.")
            exit(1)
        tokens.clear()
    printExpressions(expressions)


def expr(tokens, numberOfToken):
    lexpr(tokens, numberOfToken)
    expr1(tokens, numberOfToken)


def expr1(tokens, numberOfToken):
    if not isLastToken(tokens, numberOfToken) and isLexpr(tokens[numberOfToken]):
        lexpr(tokens, numberOfToken)
        expr1(tokens, numberOfToken)


def lexpr(tokens, numberOfToken):
    if tokens[numberOfToken] == "\\":
        if not consume(tokens, numberOfToken):
            print("Missing variable after lambda.")
            exit(1)
        if isVariableName(tokens[numberOfToken]):
            if not consume(tokens, numberOfToken):
                print("Missing expression after lambda abstraction.")
                exit(1)
            lexpr(tokens, numberOfToken)
        else:
            print("Missing variable after lambda.")
            exit(1)
    else:
        pexpr(tokens, numberOfToken)


def pexpr(tokens, numberOfToken):
    if isVariableName(tokens[numberOfToken]):
        consume(tokens, numberOfToken)
    elif tokens[numberOfToken] == "(":
        if not consume(tokens, numberOfToken):
            print("Missing expression after opening parenthesis.")
            exit(1)
        expr(tokens, numberOfToken)
        if tokens[numberOfToken] == ")":
            consume(tokens, numberOfToken)
        else:
            print("Missing closing parenthesis.")
            exit(1)
    else:
        print("Syntax error.")
        exit(1)


def isLexpr(token):
    return token in (isVariableName(token), "(", "\\")


def isLastToken(tokens, numberOfToken):
    return len(tokens) == numberOfToken + 1


def consume(tokens, numberOfToken):
    if isLastToken(tokens, numberOfToken):
        return False
    numberOfToken += 1
    return True


def isVariableName(token):
    return token.isalpha()


def sameAmountOfParentheses(tokens):
    numberOfOpeningParentheses = 0
    numberOfClosingParentheses = 0

    for token in tokens:
        if token == "(":
            numberOfOpeningParentheses += 1
        elif token == ")":
            numberOfClosingParentheses += 1

    return numberOfOpeningParentheses == numberOfClosingParentheses


def peek(tokens, numberOfToken):
    if numberOfToken + 1 < len(tokens):
        return tokens[numberOfToken + 1]
    else:
        return None


def printExpressions(expressions):
    for expression in expressions:
        tokens = expression
        for token in tokens:
            print(token, end=" ")
        print()
