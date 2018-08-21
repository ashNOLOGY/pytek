'''
Tesing the reading and parsing files with a colon (:) in between
for the Dictionary
'''

import os
import string

of = open('test.txt', 'r') #opens file
rl = of.readline() #reads file
rl2 = of.next()
rl3 = of.next()
print(rl, rl2, rl3)

#w = str.split(':')

#eng = [w[0]]
#t1 = [w[1]]
#t2 = [w[2]]
#print(eng)
#print w


of.close() #close file

