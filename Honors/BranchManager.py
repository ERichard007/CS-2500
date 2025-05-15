def GetParents(city):
    for child in adjacencyList[city]:
        parent[child] = city
        GetParents(child)

def GetPath(dest):
    path = []
    while dest != 0:
        path.append(dest)
        dest = parent[dest]
    return path[::-1]


numCities, numPeople = map(int, input().split())

adjacencyList = [[] for x in range(numCities+1)]
for x in range(numCities-1):
    root, child = map(int, input().split())
    adjacencyList[root].append(child)

for child in adjacencyList:
    child.sort()

personDestination = [int(input()) for x in range(numPeople)]

parent = [0] * (numCities + 1)
GetParents(1) 

ptr = [0] * (numCities + 1)
peopleArrived = 0

#print("***STARTING***")
for destination in personDestination:
    path = GetPath(destination)
    #print(destination)
    #print(path)
    #print(adjacencyList)

    found = True
    for node in range(len(path)-1):
        curr = path[node]
        next = path[node+1]
        #print(f'for node {path[node]}')
        while ptr[curr] < len(adjacencyList[curr]) and adjacencyList[curr][ptr[curr]] < next:
            ptr[curr] += 1

        #print(adjacencyList)

        if ptr[curr] == len(adjacencyList[curr]) or adjacencyList[curr][ptr[curr]] != next:
            found = False
            break

    #print(found)
    if found: 
        peopleArrived += 1
    else:
        break

print(peopleArrived)