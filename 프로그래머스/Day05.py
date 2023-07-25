# 옷가게 할인 받기
import math
def solution(price):
    answer = 0
    if price >= 500000:
        answer = math.trunc(price*0.8)
    elif price >= 300000:
        answer = math.trunc(price*0.9)
    elif price >=100000:
        answer = math.trunc(price*0.95)
    else:
        answer = price
    return answer

# 아이스 아메리카노
def solution(money):
    return divmod(money, 5500)

# 나이 출력
def solution(age):
    answer = 2023-age
    return answer

# 배열 뒤집기
def solution(num_list):
    num_list.reverse()
    return num_list
