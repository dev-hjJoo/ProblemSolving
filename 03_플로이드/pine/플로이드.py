INF = 9999999

city_number = int(input())
bus_number = int(input())

graph = [[INF]*(city_number) for _ in range(city_number)]

for _ in range(bus_number):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1],c)

for i in range(city_number):
    graph[i][i]=0

for k in range(city_number):
    for i in range(city_number):
        for j in range(city_number):
            graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])
            
for i in range(city_number):
    for j in range(city_number):
        result = graph[i][j] if graph[i][j]!=INF else 0
        print(result, end=" ") 
        
    print()