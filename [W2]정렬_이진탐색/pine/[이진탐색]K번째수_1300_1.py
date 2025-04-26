'''
문제 풀이 1
1. 입력받은 N을 이용해서 배열 B를 제작한다.
1.1 1-N까지의 값을 반복문을 이용해 제작.
2. B를 오름차순 정렬한다. 
3. B[k]를 구한다. -> 어차피 배열이니까 Index값으로 뽑으면 되는데 왜 이진 탐색인거지?

결과: 메모리초과
'''

n = int(input())
k = int(input())

b=sorted([i*j for i in range(1,n+1) for j in range(1,n+1)])
print(b[k])
