'''
문제 풀이 2
1. 숫자의 개수 = N*N
2. (숫자의 개수)/2 와 K를 비교해 배열의 크기를 절반으로 축소
2.1 K가 클 경우 배열 = (1 ~ N) * ((N/2)+1 ~ N)
2.2 K가 작을 경우 배열 = (1 ~ N) * ((1~(N/2+나머지))
3. 남은 숫자의 개수 = ((N/2)+1) * N개
4. 반복하며 범위 축소
4.1 언제까지? 시작인덱스와 종료인덱스가 같을때까지

결과: 값이 정렬되지 않은 상태여서 정렬된 값을 구할 수 없음
'''
import math

n = int(input())
k = int(input())

startIndex = 1
endIndex = n
number= n*n  # 숫자의 개수

while startIndex != endIndex: 
    isAboveMid = (number/2)<=k #16
    if isAboveMid: startIndex += math.ceil((endIndex-startIndex)/2)
    else: endIndex = sum(divmod(endIndex, 2)) # K가 같거나 작을 경우의 배열
    number = (endIndex-startIndex+1)*n

b = [i*j for i in range(1,n+1) for j in range(startIndex,endIndex+1)]
index = k-(n*n-n) # (endIndex-1) = 현재 선택된 행 이전의 행 -> *n을 하여 앞의 숫자 개수를 계산해서 k에서 빼준다.
print(b[index])
