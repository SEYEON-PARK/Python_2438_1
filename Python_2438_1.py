'''
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
'''

N=int(input()) # 사용자로부터 정수 입력받기
num=1 # num 선언 및 초기화

for i in range(N): # i에 0부터 N-1까지 대입하며 반복
    for j in range(num): # j에 0부터 num-1까지 대입하며 반복
        print("*", end="") # 별 출력하기
    num+=1 # num에 num+1 대입하기
    print() # 한 줄 띄기
