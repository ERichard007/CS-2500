days, minSegSize, maxSegSize = map(int, input().split())
prefixSum = [0] * (days+1)
dailyProfits = [0] * (days)

sum = 0
for i in range(days):
    num = int(input())
    sum += num
    prefixSum[i+1] = sum
    dailyProfits[i] = num

minProfitSegs, maxProfitSegs = float("inf"), float("-inf")
for segSize in range(minSegSize, maxSegSize + 1):
    for offset in range(segSize):
        start = offset
        profitCount = 0

        #print(f"TESTING: SegSize: {segSize} start: {start}") TESTING
        if(offset > 0):
            end = offset
            segSum = prefixSum[end]

            '''
            ###FOR TESTING###
            print('< ', end="")
            for num in range(end):
                print(f'{dailyProfits[num]}, ', end="")
            print('>')
            '''

            if (segSum > 0):
                profitCount += 1

        while (start < days):
            end = min(days, start+segSize)
            segSum = prefixSum[end] - prefixSum[start]

            '''
            ###FOR TESTING###
            print('< ', end="")
            for num in range(start, end):
                print(f'{dailyProfits[num]}, ', end="")
            print('>') 
            '''
            
            if (segSum > 0):
                profitCount += 1
            start += segSize

        #print(f'PROFIT: {profitCount}') TESTING
        minProfitSegs = min(minProfitSegs, profitCount)
        maxProfitSegs = max(maxProfitSegs, profitCount)

print(f"{minProfitSegs} {maxProfitSegs}")