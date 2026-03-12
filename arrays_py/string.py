# camelcase problem


def camelcase(s):
    count = 1
    for c in s:
        if c.isupper():
            count += 1
    return count
s = input("Enter a string in camel case : ")
print(camelcase(s)) 
