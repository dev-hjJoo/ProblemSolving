def getExpectedEXP(target: int, exp_type: str):
    '''
        누적 경험치를 계산해주는 함수 (반환값: 예상 경험치 누적 합)
       
        <Parameter>
        - target: 경험치를 구하려는 범위 (MONSTER → 슬라임 수 / LEVEL_UP → 레벨)
        - exp_type: 경험치 유형 (1. MONSTER: 슬라임 처치 경험치 / 2. LEVEL_UP: 레벨업 필요 경험치)
    
    '''
    if exp_type == 'MONSTER':
        s, l, n = 1, target, target
    else: # LEVEL_UP
        s, l, n = 0, 2*(target-1), target
    
    exp = n * (s+l) // 2 # 등차수열 합 공식
    return exp


t = int(input())
for _ in range(t):
    killed_monsters = int(input())

    expected = -1
    user_exp = getExpectedEXP(killed_monsters, 'MONSTER')
    
    st, en = 1, killed_monsters # 레벨이 몬스터 잡은 수보다 클 수 없으므로 마지막 값으로 설정
    while st <= en:
        mid = (st + en) // 2
        expected = getExpectedEXP(mid, 'LEVEL_UP')

        if expected < user_exp: st = mid + 1 
        elif expected > user_exp: en = mid - 1
        else: break # 딱 일치하는 경우
    if expected > user_exp: mid = mid - 1
    print(mid)