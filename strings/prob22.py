## https://www.hackerrank.com/challenges/designer-door-mat/problem

m, n= map(int, input().split())
for r in range(0,m//2):
    print('-'*((n//2)-(3*(r+1))+2)+'.|.'*(1+(2*r))+'-'*((n//2)-(3*(r+1))+2))
print('-'*((n-7)//2)+'WELCOME'+'-'*((n-7)//2))
for r in reversed(range(0, m//2)):
    print('-'*((n//2)-(3*(r+1))+2)+'.|.'*(1+(2*r))+'-'*((n//2)-(3*(r+1))+2))


# n, m = map(int,input().split())
# pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))


# N, M = map(int,input().split())
# for i in range(1,N,2): 
#     print((i * ".|.").center(M, "-"))
# print("WELCOME".center(M,"-"))
# for i in range(N-2,-1,-2): 
#     print((i * ".|.").center(M, "-"))
