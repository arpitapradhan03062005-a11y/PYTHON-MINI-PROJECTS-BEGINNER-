import random 

n = random.randint(1,100)
a = int(input("Enter number :"))

count = 1
while(a != n):
    count += 1
    if(a<n):
        print("Higher number!!")
    else:
        print("Lower number!!")
    a = int(input("Enter number :"))

print(f"You have guessed {n} number in {count} guesses")
