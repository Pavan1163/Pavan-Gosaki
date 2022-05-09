#This is My first project of python
#By Pavan Gosaki
from random import random, randrange

ch=5
print("This is no guessing game between 1 to 100")
c=randrange(0,100)
while ch>0:
    try:
        no=int(input("Enter no :"))
    except:
        print("!! Only Integer values you have to enter !!s")
        exit()
    if(no<c):
        print("\nYour guessis too low")
        ch=ch-1
        print("total chances remaining :",ch)
    elif(no>c):
        print("\nYour guess is too high")
        ch=ch-1
        print("total chances remaining :",ch)
    else :
        print("\ncongratulation ! You won the game.")
        exit()
print("Better luck next time")
print("Answer is ",c)
