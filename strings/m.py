def print_formatted(number):
    c = bin(number)
    x = len(str(c[2:]))
    print("{0:{width}b}".format(number, width = 5))
    # for i in range(1, number+1):
    #     print(str(i).rjust(x)+' '+str(oct(i))[2:].rjust(x)+' '+str(hex(i))[2:].rjust(x).swapcase()+' '+str(bin(i))[2:].rjust(x))
    

if __name__ == '__main__':
    print_formatted(15)