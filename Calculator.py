a = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계: "))
if a == 1:
    susik_str = input("*** 수식을 입력하세요 : ")
    susik_aws = eval(susik_str)
    print("%s 결과는 %5.1f입니다."%(susik_str,susik_aws))

elif a == 2:
    
    start = 0
    first = int(input("*** 첫 번째 숫자를 입력하세요:"))
    second = int(input("*** 두 번째 숫자를 입력하세요:"))
    for t in range(first,second+1):
        start += t
    print("%d+...+%d는 %d입니다."%(first,second,start))