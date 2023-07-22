# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]


## 내풀이

import math
def solution(progresses, speeds):
    answer = []
    compare = []
    now = 0

    for i in range(len(progresses)):
        a = 100 - progresses[i]
        b = math.ceil(a/speeds[i])
        compare.append(b)
    print(compare)

    for i in range(1,len(progresses)):
        if compare[i] > compare[now]:
            answer.append(i-now)
            now = i
    answer.append(len(progresses)-now)
    print(answer)

    return answer
