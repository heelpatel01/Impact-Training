# Eval:- 
# The eval() function evaluates the specified expression, if the expression is a legal Python statement, it will be executed.
# Syntax :- 
# eval(expression, globals, locals)
# Parameter Values
# Parameter	Description:
# expression:	A String, that will be evaluated as Python code
# globals:	    A dictionary containing global parameters (Optional)
# locals:	    A dictionary containing local parameters (Optional)

a = eval(input("Enter equation"))
print(a)