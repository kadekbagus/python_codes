#!/usr/bin/python

var_string = 'this is a string'
var_integer = 12
var_float = 3.6

var_list = [1,2,3,'test 123']
var_dictionary = {'a':1, 'b':2, 'c':3}

print(type(var_string), var_string)
print(type(var_integer), var_integer)
print(type(var_float), var_float)
print(type(var_list), var_list)
print(type(var_dictionary), var_dictionary)

print(var_string,'yow!')
message = var_string + ' oke'
print(message)