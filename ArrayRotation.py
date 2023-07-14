array = list(map(int,input().strip().split()))
rotate = int(input())

for i in range(rotate):
    temp = array[len(array)-1]
    array[1:len(array)] = array[0:len(array)-1]
    array[0] = temp

print(array)
