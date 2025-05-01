from collections import defaultdict

def printFloorPlan(plan: list) -> None:
    print("\n********************FLOOR PLAN********************",end="\n")
    for x in range(len(plan)):
        for char in plan[x]:
            print(char,end=" ")
        print()
    print("********************END********************\n")

def bpm(u, visited):
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            if match_to[v] == -1 or bpm(match_to[v], visited):
                match_to[v] = u
                return True
    return False

height, width, time = map(int, input().split())

exitPositions = []
playerPositions = []
distances = [-1]*height
floorPlan = [0]*height
for h in range(height):
    newline = input()
    col = [0]*width
    dist = [-1]*width
    for w in range(width):
        col[w] = (newline[w])
        if (newline[w] == "E"):
            exitPositions.append([h,w])
        elif (newline[w] == "P"):
            playerPositions.append([h,w])
    floorPlan[h] = col
    distances[h] = dist

ct = 0
myQueue = []
for exit in exitPositions:
    distances[exit[0]][exit[1]] = 0
    myQueue.append(exit)

directions = [[-1,0],[1,0],[0,-1],[0,1]]
while len(myQueue) > 0:
    #printFloorPlan(distances) #TESTING PURPOSES

    ct += 1
    point = myQueue.pop(0)
    
    for dir in directions:
        newX = point[0] + dir[0]
        newY = point[1] + dir[1]

        if (newX >= 0 and newX < height and newY >= 0 and newY < width and distances[newX][newY] == -1 and floorPlan[newX][newY] != "#"):
            distances[newX][newY] = distances[point[0]][point[1]] + 1
            myQueue.append([newX,newY])  

graph = defaultdict(list)
exitTimeDictionary = {}
exitID = 0
for pid, (px, py) in enumerate(playerPositions):
    for t in range(time + 1):
        for ex, ey in exitPositions:
            if distances[px][py] == -1:
                continue
            if distances[px][py] <= t:
                key = (ex, ey, t)
                if key not in exitTimeDictionary:
                    exitTimeDictionary[key] = exitID
                    exitID += 1
                graph[pid].append(exitTimeDictionary[key])

V = exitID
U = len(playerPositions)

match_to = [-1] * V 

result = 0
for u in range(U):
    visited = [False] * V
    if bpm(u, visited):
        result += 1

print(result)