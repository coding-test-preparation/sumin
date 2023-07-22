# 나머지 구하기

def solution(num1, num2):
    namuge = num1%num2
    answer = int(namuge)
    return answer

# 중앙값 구하기

def solution(array):
    array.sort()
    i = len(array)/2
    i = int(i)
    answer = array[i]
    
    return answer

