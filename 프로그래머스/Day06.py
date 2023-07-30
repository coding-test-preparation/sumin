# 문자열 뒤집기

def solution(my_string):
    answer = ''
    word = []
    
    for i in my_string:
        word.append(i)
    
    word.reverse()
    for i in word:
        answer = answer+i
    return answer
# 직각삼각형 출력하기
num = int(input())

for i in range(1,num+1):
    print('*'*i)
# 짝수 홀수 개수
def solution(num_list):
    
    answer = []
    num_list.sort()
    num_list.reverse()
    jjack = 0
    hol = 0
    for i in num_list:
        if i % 2 == 0:
            jjack = jjack+1
        else:
            hol = hol + 1
    answer.append(jjack)
    answer.append(hol)
    
    return answer

# 문자 반복 출력하기
def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer = answer + i*n
    return answer
