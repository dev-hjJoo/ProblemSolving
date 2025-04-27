'''
풀이 방식
1. 종료시간으로 정렬
1.1 종료시간으로만 정렬했다가 실패. -> 1순위는 종료시간, 2순위는 시작시간으로 정렬해줘야했음
2. 예약 배열에 예약된 시간을 넣어줌
3. 이때, 신청 시작시간이 최근 예약된 시간의 종료시간 이후일 경우 예약 확정
----------
예제 입력1(1.1에 해당하는 예시)
5
3 3
1 2
2 3
3 4
4 5
'''
n = int(input())
schedule = sorted([list(map(int, input().split())) for _ in range(n)],key=lambda time: (time[1],time[0]))
print(schedule)
reservation=[schedule[0]]
for time in schedule[1:]:
    if time[0]>=reservation[-1][1]:reservation.append(time)

print(len(reservation))