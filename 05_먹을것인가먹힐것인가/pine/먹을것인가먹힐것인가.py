case = int(input())
    
while case > 0:
    count = 0 # 정답값. A가 먹을 수 있는 B 경우의 수
    a_number, b_number = list(map(int, input().split())) 
    a = sorted(list(map(int, input().split())),reverse=True)
    b = sorted(list(map(int, input().split())))

    min_b = b[0]
    max_b = b[-1]

    start = 0
    end = b_number - 1 # 인덱스 값이기 때문에 -1

    for target in a:
        if target <= min_b: break # B의 최소값보다 타겟이 작을 경우 종료
        if target > max_b: # B의 최대값보다 타겟이 클 경우 B의 수량만큼 카운트 추가
            count += b_number
            continue
        
        # 이진 탐색 시작
        
        while start <= end:
            mid = (start + end)//2
            if target<=b[mid]:
                mid = mid-1
                end = mid
                if target > b[mid]: # b[mid] < target ≤ b[mid+1] 검증
                    break
                else: continue
            else: # (= b[mid] < target)인 경우
                start = mid+1
                if target < b[mid+1]: # b[mid] < target ≤ b[mid+1] 검증
                    break 
                else: continue
                
        # 이진탐색 종료. mid값을 찾은 후, star/end 값 초기화
        start = 0
        end = mid # A는 내림차순 정렬이기 때문에, 다음 타겟의 end는 현태 타겟의 mid보다 반드시 작다.
        count += mid+1 # mid는 인덱스값이기 때문에 수량으로 변환(+1)
    print(count)
    case -= 1