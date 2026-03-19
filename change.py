a=int(input("입력 진수 결정(16/10/8/2)"))
b=input("값 입력")

if (a==2):
    b=int(b,2)
    print("2진수:", bin(b))
    print("8진수:", oct(b))
    print("10진수:", b)
    print("16진수:", hex(b))
    
elif (a==8):
    b=int(b,8)
    print("2진수:", bin(b))
    print("8진수:", oct(b))
    print("10진수:", b)
    print("16진수:", hex(b))

elif (a==10):
    b=int(b,10)
    print("2진수:", bin(b))
    print("8진수:", oct(b))
    print("10진수:", b)
    print("16진수:", hex(b))

elif (a==16):
    b=int(b,16)
    print("2진수:", bin(b))
    print("8진수:", oct(b))
    print("10진수:", b)
    print("16진수:", hex(b))