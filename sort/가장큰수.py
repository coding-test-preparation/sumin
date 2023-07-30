def solution(numbers):
    answer = ''
    answers = list(map(str, numbers))
    # map 함수 >> map(함수, list)
    answers.sort(key=lambda x: x*4, reverse=True)
    answer = ''.join(answers)
    #예외 case = numbers가 전부 0일때:
    if int(answer) == 0:
        answer = str(0)
    return answer
