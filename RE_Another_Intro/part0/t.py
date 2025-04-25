import re
def isDigit(ch):
    return re.search(ch, "[0-9]") != None
print(isDigit("4"))