#https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    list1 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name,score])
    scores = sorted(set([x[1] for x in list1]))
    lowest = sorted([x[0] for x in list1 if x[1] == scores[1]])
    print(*lowest, sep = '\n')


    