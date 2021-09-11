## https://www.hackerrank.com/challenges/merge-the-tools/problem


def merge_the_tools(string, k):
    x = [''.join(dict.fromkeys(string[i:i+k])) for i in range(0,len(string), k)]
    print(*x, sep = '\n')

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


