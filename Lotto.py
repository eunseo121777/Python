import random
lotto_list=[]
a=0
print("로또 추첨을 시작합니다.")
for i in range (6):
    
    while a in lotto_list:
        a=int(random.randint(1,45))
    lotto_list.append(a)

print("추첨된 로또 번호 ==>",lotto_list)
