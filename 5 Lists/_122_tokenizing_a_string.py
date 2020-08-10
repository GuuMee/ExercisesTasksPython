"""
Tokenizing is the process of converting a string into a list of substrings, known as
tokens. In many circumstances, a list of tokens is far easier to work with than the
original string because the original string may have irregular spacing. In some cases
substantial work is also required to determine where one token ends and the next one
begins.
In a mathematical expression, tokens are items such as operators, numbers and
parentheses. Some tokens, such as *, /,ˆ, ( and ) are easy to identify because the
token is a single character, and the character is never part of another token. The + and
- symbols are a little bit more challenging to handle because they might represent
the addition or subtraction operator, or they might be part of a number token.
Hint: A + or - is an operator if the non-whitespace character immediately
before it is part of a number, or if the non-whitespace character immediately
before it is a close parenthesis. Otherwise it is part of a number.
Write a function that takes a string containing a mathematical expression as its
only parameter and breaks it into a list of tokens. Each token should be a parenthesis,
an operator, or a number with an optional leading + or - (for simplicity we will
only work with integers in this problem). Return the list of tokens as the function’s
result.
You may assume that the string passed to your function always contains a valid
mathematical expression consisting of parentheses, operators and integers. However,
your function must handle variable amounts of whitespace between these
elements. Include a main program that demonstrates your tokenizing function by
reading an expression from the user and printing the list of tokens. Ensure that the
main program will not run when the file containing your solution is imported into
another program.
"""


# Convert a mathematical expression into a list of tokens
# @param s the string to tokenize
# @return a list of the tokens in s, or empty list of an error occurs
def token_list(s):
    # Remove all of the spaces from s
    s = s.replace(" ", "")

    # Look through all of the characters in the string
    # identifying the tokens adding them to the list
    tokens = []
    i = 0
    while i < len(s):
        # Handle the tokens that are always a single character: *,/,^,( and )
        if s[i] == "*" or s[i] == "/" or s[i] == "^" or s[i] == "(" or s[i] == ")":
            tokens.append(s[i])
            i += 1
        # Handle + and -
        elif s[i] == "+" or s[i] == "-":
            # If there is a previous character and it is a number or close bracket
            # then the + or - is a token its own
            if i > 0 and ("0" <= s[i - 1] <= "9" or s[i - 1] == ")"):
                tokens.append(s[i])
                i += 1
            else:
                # The + or - is part of a number
                num = s[i]
                i += 1
                # Keep on adding characters to the token as long as they are digits
                while i < len(s) and "0" <= s[i] <= "9":
                    num += s[i]
                    i += 1
                tokens.append(num)

            # Handle a number without a leading + or -
        elif "0" <= s[i] <= "9":
            num = ""
            # Keep on adding characters to the token as long as they are digits
            while i < len(s) and "0" <= s[i] <= "9":
                num += s[i]
                i += 1
            tokens.append(num)

        # Any other character means the expression is not valid
        # Return an empty list to indicate that an error occurred
        else:
            return []
    return tokens


# Read an expression from the user and tokenize it, displaying the result
def main():
    exp = input("Enter a mathematical expression: ")
    tokens = token_list(exp)
    print("The tokens are: ", tokens)


# Call the main function only if the file hasn't been
if __name__ == '__main__':
    main()

