## https://www.hackerrank.com/challenges/python-string-formatting/problem


def print_formatted(number):
    c = bin(number)
    x = len(str(c[2:]))
    for i in range(1, number+1):
        print(str(i).rjust(x)+' '+str(oct(i))[2:].rjust(x)+' '+str(hex(i))[2:].rjust(x).swapcase()+' '+str(bin(i))[2:].rjust(x))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# n = int(raw_input())
# width = len("{0:b}".format(n))
# for i in xrange(1,n+1):
#   print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))