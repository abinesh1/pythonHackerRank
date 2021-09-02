##https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    for i, x in enumerate(arr):
        if arr[i+1]<arr[i]:
            print(arr[i+1])
            break

# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     print (sorted(set(arr))[-2])