def solution(numbers, target):
    sup=[0]
    for i in numbers:
        sub=[]
        for j in sup:
            sub.append(j+i)
            sub.append(j-i)
        sup=sub
    return sup.count(target)

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']


tickets=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

def dfs(graph, start_node):
    visited, need_visit = list(), list() 
    need_visit.append(start_node)
    print(visited,need_visit)
    while need_visit:
        node = need_visit.pop()

        if node not in visited:
            visited.append(node)
            if graph.get(node):
                need_visit.append(graph.get(node))

    return visited

def solution(tickets):
    graph = dict()

    for i in tickets:
        graph[i[0]] = graph[i[0]]
    answer=dfs(graph,tickets[0][0])
    print(answer)
    return answer
solution(tickets)
"""from sys import stdin
n, m, v = map(int, stdin.readline().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    line = list(map(int, stdin.readline().split()))
    matrix[line[0]][line[1]] = 1
    matrix[line[1]][line[0]] = 1
"""
computers=[[1, 1, 0], [1, 1, 1], [0, 1, 1]]


def dfs(current_node, row, foot_prints):
    foot_prints += [current_node]
    for search_node in range(len(row[current_node])):
        if row[current_node][search_node] and search_node not in foot_prints:
            foot_prints = dfs(search_node, row, foot_prints)
    return foot_prints


count=0
need = [i for i in range(len(computers[0]))]
while True:
    print(need)
    visited=dfs(need[0],computers,[])
    print(visited,-1)
    for j in visited:
        need.remove(j)
    count=count+1

    if len(need)==0:
        print(count)
        break

def dfs(current_node, row, foot_prints):
    foot_prints += [current_node]
    for search_node in range(len(row[current_node])):
        if row[current_node][search_node] and search_node not in foot_prints:
            foot_prints = dfs(search_node, row, foot_prints)
    return foot_prints

def solution(n, computers):
    count = 0
    need = [i for i in range(n)]
    while True:
        visited = dfs(need[0], computers, [])
        for j in visited:
            need.remove(j)
        count = count + 1

        if len(need) == 0:
            answer=count
            return answer