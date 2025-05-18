n = int(input())

scores = [int(input()) for _ in range(n)]
max_scores = []

for c_step in range(n):
    c_score = scores[c_step]
    
    # f_score: 현재 위치가 첫 번째 스텝일 때 최대값
    # s_score: 현재 위치가 두 번째 스텝일 때 최대값
    if c_step < 2:
        f_score = c_score
    else:
        f_score = max(max_scores[c_step-2])+c_score
    
    s_score = max_scores[c_step-1][0]+c_score if c_step >= 1 else 0 
    
    # 최대값 배열에 점수 업데이트
    max_scores.append([f_score, s_score])

# 4. 목표 위치의 최대 점수 출력
print(max(max_scores[-1]))