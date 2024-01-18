"""
Function annotations are completely optional metadata information about the types used
by user-defined functions.

Annotations are stored in the __annotations__ attribute of the function as a dictionary and have no
effect on any other part of the function. Parameter annotations are defined by a colon after the
parameter name, followed by an expression evaluating to the value of the annotation. Return
annotations are defined by a literal ->, followed by an expression, between the parameter list and
the colon denoting the end of the def statement.
"""

def function_a(test1: str,test2:str) -> str:
    return test1+test2

def test_function():
    print(function_a.__annotations__)

test_function()