import random
lotto_list=[]
a=int(random.randint(1,45))
lotto_list.append(a)
print("** 로또 추첨을 시작합니다. **")
for i in range (5):
    
    while a in lotto_list:
        a=int(random.randint(1,45))
    lotto_list.append(a)

print("추첨된 로또 번호 ==>",lotto_list[0],lotto_list[1],lotto_list[2],lotto_list[3],lotto_list[4],lotto_list[5])
