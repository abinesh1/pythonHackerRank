##https://www.hackerrank.com/challenges/python-lists/forum


if __name__ == '__main__':
    N = int(input())
    list1 = [] 
    for _ in range(N):
        ins = input().strip().split()
        if ins[0] == 'insert':
            list1.insert(int(ins[1]), int(ins[2]))
        elif ins[0] == 'print':
            print(list1)
        elif ins[0] == 'append':
            list1.append(int(ins[1]))
        elif ins[0] == 'remove':
            list1.remove(int(ins[1]))
        elif ins[0] == 'pop':
            list1.pop()
        elif ins[0] == 'sort':
            list1.sort()
        elif ins[0] == 'reverse':
            list1.reverse()
        


# n = input()
# l = []
# for _ in range(n):
#     s = raw_input().split()
#     cmd = s[0]
#     args = s[1:]
#     if cmd !="print":
#         cmd += "("+ ",".join(args) +")"
#         eval("l."+cmd)
#     else:
#         print l