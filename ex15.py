#imports argv module
from sys import argv
#unpacks argument
script, filename = argv
#opens the filename from the argument
txt = open(filename)
#prints with the filename argument name
print(f"Here's your file {filename}:")
#prints the contents of the file
print(txt.read())

#prints a line to request the filename
print("Type the filename again:")
#filename line to input
file_again = input("> ")
#opens file again
txt_again = open(file_again)
#prints the contents of the file again
print(txt_again.read())
