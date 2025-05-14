elements, numRungs = map(int, input().split())
rungList = [int(input()) for x in range(numRungs)]
permList = [x+1 for x in range(elements)]

for i in range(len(rungList)):
    numIndex1 = rungList[i]-1
    numIndex2 = rungList[i]

    temp = permList[numIndex1]
    permList[numIndex1] = permList[numIndex2]
    permList[numIndex2] = temp

for num in permList:
    print(num)

    


