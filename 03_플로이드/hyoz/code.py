cnt_city = int(input())
cnt_bus = int(input())

INIT_VALUE = int(1e9)

# 비용 ≤ 10만이므로 초기값 10만+1
# 시작 도시와 도착 도시 같은 경우 없으므로 대각선 0
costs = [[INIT_VALUE if i!=j else 0 for j in range(cnt_city)] for i in range(cnt_city)]

for _ in range(cnt_bus):
    st, en, cost = map(int, input().split())
    i, j = st-1, en-1
    costs[i][j] = min(costs[i][j], cost)

for n in range(cnt_city):
    for i in range(cnt_city):
        if i == n: continue # 현재 도시 N에 대해서는 확인 X (거쳐가는 경로만 확인)
        for j in range(cnt_city):
            if j == n or i==j: continue # 현재 도시 N에 대해서는 확인 X (거쳐가는 경로만 확인)
            costs[i][j] = min(costs[i][j], costs[i][n]+costs[n][j])

# 출력
for i in range(cnt_city):
    for j in range(cnt_city):
        cost = costs[i][j] if costs[i][j] != INIT_VALUE else 0
        print(cost, end=' ')
    print()