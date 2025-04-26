import re
def isDigit(ch):
    return re.search(ch, "d") != None
print(isDigit("8"))