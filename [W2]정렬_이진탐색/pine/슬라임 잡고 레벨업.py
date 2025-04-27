n = int(input())

def getNeedExp(y):
    return y*y-y
    
for _ in range(n):
    monster = int(input())
    exp = (monster*(1+monster))/2 # 획득 경험치수. 시작경험치:1, 마지막경험치:monster -> 등차수열 식
    # needExp = 2
    # y레벨일때, 레벨업에 필요한 경험치 -> 등차수열 식
    # ((y-1) *(2+(2y-2)))/2 => y*y -y
    # (y-1) = 레벌업 횟수
    # 2 = 최초 레벨업에 필요한 경험치
    # (2*y - 2) = 마지막 레벨업에 필요한 경험치
    start= 1
    end=monster
    lv= int((start+end)//2)
    if(monster == 1):
        print(1)
    else:
        while not (getNeedExp(lv) <= exp <= getNeedExp(lv + 1)):
            if exp >getNeedExp(lv): #경험치남음
                start=lv
            else: #경험치부족
                end=lv
            lv= int((start+end)//2)
        print(lv)
