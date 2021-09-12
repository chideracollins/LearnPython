# Symbols Identifier
a = input("Enter the symbols: ")
z = "abcdefghijklmnopqrstuvwxyz"
y = z.upper()
g = "1234567890" 
def identifySymbols(a):
    for letter in a: 
        if letter == "a [len(a) - 1]":
            break
        if letter in z:
            print(letter + " is an alphabet.")
        elif letter in y:
            print(letter + " is an alphabet.")
        elif letter in g:
            print(letter + " is a figure.")
        else:
             print(letter + " is an unknown character.")
identifySymbols(a)
