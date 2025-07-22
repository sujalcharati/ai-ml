# list comprehension display

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
perm = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(perm)

# find runners score ...


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    ans = list(arr)
    
    max = -101
    second_max = -101
    
    for elem in ans:
        if elem > max:
            second_max = max
            max = elem
        elif elem >second_max & elem != max:
            second_max = elem
    print(second_max)
 
