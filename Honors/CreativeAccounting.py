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