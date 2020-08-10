"""
Mathematical expressions are often written in infix form, where operators appear
between the operands on which they act. While this is a common form, it is also
possible to express mathematical expressions in postfix form, where the operator
appears after both operands. For example, the infix expression 3+4 is written as
34+ in postfix form. One can convert an infix expression to postfix form using
the following algorithm:

Create a new empty list, operators
Create a new empty list, postfix
For each token in the infix expression
    If the token is an integer then
        Add the token to the end of postfix
    If the token is an operator then
        While operators is not empty and
                the last item in operators is not an open parenthesis and
                precedence(token) < precedence(last item in operators) do
            Remove the last item from operators and add it to postfix
        Add token to the end of operators
    If the token is an open parenthesis then
        Add token to the end of operators
    If the token is a close parenthesis then
        While the last item in operators is not an open parenthesis do
            Remove the last item from operators and add it to postfix
        Remove the open parenthesis from operators
While operators is not the empty list do
    Remove the last item from operators and add it to postfix
Return postfix as the result of the algorithm

Use your solution to Exercise 122 to tokenize a mathematical expression. Then
use the algorithm above to transform the expression from infix form to postfix form.
Your code that implements the preceding algorithm should reside in a function that
takes a list of tokens representing an infix expression as its only parameter. It should
return a list of tokens representing the equivalent postfix expression as its only result.
Include a main program that demonstrates your infix to postfix function by reading
an expression from the user in infix form and displaying it in postfix form.

The purpose of converting from infix form to postfix form will become apparent
when you read Exercise 124. You may find your solutions to Exercises 90 and 91
helpful when completing this problem.
The algorithms provided in Exercises 123 and 124 do not perform any error
checking. As a result, you may crash your program or receive incorrect results
if you provide them with invalid input. These algorithms can be extended to
detect invalid input and respond to it in a reasonable manner. Doing so is left
as an independent study exercise for the interested student.
"""

from _122_tokenizing_a_string import token_list
from _91_operator_precedence import operator_precedence

BASE_OPERATORS = ["+", "-", "*", "/", "^"]


def infix_to_postfix (tokens):
    operators = []
    postfix = []

    for i in range(0, len(tokens)):
        if int(i) == int:
            postfix.append(i)
        elif i in BASE_OPERATORS:
            while len(operators) != 0 and operators[-1] != "(" and  \
                    operator_precedence(i) < operator_precedence(operators[-1]):
                from_operators = operators.pop(-1)
                postfix.append(from_operators)
            operators.append(i)
        elif i == "(":
            operators.append(i)
        elif i == ")":
            while operators[-1] != "(":
                take = operators.pop(-1)
                postfix.append(take)
            operators.remove(i)

    while len(operators) != 0:
        take = operators.pop(-1)
        postfix.append(take)

    return postfix


def main():
    line = input("Enter infix math expression(2+3): ")
    tokens = token_list(line)
    postfix = infix_to_postfix(tokens)
    print("Yor expression in postfix:", postfix)


if __name__ == '__main__':
    main()
