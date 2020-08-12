"""
Evaluating a postfix expression is easier than evaluating an infix expression because it
does not contain any brackets and there are no operator precedence rules to consider.
A postfix expression can be evaluated using the following algorithm:
Create a new empty list, values
For each token in the postfix expression
If the token is a number then
Convert it to an integer and add it to the end of values
Else
Remove an item from the end of values and call it right
Remove an item from the end of values and call it left
Apply the operator to left and right
Append the result to the end of values
Return the first item in values as the value of the expression
Write a program that reads a mathematical expression in infix form from the user,
evaluates it, and displays its value. Uses your solutions to Exercises 122 and 123
along with the algorithm shown above to solve this problem.

"""