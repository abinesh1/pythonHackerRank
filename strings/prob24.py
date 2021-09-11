##https://www.hackerrank.com/challenges/alphabet-rangoli/problem


import string
def print_rangoli(size):
    l = string.ascii_lowercase
    lstring = ''
    rstring = ''
    for i in range(0,size):
        if i!=0:
            for x in range(0,i):
                lstring+= l[size-x-1]+'-'
            rstring= lstring[::-1]
        print((lstring + l[size-i-1]+ rstring).center((size*2-1)*2-1, '-'))
        lstring, rstring = '', ''
    for i in reversed(range(0,size-1)):
        if i!=0:
            for x in range(0,i):
                lstring+= l[size-x-1]+'-'
            rstring= lstring[::-1]
        print((lstring + l[size-i-1]+ rstring).center((size*2-1)*2-1, '-'))
        lstring, rstring = '', ''


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# import string
# alpha = string.ascii_lowercase

# n = int(input())
# L = []
# for i in range(n):
#     s = "-".join(alpha[i:n])
#     L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
# print('\n'.join(L[:0:-1]+L))