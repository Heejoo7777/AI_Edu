import sys

s = list(input("대상 문자열 입력: "))   
t = list(input("제거할 문자열 입력: ")) 

i = 0
result=[]


for i in s:
    if (i != t[0]):
        result.append(i)

result.reverse()

newS = str(result) #문자열로 바꿈
for i in newS:
    print(i , end='')
#print("결과 문자열은 {}입니다.".format(newS))
