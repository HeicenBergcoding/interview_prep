"""
Function can be called with an arbitrary number of arguments. These arguments will be wrapped up in
a tuple. Before the variable number of arguments, zero or more normal arguments may occur.
"""
def test_arb(num1:int,*args):
    # wrapped in tuples
    print(args)
    for a in args:
        sum = num1 + a
    return sum

print(test_arb(1,2,3,4,5))