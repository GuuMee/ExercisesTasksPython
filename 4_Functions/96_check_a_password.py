"""
In this exercise you will write a function that determines whether or not a password
is good. We will define a good password to be a one that is at least 8 characters
long and contains at least one uppercase letter, at least one lowercase letter, and at
least one number. Your function should return true if the password passed to it as
its only parameter is good. Otherwise it should return false. Include a main program
that reads a password from the user and reports whether or not it is good. Ensure
that your main program only runs when your solution has not been imported into
another file.
"""


def check_password(password):
    has_upper = False
    has_lower = False
    has_num = False

    for ch in password:
        if ch >= "A" and ch <= "Z":
            has_upper = True
        elif ch >= "a" and "z":
            has_lower = True
        elif ch >= "0" and ch <= "9":
            has_num = True

    if len(password) >= 8 and has_upper and has_lower and has_num:
        return True

    return False


def main():
    p = input("Enter a password: ")
    if check_password(p):
        print("That's a good password.")
    else:
        print("That isn't a good password.")

if __name__ == '__main__':
    main()

