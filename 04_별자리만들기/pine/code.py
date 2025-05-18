import math

n = int(input())

stars = [list(map(float,input().split())) for _ in range(n)] # 별들의 좌표 정보
root = [i for i in range(n)] # 별의 root 정보가 담긴 배열
cost = 0 # 정답 비용
edge = [] # 모든 별들이 연결된 간선 정보와 별 사이의 거리를 저장할 배열. 구조:모든 간선 정보[거리, 시작인덱스, 종료 인덱스]

def getDistance(star1,star2):
    x1, y1=star1
    x2, y2=star2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
def find(x):
    if root[x]!=x:
        root[x]=find(root[x])
    return root[x]

def union(star1,star2):
    root1=find(star1)
    root2=find(star2)

    if root1<root2: root[root2]=root1
    else: root[root1]=root2

for i in range(n): # 모든 간선을 제작하고, 해당 간선의 거리를 구해서 edge에 추가
    for j in range(i,n):
        if i!=j:
            edge.append([getDistance(stars[i],stars[j]),i,j])

edge = sorted(edge) # 비용순으로 정렬

for distance,index1,index2 in edge: # 간선 리스트를 반복하며 별들을 연결하고 비용을 계산한다.
    # root별이 같은 경우를 필터링 하기위함 -> root별이 같은데 union하면 사이클이 발생하기 때문
    if find(index1) != find(index2): # root별이 같지 않을 경우(= 사이클이 발생하지 않는 경우, => 이상태에서 unioin을 하면 그때 사이클이 발생한다.)
        union(index1,index2) # index1,index2의 별을 연결
        cost+=distance

print(f"{cost:.2f}")