days, minSegSize, maxSegSize = map(int, input().split())
prefixSum = []
dailyProfits = []

print(days)

sum = 0
for i in range(days):
    num = int(input())
    sum += num
    prefixSum.append(sum)
    dailyProfits.append(num)

print(prefixSum)
print(dailyProfits)


minProfitSegs, maxProfitSegs = float("inf"), float("-inf")
for segSize in range(minSegSize, maxSegSize):
    for offset in range(0, segSize-1):
        start = offset
        profitCount = 0
        while (start < days-1):
            end = min(days-1, (start+segSize)-1)
            segSum = prefixSum[end] - prefixSum[start]
            if (segSum > 0):
                profitCount += 1
            start += segSize
        minProfitSegs = min(minProfitSegs, profitCount)
        maxProfitSegs = max(maxProfitSegs, profitCount)

print(f"{minProfitSegs} {maxProfitSegs}")