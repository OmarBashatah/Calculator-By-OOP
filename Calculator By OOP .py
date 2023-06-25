while True :
    num1=float(input("enter your first number : "))
    num2=float(input("enter your second number : "))
    import random
    list=["+","-","*","/"]
    random_elemant=random.choice(list)
    print("your choosen operation system is : ",random_elemant)
    op= input("enter your choosen operation system : ")
    if op=="+":
        print(f'{num1}+{num2}={num1+num2}')
    elif op=="-":
        print(f'{num2}-{num1}={num2-num1}')
    elif op=="/":
        print(f'{num2}/{num1}={num2/num1}')
    elif op=="*":
        print(f'{num1}*{num2}={num1 * num2}')
    else :
        print(" invalid operation system ")
