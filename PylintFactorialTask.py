def factorial (x)
    if x == 1:
        return 1

    else:
        return (x * factorial(x-1))

num = 3
print("The factorial of", num, "is", factorial(num))  

# Pylint error message -	'Parsing failed: 'expected ':' (PylintFactorialTask, line 1)'
# This message indicates that there is a missing colon following the
# initial function definition line.


# Source: Progamiz. (n.d.) Python Recursion.