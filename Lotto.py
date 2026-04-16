import random
lotto_list=[]
a=int(random.randint(1,45))
lotto_list.append(a)
print("** 로또 추첨을 시작합니다. **")
for i in range (5):
    
    while a in lotto_list:
        a=int(random.randint(1,45))
    lotto_list.append(a)
lotto_list.sort()
print("추첨된 로또 번호 ==> ",end='')
for i in range(6):
    print("%d "%lotto_list[i],end='')
