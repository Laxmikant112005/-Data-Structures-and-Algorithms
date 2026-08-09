# string to array and array to string coversion

arr = ['H', 'e', 'l', 'l', 'o', 1, 2, 3]
string = ''.join(map(str, arr))
print("String:", string)

new_arr = list(string)
print("Array:", new_arr)



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

# coversion os intiger array to string

def array_to_string(arr):
    return ''.join(map(str, arr))
arr = [1, 2, 3, 4, 5]
result = array_to_string(arr)
print(result)  # Output: "12345"

# time convertion 

def timeConversion(s):
    hour = int(s[0:2])
    period = s[8:]          # AM or PM
    rest = s[2:8]           # :mm:ss

    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0

    return f"{hour:02d}{rest}"


s = input()

result = timeConversion(s)
print(result)
