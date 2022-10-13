#This program will take your input and print 5 different, shuffeled, versions of your input.

from random import sample
the_input = input("Write whatever you want, preferrably a word with 5 letters: ")

a = ''.join(sample(the_input, len(the_input)))
b = ''.join(sample(the_input, len(the_input)))
c = ''.join(sample(the_input, len(the_input)))
d = ''.join(sample(the_input, len(the_input)))
e = ''.join(sample(the_input, len(the_input)))
print(a)
print(b)
print(c)
print(d)
print(e)
