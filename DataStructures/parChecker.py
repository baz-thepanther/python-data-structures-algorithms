from Stack import Stack

def parChecker(symbolString):
    """ Reads a string of parentheses from left to right and decides
    whether the symbols are balanced using the Stack data structure.
    >>> parChecker('((()))')
    True
    >>> parChecker('(()')
    False
    """
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index += 1

    return balanced and s.isEmpty()

def parChecker2(symbolString):
    """Generalized version of the balanced symbols checker.
    Can check parentheses, brackets, and curly brackets.
    >>> parChecker('{{([][])}()}')
    True
    >>> parChecker('{{{}()}])')
    False
    """
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    return balanced and s.isEmpty()

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

