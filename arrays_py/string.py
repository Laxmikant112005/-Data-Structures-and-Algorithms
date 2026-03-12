# camelcase problem


def camelcase(s):
    count = 1
    for c in s:
        if c.isupper():
            count += 1
    return count
s = input("Enter a string in camel case : ")
print(camelcase(s)) 


# strong password checker

def strong(password):
    lower = upper = digit = special = False

    for c in password:
        if c.islower():
            lower = True
        elif c.isupper():
            upper = True
        elif c.isdigit():
            digit = True
        elif c in "!@#$%^&*()-+":
            special = True

    missing = 4 - (lower + upper + digit + special)

    return max(missing, 6 - len(password))


password = input(" Enter your password . ")
res = strong(password)
if res == 0:
    print(" strong password !")
else :
    print(f"Not strong {res} instruction is missing")

