import random
number=random.randint(1,100)
attempt=0

print("Guess the number!")
a=int(input())

while True: 
    if(a<number):
        print("Enter a greater number!")
        attempt+=1
        a=int(input())

    elif(a>number):
        print("Enter a lower number!")
        attempt+=1
        a=int(input())

    else:
        attempt+=1
        print("You guessed the number ",number," in ",attempt,"attempts")
        break



