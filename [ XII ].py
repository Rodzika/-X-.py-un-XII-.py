#1.uzd
import random

lielaka_summa = 0

for i in range(10):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(f'{dice1} / {dice2}')
    if dice1 > dice2:
        print(f'{dice1} {dice2} / {dice1} / {dice1+dice2}')
        
    elif dice2 > dice1:
        print(f'{dice1} {dice2} / {dice2} / {dice1+dice2}')
        
    if dice1+dice2 > lielaka_summa:
       lielaka_summa = dice1+dice2 
    
print(lielaka_summa)

#2.uzd
input random
answer = random.randrange(1, 11)
chance = 0
while chance < 5:
    guess = int(input("Guess number between 1 and 10: "))
    
    if guess == answer:
        print("Uzminēts!")
    if guess < answer :
        print("Augstāks!")
    if guess > answer:
        print("Zemāks")
        
        chance += 1
    if chance == 5:
        print("Spēle peigusies. atbilde bija:", answer)
        
