import sys

numFoundationPoints, smallestPlatformLength, largestPlatformLength = map(int, input().split())
foundationPoints = [int(input()) for x in range(numFoundationPoints)]

foundationPoints = sorted(foundationPoints)
lengths = [largestPlatformLength] * numFoundationPoints

for i in range(numFoundationPoints-1):
    if (lengths[i] + lengths[i+1] > 2 * (foundationPoints[i+1] - foundationPoints[i])):
        newLength1 = min(lengths[i], 2 * (foundationPoints[i+1] - foundationPoints[i]) - smallestPlatformLength)
        newLength2 = 2 * (foundationPoints[i+1] - foundationPoints[i]) - newLength1

        if (newLength1 < smallestPlatformLength):
            print(-1)
            sys.exit()

        lengths[i] = newLength1
        lengths[i+1] = newLength2
    
    #print(f'***{lengths}***')

print(sum(lengths))