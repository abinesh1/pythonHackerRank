##  https://www.hackerrank.com/challenges/python-print/problem

if __name__ == '__main__':
    n = int(input())
    print(*[i for i in range(1,n+1)], sep='')

#print(*range(1, int(input())+1), sep='')