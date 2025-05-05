streets, drivers = map(int, input().split())
streetNames = [input() for x in range(streets)]
streetIndices = {name: i for i,name in enumerate(streetNames)}
driverDirections = [input().split() for i in range(drivers)]

for driver in driverDirections:
    start = driver[0]
    end = driver[1]
    print(abs(streetIndices.get(end) - streetIndices.get(start))-1)