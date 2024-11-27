'''
Immutable Data and IO
Homework 4
27/11/2024
'''

#

a = "this"
b = "is"
c = "great"

print(a,b,c)

(a, b, c) = (c, a, b)

print(a,b,c)