from collections import deque
import heapq
import copy

mazePrintedCount = 1
def PrintMaze(m):
    global mazePrintedCount
    print(f'******************************************* MAZE:{mazePrintedCount}')
    for r in range(rows):
        for c in range(columns):
            print(m[r][c],end="")
        print()
    print("*******************************************")
    mazePrintedCount+=1

rows, columns = map(int, input().split())

maze = []
totalDots = 0
for _ in range(rows):
    line = list(input())
    totalDots += line.count(".")
    maze.append(line)

entrancePosition = []
for c in range(columns):
    if 'A' <= maze[0][c] <= 'W':
        entrancePosition.append((0, c))
    if 'A' <= maze[rows - 1][c] <= 'W':
        entrancePosition.append((rows - 1, c))

for r in range(1, rows - 1):
    if 'A' <= maze[r][0] <= 'W':
        entrancePosition.append((r, 0))
    if 'A' <= maze[r][columns - 1] <= 'W':
        entrancePosition.append((r, columns - 1))

#PrintMaze(maze)

#tempMaze = maze #copy so wont mess up original [THIS IS FOR TESTING]
moveDirections = [[-1,0],[1,0],[0,-1],[0,1]] #up, down, left, right
reachablesDots = {} #key = entrance; value = dot coordinate
visited = {} #universal visited for decreasing amount of mazes generated

for entrance in entrancePosition:
    #tempMaze = copy.deepcopy(maze)

    #print(f'$$$$$$$$$$$$$$$$$ FOR ENTRANCE {maze[entrance[0]][entrance[1]]} $$$$$$$$$$$$$$$$$')
    entranceChar = maze[entrance[0]][entrance[1]]
    if entranceChar not in reachablesDots:
        reachablesDots[entranceChar] = set()

    queue = deque([entrance])
    visited[entrance] = entranceChar

    while queue:
        pos = queue.pop()
        #tempMaze[pos[0]][pos[1]] = "*"
        #PrintMaze(tempMaze)

        for dx, dy in moveDirections:
            nx, ny = [pos[0]+dx,pos[1]+dy]
            if not (0 <= nx < rows and 0 <= ny < columns):
                continue
            if maze[nx][ny] not in {".", " "}:
                continue
            if (nx, ny) in visited:
                otherEntrance = visited[(nx, ny)]
                if otherEntrance != entranceChar:
                    #print(f'GOT OTHER ENTRANCE {entrance} FOUND {otherEntrance}')
                    reachablesDots[entranceChar].update(reachablesDots[otherEntrance])
                    for dot in reachablesDots[otherEntrance]:
                        visited[dot] = entranceChar
                continue
            else:
                visited[(nx, ny)] = entranceChar
                if maze[nx][ny] == ".":
                    reachablesDots[entranceChar].add((nx, ny))
                queue.append((nx, ny))

    
#print("$$$$$$$$$$$$$$$$$")
#print(reachablesDots)

allDots = set()
for dots in reachablesDots.values():
    allDots.update(dots)

selectedEntrances = []
dotsCovered = set()
heap = [] 
for entrance in reachablesDots:
    heapq.heappush(heap (-len(reachablesDots[entrance]), entrance))

while dotsCovered != allDots and heap:
    _, bestEntrance = heapq.heappop(heap)
    newDots = reachablesDots[bestEntrance] - dotsCovered
    if not newDots:
        continue
    selectedEntrances.append(bestEntrance)
    dotsCovered.update(newDots)

#print(selectedEntrances)
#print(dotsCovered)


print(len(selectedEntrances), totalDots - len(allDots)) 