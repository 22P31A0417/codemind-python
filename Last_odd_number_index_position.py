n=int(input())
nums=list(map(int,input().split()))
for i in range(n-1,-1,-1):
    if nums[i]%2!=0:
        print(i)
        break