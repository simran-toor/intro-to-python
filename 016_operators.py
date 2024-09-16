# breaking down `add_one`

def add_one(num):
    return num + 1

# `def`: keyword that defines a new function 
# `add_one`: fuction name 
# `(num)`: parameter list
#`:`: indicates the body should start now 
# `return num + 1`: statement
# `num + 1`: expression 
# `+`: operator
# `1`: literal number

# python operators 

# ARITHMETIC OPERATORS

# addition 
added = 2 + 3
print(added)

# multiplication 
multiplied = 2 * 3
print(multiplied)

# subtraction
subtraction = 2 - 3
print(subtraction)

# division
division = 2 / 3 
print(division)
# this kind of 'decimal point' number 0.666666666 is called a `float` meaning `floating point`

# modulus 
# sometimes known as "remainder if you divide 3 by 2"

modulus = 3 % 2
print(modulus)

# floor division 
# sometimes known as "division without remainder"
floor_divided = 2 // 3
print(floor_divided)

# exponentiation
# sometimes known as "2 to the power of 3"

expr = 2 ** 3
print(expr)

# There are many more operators in Python that you can
# research. You're very welcome to try out a few below:

# OPERATOR PLAYGROUND STARTS

# ASSIGNMENT OPERATORS

# equals
x = 5 
print(x)

#plus equal
x = 5
x += 3 
print(x)

# minus equal
x = 5
x -= 3 
print(x)

# multiply equal 
x = 5
x *= 3
print(x)

# divide equal 
x = 5
x /= 3
print(x)

# modulus equal 
x = 5
x %= 3
print(x)

# floor divide equal 
x = 5
x //= 3
print(x)

# exponential equal 
x = 5 
x **= 3
print(x)

# AND equals 
# `&` operator sets each bit to 1 if both bits are 1 
x = 5 
x &= 3
print(x)

# OR equals
# `|` operator sets each bit to 1 if one of the two bits is 1
x = 5 
x |= 3 
print(x)

# XOR equals 
# `^` operator sets each bit to 1 if only one of the two bits is 1 
x = 5 
x ^= 3
print(x)

# NOT 
# `~` operator inverts all the bits 
print(~3)

# print 
print(x := 3)

# COMPARISON OPERATORS 

# equal `==`
x = 5 
y = 3
print(x == y)
# returns false because 5 is not equal to 3

# not equal `!=`
x = 5
y = 3
print(x != y)
# returns true because 5 is not equal to 3

# greater than `>`
x = 5 
y = 3
print(x > y)
# returns true because 5 is greater than 3

# less than `<`
x = 5 
y = 3
print(x < y)
# returns false because 5 is not less than 3

# greater than or equal `>=`
x = 5 
y = 3
print(x >= y)
# returns true because 5 is greater or equal to 3

# less than or equal `<=`
x = 5 
y = 3
print(x <= y)
# returns false because 5 is not less than or equal to 3

# LOGICAL OPERATORS

# and 
# returns true if both statements are true
x = 5 
print(x > 3 and x < 10)
# returns true because 5 is greater than 3 AND 5 is less than 10

# or
# returns true if one of the statements is true 
x = 5 
print(x > 3 or x < 4)
# returns true because of the conditions are true ( 5 is greater than 3)

# not 
# reverse the result, returns false if the result is true
x = 5 
print(not(x > 3 and x < 10))
# returns false because not is used to reverse the result

# IDENTITY OPERATORS 

# is 
# returns true is both variables are the same object 
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns true because z is the same object as x 
print(x is y)
# returns false because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate difference between `is` and `==`: returns true because x is equal to y

# is not 
# returns true if both variabls are not the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
# returns false because z is the same object as x
print(x is not y)
# returns true because x is not the same object as y, even if they have the same content
print(x != y)
# to demonstrate difference between `is not` and `!=`: returns false because x is equal to y

# OPERATOR PLAYGROUND ENDS