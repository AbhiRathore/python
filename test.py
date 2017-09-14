import sys
def calc():
    n,m = map(int,raw_input().strip().split(' '))
    c = map(int,raw_input().strip().split(' '))
    w = map(int,raw_input().strip().split(' '))
    t = map(int,raw_input().strip().split(' '))
    d=0

    for i in range(0,m):
        for k in range(0,n):
            if c[i] < w[k]:u=-1
            else:u=1
            if c[i] >= w[k]:
                d +=1
    print u,d


 
t=input()
for i in range(0,t):
    print calc()
