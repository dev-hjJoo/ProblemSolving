from collections import deque
field = []
directions = [[-1, 0], [0, -1], [1, 0], [0, 1]] # 상하좌우


def bfs(color, x, y, visited):
    ''' 
        동일 색상에 대해 BFS를 수행하는 함수 (반환값: 인접한 동일한 색상의 개수)
    
        <Parameters>
        - color: 현재 탐색해야 할 색상
        - x, y: 시작 좌표
        - visited: 방문 여부 판단 배열
    '''
    queue = deque([(x, y)]) # BFS 탐색용 큐
    coords = [(x, y)] # 4개 이상일 때 제거를 위해 반환할 좌표 배열
    cnt = 1
    while queue:
        cx, cy = queue.popleft()
        
        visited[cx][cy] = True # 방문 처리
        for dx, dy in directions:
            nx, ny = cx+dx, cy+dy
            if (nx >= 0 and nx < 6) and (ny >= 0 and ny < 12): # 배열 범위 내
                if field[nx][ny] == color and not visited[nx][ny]:
                    queue.append((nx, ny))
                    coords.append((nx, ny))
                    cnt += 1
                    visited[nx][ny]=True
    return cnt, coords


# 필드 입력
for _ in range(12):
    field.append(input())

# 필드 90도 시계방향으로 회전
field = [list(e) for e in zip(*field[::-1])]

answer = 0
while True:
    visited = [[False]*12 for _ in range(6)] # 방문 여부 판단 배열

    remove_coords = [] # 1연쇄 시 제거해야 할 좌표들

    for x in range(6):
        for y in range(12):
            if field[x][y] != '.':
                if not visited[x][y]:
                    cnt, coords = bfs(field[x][y], x, y, visited)
                    if cnt >= 4: 
                        remove_coords.extend(coords)

    if len(remove_coords) > 0:
        # Clear
        Xs = []
        for x in range(6):
            col = ''
            for y in range(12):
                if (x, y) not in remove_coords and field[x][y] != '.':
                    col += field[x][y]
            field[x] = list(col.ljust(12, '.'))

        answer += 1
    else:
        print(answer)
        break