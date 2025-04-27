n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]

# 종료시간 기준 정렬
meetings = sorted(meetings, key=lambda x: (x[1], x[0]))

answer, time = 0, -1
for st, en in meetings:
    if st >= time: 
        time = en # 기준 시간(time)을 종료 시간으로 업데이트
        answer += 1
print(answer)