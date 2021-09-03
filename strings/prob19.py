## https://www.hackerrank.com/challenges/string-validators/problem


if __name__ == '__main__':
    s = input()
    print(True if any([x.isalnum() for x in s]) else False)
    print(True if any([x.isalpha() for x in s]) else False)
    print(True if any([x.isdigit() for x in s]) else False)
    print(True if any([x.islower() for x in s]) else False)
    print(True if any([x.isupper() for x in s]) else False)



# print any(c.isalnum()  for c in str)
# print any(c.isalpha() for c in str)
# print any(c.isdigit() for c in str)
# print any(c.islower() for c in str)
# print any(c.isupper() for c in str)