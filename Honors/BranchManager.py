import sys
sys.setrecursionlimit(2 * 10**5)
input = sys.stdin.readline

num_cities, num_people = map(int, input().split())

adjacency_list = [[] for _ in range(num_cities)]
parent = [0] * num_cities

for _ in range(num_cities - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    parent[b] = a
    adjacency_list[a].append(b)

for children in adjacency_list:
    children.sort()

entry_time = [-1] * num_cities
exit_time = [-1] * num_cities
time = 0

def dfs(node):
    global time
    entry_time[node] = time
    time += 1
    for child in adjacency_list[node]:
        dfs(child)
    exit_time[node] = time
dfs(0)

max_entry_seen = -1

for i in range(num_people):
    destination = int(input()) - 1

    if exit_time[destination] <= max_entry_seen:
        print(i)
        exit(0)

    max_entry_seen = max(max_entry_seen, entry_time[destination])

print(num_people)
